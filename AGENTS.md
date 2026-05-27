# Agent Guide

This repository contains the `visual-ppt-builder` Codex skill. Follow this file
when changing the skill itself.

## Scope

The runtime skill entry is [SKILL.md](SKILL.md). Keep it compact. Put detailed
procedures, schemas, examples, and edge-case guidance in `references/`.

Human-facing project documentation belongs in `README.md`, `INDEX.md`, and
`RULES.md`. Do not duplicate large reference sections across multiple files.

## Editing Principles

- Preserve the core workflow: ask when needed, design prompts, generate one
  draft per slide, validate ratios, reconstruct editably, validate PPTX.
- Keep `SKILL.md` under control. Add links to references instead of expanding
  it into a full manual.
- Prefer deterministic scripts for repeated checks or package inspection.
- Keep docs ASCII unless there is a clear reason to add localized examples.
- Do not weaken the editability rules to make generation faster.
- Do not remove ratio validation or the ban on slicing generated contact sheets.

## File Map

- `SKILL.md`: skill trigger metadata and runtime workflow
- `README.md`: human overview and install/use instructions
- `INDEX.md`: Markdown navigation
- `RULES.md`: stable operational rules
- `references/`: detailed procedural guidance
- `scripts/`: helper scripts for building and validating decks
- `agents/openai.yaml`: UI-facing skill metadata

## Validation

After changing metadata, docs, or scripts, run:

```bash
python C:/Users/hersh/.codex/skills/.system/skill-creator/scripts/quick_validate.py ./visual-ppt-builder
```

When touching `scripts/build_ppt.py`, also run it against a small sample plan if
one is available.

When touching `scripts/validate_drafts.py` or image-generation rules, test with
a folder of known 16:9 images and a folder with a wrong-ratio image.

When touching `scripts/validate_ppt.py`, test with at least one generated PPTX.

## Installed Copy

The installed skill may live at:

```text
C:/Users/hersh/.codex/skills/visual-ppt-builder
```

After repository edits, sync the folder there when the user wants the local
Codex installation updated.

## Release Checklist

1. Update docs and references.
2. Run `quick_validate.py`.
3. Sync the installed skill copy if needed.
4. Confirm `git status --short`.
5. Commit with a concise message.
6. Push when requested or when continuing the existing publish workflow.
