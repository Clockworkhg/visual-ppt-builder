# Operational Rules

These rules protect the skill's core promise: AI-rich visuals with editable PPTX
structure.

## User Input

- Ask only when a choice materially changes style, scope, source accuracy,
  fidelity, cost, time, or editability.
- When the user gives a short prompt, ask 1-3 high-impact questions before
  image generation.
- Offer 2-3 options with a recommended default and allow a custom answer.
- If the user says "you decide", choose a sensible direction and continue.

## Prompt Strategy

- Do not send vague one-line requests directly to the image model.
- Create `visual_prompt_strategy.md` before high-visual image generation.
- Store exact per-slide prompts in `image_prompts.json`.
- Prompts must include a specific art direction, composition system, reserved
  text zones, visual motifs, and negative constraints.
- Avoid generic prompts such as "beautiful modern PPT" or "clean corporate
  template".

## Visual Drafts

- Generate one separate 16:9 image per slide.
- Do not generate a multi-slide contact sheet as the source for draft pages.
- Use contact sheets only as review artifacts assembled after individual drafts
  already exist.
- Validate draft dimensions before asset extraction.
- If draft ratios are wrong, stop and regenerate individual slide drafts.

## Editability

- In editable modes, every meaningful visible word must be a PPT text object.
- Do not flatten the final editable deck into full-slide screenshots.
- Use generated full-page visual drafts as references, not as final backgrounds
  in `reconstruct_editable` mode.
- Rebuild simple cards, circles, lines, dividers, chips, and diagrams as native
  PPT shapes whenever practical.
- Insert product images, portraits, props, and complex decorations as separate
  movable image objects.

## Asset Reconstruction

- Split only useful visual elements into transparent PNG assets.
- Deduplicate repeated decorations.
- Do not split plain geometry that should be native PPT shapes.
- Prefer fewer, stronger assets over many tiny decorative fragments.
- Prioritize thumbnail-level faithfulness and clean editability over maximal
  asset count.

## Facts And Claims

- Do not invent names, titles, metrics, prices, specs, citations, logos, or
  product capabilities.
- Ask for missing source facts or mark them as placeholders.
- Do not create lookalike logos or brand marks.

## Output

- Produce `final_deck.pptx`, `slide_plan.json`, `visual_prompt_strategy.md`,
  `image_prompts.json`, and `build_report.md` when image generation is part of
  the workflow.
- Include `asset_manifest.json` when reconstructing from visual drafts.
- Keep drafts, assets, previews, and scratch files inside the task output
  folder.

## Validation

- Run `quick_validate.py` after changing the skill.
- Run `validate_drafts.py` before extracting assets.
- Run `validate_ppt.py` after building the PPTX.
- Report validation results in the final response.

## Recovery

- If visuals are too plain, rewrite the visual prompt strategy before
  regenerating images.
- If visuals are too busy, reserve larger blank text zones and reduce props.
- If the reconstructed PPT is messy, rebuild more elements as native shapes and
  reduce decorative fragments.
- If text overflows, shorten copy before shrinking fonts.
