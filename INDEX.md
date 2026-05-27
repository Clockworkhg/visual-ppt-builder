# Markdown Index

This index maps the skill's Markdown files and when to read each one.

## Runtime Entry

- [SKILL.md](SKILL.md)  
  Main runtime instructions loaded when the skill triggers. Keep this concise
  and focused on workflow, routing, hard rules, artifacts, and script commands.

## Repository Docs

- [README.md](README.md)  
  Human-facing overview, use cases, workflow, output structure, install notes,
  and validation commands.

- [RULES.md](RULES.md)  
  Stable operational rules for generation, editability, draft ratios, asset
  reconstruction, user questions, and failure recovery.

- [AGENTS.md](AGENTS.md)  
  Maintenance guide for coding agents editing this repository.

## Reference Files

- [references/decision-gates.md](references/decision-gates.md)  
  Read when the request has subjective style choices, missing source facts,
  uncertain page count, fidelity tradeoffs, or approval checkpoints.

- [references/visual-prompt-strategy.md](references/visual-prompt-strategy.md)  
  Read before image generation when the user gives a short prompt, style is
  subjective, or generated images need a stronger art direction.

- [references/image-prompting.md](references/image-prompting.md)  
  Read before generating slide drafts, backgrounds, or visual assets.

- [references/asset-reconstruction.md](references/asset-reconstruction.md)  
  Read when using the visual-draft -> asset extraction -> editable PPT
  reconstruction workflow.

- [references/slide-plan-schema.md](references/slide-plan-schema.md)  
  Read when creating or repairing `slide_plan.json`.

## Scripts

- [scripts/build_ppt.py](scripts/build_ppt.py)  
  Lightweight PPTX builder for `slide_plan.json` when `python-pptx` is
  available.

- [scripts/validate_drafts.py](scripts/validate_drafts.py)  
  Validates that visual drafts are individual 16:9 slide images before asset
  extraction.

- [scripts/validate_ppt.py](scripts/validate_ppt.py)  
  Inspects a PPTX package for slide count, text objects, and image objects.

## Metadata

- [agents/openai.yaml](agents/openai.yaml)  
  UI-facing metadata for the skill name, summary, and default prompt.

## Recommended Read Order

For using the skill:

1. `SKILL.md`
2. `references/decision-gates.md` if the brief is underspecified
3. `references/visual-prompt-strategy.md` before image generation
4. `references/image-prompting.md`
5. `references/asset-reconstruction.md` for editable reconstruction
6. `references/slide-plan-schema.md` when building the plan

For maintaining the skill:

1. `AGENTS.md`
2. `SKILL.md`
3. `RULES.md`
4. relevant files under `references/`
5. relevant files under `scripts/`
