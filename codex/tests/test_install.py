import importlib.util
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("pstack_install", ROOT / "install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.destination = Path(self.temp.name) / "skills"

    def test_self_contained_copy_and_idempotent_retry(self):
        target, created = installer.install(self.destination)
        self.assertTrue(created)
        self.assertEqual(installer.snapshot(target), installer.snapshot(installer.SOURCE))
        self.assertFalse(installer.install(self.destination)[1])
        self.assertTrue((target / "LICENSE").is_file())
        for document in target.rglob("*.md"):
            for link in re.findall(r"\]\(([^)]+)\)", document.read_text()):
                if "://" not in link and not link.startswith("#"):
                    resolved = (document.parent / link.split("#")[0]).resolve()
                    self.assertTrue(resolved.is_relative_to(target.resolve()), link)
                    self.assertTrue(resolved.is_file(), f"Broken link: {document}: {link}")

    def test_local_modification_is_preserved(self):
        target, _ = installer.install(self.destination)
        document = target / "SKILL.md"
        document.write_text("local customization")
        with self.assertRaises(FileExistsError):
            installer.install(self.destination)
        self.assertEqual(document.read_text(), "local customization")

    def test_additional_user_file_is_preserved(self):
        target, _ = installer.install(self.destination)
        extra = target / "my-notes.md"
        extra.write_text("keep me")
        with self.assertRaises(FileExistsError):
            installer.install(self.destination)
        self.assertEqual(extra.read_text(), "keep me")

    def test_symlink_is_preserved(self):
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        self.destination.mkdir()
        target = self.destination / installer.SOURCE.name
        target.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(FileExistsError):
            installer.install(self.destination)
        self.assertTrue(target.is_symlink())
        self.assertEqual(list(outside.iterdir()), [])

    def test_project_cli_with_spaces(self):
        project = Path(self.temp.name) / "example project"
        command = [sys.executable, str(ROOT / "install.py"), "--project", str(project)]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((project / ".agents/skills/poteto-mode/SKILL.md").exists())
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Already installed", result.stdout)

    def test_file_collision_is_preserved(self):
        self.destination.mkdir()
        target = self.destination / installer.SOURCE.name
        target.write_text("existing file")
        with self.assertRaises(FileExistsError):
            installer.install(self.destination)
        self.assertEqual(target.read_text(), "existing file")


if __name__ == "__main__":
    unittest.main()
