# Visual PPT Builder

Visual PPT Builder is a Codex skill for creating visually polished, editable
PowerPoint decks from a short brief, product image, profile photo, reference
style, outline, or copy.

The skill is designed for the workflow where AI-generated visuals provide the
look, but the final PPTX keeps meaningful text, simple geometry, image assets,
and layout objects separately editable in PowerPoint or WPS.

## What It Does

- asks for high-impact style choices when the user gives a short prompt
- designs a visual prompt strategy before image generation
- generates one separate 16:9 visual draft per slide
- validates draft image ratios before asset extraction
- rebuilds slides with native PPT shapes, independent PNG assets, and editable
  text boxes
- validates the final PPTX for slide count, text objects, and image objects

## Best For

- product introduction decks
- profile or resume decks
- visual proposal decks
- course or activity decks
- image-led presentation drafts that still need editable text

It is not meant for highly animated decks, very long research reports, or
spreadsheet-driven financial decks.

## Core Workflow

1. Build a brief from the user's request.
2. Ask for missing style, audience, page count, fidelity, or source facts when
   those choices matter.
3. Create a `slide_plan.json`.
4. Create `visual_prompt_strategy.md` and `image_prompts.json`.
5. Generate one individual 16:9 visual draft per slide.
6. Validate draft ratios with `scripts/validate_drafts.py`.
7. Extract useful image assets and rebuild simple geometry as native shapes.
8. Assemble the PPTX with editable text layers.
9. Validate the PPTX and produce a build report.

## Expected Output

```text
outputs/<task-slug>/
  final_deck.pptx
  slide_plan.json
  visual_prompt_strategy.md
  image_prompts.json
  asset_manifest.json
  build_report.md
  drafts/
  assets/
  images/
  previews/
```

## Usage Examples

```text
Use $visual-ppt-builder to create a 6-page editable product deck from this
product photo. Keep the style fresh, premium, white and mint green.
```

```text
Use $visual-ppt-builder to make a profile presentation from this headshot.
Ask me for style options first, then generate visual drafts and rebuild the
final PPTX with editable text.
```

```text
Use $visual-ppt-builder for a 6-page community anti-fraud activity proposal.
You decide the page structure, but ask me before choosing the visual direction.
```

## Validation

Validate the skill folder:

```bash
python C:/Users/hersh/.codex/skills/.system/skill-creator/scripts/quick_validate.py ./visual-ppt-builder
```

Validate generated drafts:

```bash
python scripts/validate_drafts.py outputs/demo/drafts --expect-count 6 --report outputs/demo/draft_validation_report.md
```

Validate a generated PPTX:

```bash
python scripts/validate_ppt.py outputs/demo/final_deck.pptx --expect-slides 6 --report outputs/demo/validation_report.md
```

## Install

Copy this folder to the Codex skills directory:

```powershell
Copy-Item -Path .\visual-ppt-builder -Destination "$env:USERPROFILE\.codex\skills\visual-ppt-builder" -Recurse -Force
```

Restart or refresh Codex so the skill metadata is discovered.

## File Guide

See [INDEX.md](INDEX.md) for the full Markdown index and maintenance map.
Read [RULES.md](RULES.md) for the operational rules that should not drift.
Read [AGENTS.md](AGENTS.md) before changing the skill implementation.
