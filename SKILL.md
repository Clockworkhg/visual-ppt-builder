---
name: visual-ppt-builder
description: Create visually polished, editable PowerPoint PPTX decks from a topic, brief, product image, reference style, copy, or rough outline. Use when the user asks to make a PPT, slide deck, presentation, product showcase, proposal deck, course deck, activity plan, image-led deck, high-visual editable PPTX, or when Codex should generate slide backgrounds/assets, assemble them into a PPTX with editable text layers, and validate the output.
---

# Visual PPT Builder

## Goal

Produce a finished PPTX deck that looks visual and polished while keeping
meaningful text, product images, decorative assets, and simple layout objects
separately editable in PowerPoint or WPS. Treat generated page visuals as a
directional draft, then reconstruct the deck from native PPT shapes, independent
PNG assets, and editable text boxes.

Default to `reconstruct_editable` mode for product/image-led decks. Use
`background_plus_text` only for quick drafts. Use `visual_only` only when the
user asks for poster-like flat slides, speed over editability, or image-only
pages.

## Resource Map

- Read [references/slide-plan-schema.md](references/slide-plan-schema.md) when
  creating or repairing `slide_plan.json`.
- Read [references/image-prompting.md](references/image-prompting.md) before
  generating slide visuals.
- Read [references/asset-reconstruction.md](references/asset-reconstruction.md)
  when using the visual-draft -> asset extraction -> PPT reconstruction flow.
- Use [scripts/build_ppt.py](scripts/build_ppt.py) when a lightweight local
  PPTX builder is enough and `python-pptx` is available.
- Use [scripts/validate_drafts.py](scripts/validate_drafts.py) before asset
  extraction to verify every visual draft is an individual 16:9 slide image.
- Use [scripts/validate_ppt.py](scripts/validate_ppt.py) to inspect the final
  PPTX package for slide count, text objects, and image objects.

If the installed `Presentations` skill/plugin is available and the deck needs
high polish, rendered previews, template editing, or stronger PPTX export,
prefer that workflow for production assembly. This skill still controls the
visual-planning, image-generation, editability, and validation rules.

## Workflow

1. Classify the deck mode: `reconstruct_editable`, `background_plus_text`, or
   `visual_only`.
2. Build a brief from the user request. Infer missing non-critical details.
   Ask only when purpose, language, page count, source facts, or required assets
   are impossible to infer safely.
3. Create `slide_plan.json` before generating visuals or slides. Include deck
   metadata, a visual system, and one object per slide.
4. Lock a visual system: palette, font direction, layout rhythm, background
   treatment, image style, and whitespace rules. Reuse this in every image
   prompt and slide layout.
5. In `reconstruct_editable` mode, generate full-page visual drafts first.
   Generate one separate image per slide, not a contact sheet or collage. Save
   them as `drafts/slide_01.png`, `drafts/slide_02.png`, and so on. These are
   references only, not final slide backgrounds.
6. Validate visual draft dimensions before extraction. Each draft must be 16:9
   within a small tolerance. If drafts came from a generated contact sheet,
   reject them and regenerate individual slide drafts.
7. Extract or regenerate the useful visual pieces as separate transparent PNGs:
   product cutouts, decorative leaves, platforms, icon-like assets, soft
   shadows, and reusable image fragments. Skip plain rectangles, circles,
   cards, dividers, and lines because those should be rebuilt as native PPT
   shapes.
8. Add every reusable image asset to the top-level `assets` list. Add every
   per-slide placement to `slides[].image_assets`. Add circles, cards, chips,
   color blocks, dividers, and panels to `slides[].native_shapes`.
9. Assemble the PPTX. Insert native shapes first, then independent image assets,
   then editable text boxes. Keep all title, body, label, table, and parameter
   text editable.
10. Validate the deck. Prefer rendered preview QA when available. Always inspect
   the PPTX package for slide count and text objects.
11. Deliver the final PPTX plus useful support artifacts.

## Mode Router

- `reconstruct_editable`: use for product decks, uploaded product photos,
  "use image generation", "like the visual draft", "extract assets", "editable
  PPT", or any request where the user expects visual richness and object-level
  editing. This is the default.
- `background_plus_text`: use for quick internal drafts where the user mainly
  needs editable text and accepts a mostly flat visual background.
