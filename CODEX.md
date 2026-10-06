# pstack for Codex

This fork adds a self-contained Codex adaptation of Lauren Tan's pstack. The
upstream Cursor package remains unchanged in `pstack/`. The Codex package lives
in `codex/skills/poteto-mode/` and retains the upstream MIT license.

This is an initial core port, not full feature parity. One discoverable skill
routes to focused references instead of installing dozens of global skill names.
The port preserves investigation, domain-first design, reproduce-before-fix,
behavioral verification, arena/swarm patterns, adversarial review, and scoped PR
delivery. It adapts the workflow to the tools available in each Codex session.

## Install

Requires Python 3.9 or later. From this checkout, install for a project:

```sh
python3 codex/install.py --project /absolute/path/to/your/project
```

Or install for your user:

```sh
python3 codex/install.py --user
```

The installer copies the entire skill, references, UI metadata, and license into
the selected `.agents/skills` directory. It is safe to rerun with identical files.
It refuses to replace a different skill, local customizations, or a symlink.
To update, preserve the existing folder elsewhere and rerun the installer. It
does not change model settings, credentials, or install other plugins.

Select **Poteto Mode for Codex** in the skill picker, or mention it explicitly:

```text
Use $poteto-mode to reproduce the idle scrolling bug, fix its cause, and verify it.
Use $poteto-mode to explain how cancellation reaches the database. Do not edit files.
Use $poteto-mode to interrogate this diff for correctness and missing cases.
Use $poteto-mode to compare two designs for the cache and implement the better one.
```

If it does not appear after installation, restart Codex. To uninstall, remove only
the installed `poteto-mode` folder after preserving any customizations.

## Compatibility

| Capability | This port |
| --- | --- |
| Investigation, debugging, design, refactoring, prototypes | Included |
| Runtime/trace diagnosis, performance measurement, hillclimbing | Included |
| Review, PR preparation, status/repair, shipping, pause/resume | Included; actions stay within user authorization |
| Arena/swarm and independent review | Uses available subagent tools when permitted; sequential fallback |
| Claude/Grok/OpenAI multi-model panel | No bundled external providers; uses only models exposed and permitted by the host |
| Separate `/how`, `/arena`, etc. commands | Not installed; request these workflows through `$poteto-mode` |
| Cursor persistent custom mode and `/loop` | Not emulated; use Codex's available session/scheduling capabilities |
| Benny Slack automation, bot UI, transcript mining, automatic skill correction | Not ported |
| Upstream's complete 23-playbook orchestration and evaluation machinery | Not ported; longer work uses the simpler delivery reference |

The skill cannot create tools, bypass permissions, grant external-action authority,
or guarantee that an agent follows every instruction. Same-model independent
reviews are not described as multi-model consensus. Native UI verification needs
an appropriate host tool; source inspection alone is not visual verification.

## Validate

```sh
python3 -m unittest discover -s codex/tests -v
```

The tests execute project installation and verify idempotency, preservation of
customizations and collisions, and completeness of the installed references.
These checks validate packaging, not agent behavior. End-to-end model evaluations
and an installed Codex UI smoke test are still needed before claiming behavioral
parity with upstream.

## Upstream maintenance

Adapted from `cursor/plugins` commit
`df581122cde17e6e27686b5a448bde23e4ad4318` (pstack 0.15.15).
Preserve `pstack/` as the upstream source and make Codex changes in `codex/`.
When syncing, compare the changed upstream skills and playbooks, port relevant
behavior deliberately, update this baseline, and rerun installation checks.
Do not mechanically replace tool names across all upstream files: authorization,
model routing, background execution, and UI verification have different semantics.

References: [upstream pstack](https://github.com/cursor/plugins/tree/main/pstack),
[OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills), and
[OpenAI subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).
