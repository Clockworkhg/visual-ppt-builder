# Image Prompting Guide

Generate slide visuals as draft references or support assets, not as final flat
slides unless the user explicitly chooses `visual_only`. The PPT layer should
own the text and simple geometry.

## Prompt Formula

Use this structure for each slide:

```text
Create one single 16:9 horizontal presentation slide visual draft for [slide type].
Topic/product: [subject].
Visual system: [palette, style, lighting, texture].
Composition: [where the focal object goes, where the text zone stays blank].
Content cues: [objects, environment, mood, use case].
Constraints: not a collage, not a contact sheet, no long readable text, no fake
logos, no watermark, no busy details inside the reserved text area.
```

## Reconstruct Editable Mode Rules

- First generate full-page visual drafts to establish the look. Generate one
  separate 16:9 image per slide.
- Do not ask for a 2x3 or 3x2 generated contact sheet as the source image.
  Contact sheets are review artifacts assembled after individual drafts exist.
- Then generate or extract independent transparent PNG assets for product
  cutouts, leaves, props, shadows, platforms, and complex motifs.
- Rebuild simple circles, rounded rectangles, cards, chips, and dividers as
  native PPT shapes instead of PNGs.
- Use the full-page draft only as a visual reference, not as the final
  background.

## Background Plus Text Rules

- Reserve a clean title/body zone.
- Keep the background low contrast behind future text.
- Put products, people, diagrams, or decorative elements away from text zones.
- Avoid poster typography and large embedded slogans.
- Use consistent lighting, camera distance, palette, and material language.

## Visual Only Mode Rules

Only use this mode when the user asks for flat poster-like slides. In that case,
the image may include more composition and title-like text, but still avoid
tiny unreadable text and fake marks.

## Product Image Mode

When the user provides a product image:

- Treat the user image as the source of truth for product shape and color.
- Prefer placing the original product image in PPT as an editable/movable image
  object when possible.
- Use generated backgrounds to frame the product, not to hallucinate a different
  product.
- If the generated visual changes important product details, regenerate or use
  the original product image over a generated background.

## Reference Style Mode

When the user provides a reference style:

- Extract palette, spacing, density, mood, light, and composition rhythm.
- Transfer the style; do not copy protected layouts, logos, or text.
- Keep the new deck's subject and message clear.

## Bad Prompt Patterns

Avoid:

- "Create a complete slide with all text..."
- "Add the title and bullet points..."
- "Make a detailed infographic with many labels..."
- "Use the Apple/Nike/Tesla logo" unless the user supplied or verified it.

Use:

- "Leave the left third clean for editable title and bullets."
- "No readable text except abstract signage-like micro marks."
- "Low-detail background behind the text area."

## Asset Extraction Prompt

Use prompts like:

```text
Extract the reusable visual assets from the provided slide draft as separate
transparent PNG assets. Do not include any text. Include the product cutout,
decorative leaves, platform/base, soft shadow, and icon-like motifs. Do not
extract plain circles, rounded rectangles, lines, or text panels because those
will be rebuilt as native PPT shapes. Deduplicate repeated assets.
```