- `visual_only`: use only when the user explicitly accepts image-only slides.

## Default Deck Structure

When the user provides only a topic, create a reasonable 5-7 slide structure.
For product decks, default to:

1. Cover
2. Product promise or core value
3. Key features
4. Usage scenarios
5. Specs or proof points
6. Closing / call to action

For lesson, activity, proposal, or report decks, adapt the same rhythm:
context, thesis, sections/proof, application, summary.

## Hard Rules

- In `editable` mode, every meaningful visible word must exist as a PPT text
  object. Background images may contain texture, signage-like microtext, or
  abstract marks, but not the slide's readable copy.
- In `reconstruct_editable` mode, do not use a full-page generated draft as the
  final background. Use it only as a reference. Rebuild the slide from native
  PPT shapes, independent PNG assets, and editable text.
- Do not call a reconstruction "faithful" unless a real full-page visual draft
  exists before reconstruction and the final PPT is checked against it. If the
  assets were created only to test the pipeline, label the result as a
  pipeline/object-structure demo, not a visual-quality demo.
- Do not use a generated multi-slide contact sheet as the source for per-slide
  drafts. Contact sheets are for review only after individual 16:9 slide drafts
  exist. Slicing a generated contact sheet usually produces wrong page ratios.
- Do not make each editable slide a single flattened screenshot or one
  screenshot plus text if the user asked for material object editing.
- Product images and decorative assets should be separate movable PPT image
  objects whenever practical.
- Keep a consistent visual system across the whole deck.
- Leave intentional whitespace for text. Image prompts should avoid fully
  packed compositions.
- Prefer fewer, larger visual objects over many small decorative fragments.
  Object-level editability is not a license to clutter the page.
- Prefer native PPT shapes for simple chips, dividers, badges, cards, and
  diagrams when that improves editability.
- Keep copy concise. If user copy is too long, shorten it for slide readability
  and preserve the full source in notes or the report.
- Do not invent factual claims, metrics, prices, citations, logos, or product
  capabilities. Ask for missing facts or mark them as placeholders.
- Do not create lookalike logos or brand marks. Use user-provided or verified
  assets, or omit the mark.

## Artifacts

Create a task output folder, for example:

```text
outputs/<task-slug>/
  final_deck.pptx
  slide_plan.json
  asset_manifest.json
  build_report.md
  drafts/
  assets/
  images/
  previews/
```

Keep generated prompt drafts, scratch layouts, and intermediate files inside
the task output folder. Return the final PPTX path and mention the validation
result in the final response.

## Script Commands

Build with the local helper when appropriate:

```bash
python scripts/build_ppt.py --plan outputs/demo/slide_plan.json --images outputs/demo/images --out outputs/demo/final_deck.pptx --report outputs/demo/build_report.md
```

Validate an existing PPTX:

```bash
python scripts/validate_ppt.py outputs/demo/final_deck.pptx --expect-slides 6 --report outputs/demo/validation_report.md
```

Validate visual drafts before extraction:

```bash
python scripts/validate_drafts.py outputs/demo/drafts --expect-count 6 --report outputs/demo/draft_validation_report.md
```

## Failure Recovery

- If the result is too image-heavy, rebuild with more native shapes and text
  boxes.
- If generated visual drafts are the wrong ratio, stop before extraction and
  regenerate one image per slide. Do not slice a contact sheet to recover pages.
- If the result is only "background plus text" but the user expected the video
  workflow, switch to `reconstruct_editable`: create an asset manifest, split
  useful visuals into independent PNGs, and rebuild shapes natively.
- If visuals are busy, regenerate backgrounds with larger blank text zones,
  fewer objects, and simpler depth.
- If the reconstructed PPT looks messier than the visual draft, reduce the
  number of extracted decorative assets, rebuild plain geometry as native
  shapes, and prioritize thumbnail-level similarity over asset count.
- If text overflows, shorten the copy first; then adjust font size and box
  dimensions.
- If page visuals drift in style, rewrite the visual system and regenerate only
  the inconsistent slides.
- If `python-pptx` is unavailable, use the `Presentations` skill/plugin when
  available, or create a simpler native-shape deck and explain the limitation.
