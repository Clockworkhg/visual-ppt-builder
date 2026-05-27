# Asset Reconstruction Workflow

Use this reference when the user expects the workflow:

1. Generate full-page visual drafts.
2. Extract or regenerate separate visual assets.
3. Rebuild a PPTX from independent assets, native shapes, and editable text.

## Stage 1: Visual Drafts

Generate one 16:9 visual draft per slide. These drafts establish composition,
palette, product placement, lighting, and slide rhythm. They are not final PPTX
slides in `reconstruct_editable` mode.

Never ask the image model for a multi-slide contact sheet as the canonical
source. A generated contact sheet often has the correct overall 16:9 ratio while
each thumbnail inside it is not 16:9. Slicing that sheet corrupts the geometry
for extraction and reconstruction.

Do not skip this stage for a visual-quality demo. If no real draft exists and
the assets are hand-made or code-generated placeholders, call the output a
pipeline/object-structure test only.

Draft prompts may look like complete slides, but prefer minimal or no readable
text so the later PPT text layer stays authoritative.

Save drafts as:

```text
drafts/slide_01.png
drafts/slide_02.png
...
```

Then run `scripts/validate_drafts.py` and proceed only if every draft is 16:9.
If a contact sheet is useful for review, assemble it yourself from the validated
individual drafts.

## Stage 2: Asset Extraction

Create an asset list from the drafts:

- product cutout
- hero product shadow
- decorative leaves or props
- platform/base
- icon-like visual motifs
- photo fragments that are hard to rebuild as shapes
- reusable texture or highlight fragments

Do not extract:

- slide title or paragraph text
- plain circles
- plain rectangles
- rounded cards
- lines and dividers
- simple color fields

Those should be recreated as native PPT objects.

Prefer transparent PNGs for extracted image assets. Deduplicate repeated assets
and reuse them across slides.

Keep the asset list small. A page with too many tiny extracted fragments usually
looks worse than the draft and becomes harder to edit. Extract only assets whose
visual complexity is hard to recreate with native shapes.

## Stage 3: Asset Manifest

Record assets at the top level of `slide_plan.json` or in
`asset_manifest.json`:

```json
{
  "assets": [
    {
      "id": "product_bottle",
      "path": "assets/product_bottle.png",
      "role": "product_cutout",
      "notes": "Main product cutout used on cover and closing slides"
    },
    {
      "id": "leaf_sprig",
      "path": "assets/leaf_sprig.png",
      "role": "decorative_png"
    }
  ]
}
```

## Stage 4: PPT Reconstruction

For each slide:

- use `native_shapes` for circles, cards, panels, dividers, chips, and simple
  diagrams
- use `image_assets` for product cutouts, leaves, shadows, platforms, icons, and
  complex visual fragments
- use `text_blocks` for every readable word

Object order matters. Insert broad background shapes first, then decorative
shapes, then images, then text.

Set image fit deliberately:

- `contain` for product cutouts, icons, and most transparent PNG assets
- `cover` for portrait cards or circular avatars that must fill a frame without
  distortion
- `stretch` only for abstract shadows or textures where stretching is acceptable

## QA Checklist

A reconstructed deck passes only when:

- text is selectable and editable
- product cutouts can be selected and moved
- decorative PNGs can be selected independently
- image assets preserve their intended aspect ratio; portraits must not be
  stretched to fit a frame
- simple circles/cards/blocks are native PPT shapes
- no slide is merely one full-page screenshot
- every source draft is an individual 16:9 slide image, not a slice from a
  generated collage
- the slide count and visual rhythm match the draft set
- the deck still looks close to the visual drafts at thumbnail size
- the reconstructed page is not busier than the draft
- every slide has a clear focal hierarchy: one hero object, one text zone, and
  no more decorative pieces than the composition needs
