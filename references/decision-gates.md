# Decision Gates

Use decision gates to ask the user when a choice is subjective, expensive to
redo, or affects factual accuracy. Do not ask about every small layout decision.

## Ask Format

Ask 1-3 short questions at a time. Provide 2-3 options, put the recommended
choice first, and allow the user to give a custom answer.

Pattern:

```text
Before I generate the visual drafts, please choose:

1. Visual direction: Corporate blue profile style (recommended), minimalist
   editorial, or more energetic tech style.
2. Deck length: 6 pages (recommended), 8 pages, or custom.
3. Editability level: high editability with native shapes (recommended), faster
   background-plus-text, or visual-only.
```

If the user already gave a clear answer, do not ask again.

## Must Ask

Ask before proceeding when any of these are unclear:

- `purpose`: presentation, sales, interview, class, event, proposal, portfolio
- `audience`: executive, client, student, internal team, public
- `language`: Chinese, English, bilingual
- `page_count`: if the user did not specify and the deck is more than a small
  quick draft
- `mode`: if they may care about object-level editing versus speed
- `visual_direction`: if multiple plausible styles fit the source image
- `source_facts`: if names, titles, metrics, prices, claims, or product specs
  are missing
- `asset_fidelity`: if using a provided product/person image and generated
  drafts may change the subject
- `continue_after_drafts`: if `reconstruct_editable` mode depends on visual
  draft approval
- `batch_continuation`: after each asset batch, ask whether to continue,
  revise, or stop if the user requested human control

## Usually Infer

Infer these unless the user asks to control them:

- exact file/folder names
- minor spacing and alignment
- exact native shape coordinates
- text shortening for readability
- whether simple geometry should be native PPT shapes
- whether duplicated decorative assets should be deduplicated

## Recommended Defaults

Use these defaults when the user wants speed or says "you decide":

- `mode`: `reconstruct_editable`
- `page_count`: 6 for product/profile decks, 8 for fuller proposals
- `ratio`: 16:9
- `language`: match the user's prompt language
- `visual_direction`: derive from source image or reference style
- `draft_generation`: one separate 16:9 image per slide
- `asset_batch_size`: 1 global batch, 1 PNG batch, then slide-specific batches
- `final_review`: show or report draft validation before PPT assembly

## Approval Points

Use these checkpoints for high-fidelity visual decks:

1. Brief approval: confirm topic, audience, page count, mode, and style.
2. Visual draft approval: show or describe the 16:9 drafts and ask whether to
   proceed, revise, or choose a different style.
3. Asset batch approval: after a batch, ask whether to continue, revise the
   extraction granularity, or stop if enough assets exist.
4. Final QA: report editability, draft ratio validation, and PPTX validation.

## Example Questions

For an uploaded product image:

```text
I can take this in three directions:
1. Premium product launch deck (recommended): polished, high editability.
2. E-commerce feature deck: denser selling points and more cards.
3. Minimal catalog deck: cleaner, fewer assets, easier to edit.

Which direction should I use?
```

For a profile photo:

```text
Before generating drafts, should the deck feel:
1. Corporate profile blue/white (recommended, matches the photo).
2. Portfolio/editorial with more personality.
3. Tech/startup with stronger motion and diagrams.
```

For asset extraction:

```text
Batch 1 is ready: global shapes and master style. Continue with:
1. Extract only essential PNGs (recommended): portrait/product/icons.
2. Extract more decorative pieces: richer but harder to edit.
3. Pause so you can review the draft direction.
```
