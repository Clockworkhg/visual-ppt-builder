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

## Short Prompt Gate

When the user gives a short or vague request such as "make a PPT", "make it
look good", "try this product photo", or "do a 6-page deck", ask for the
highest-impact visual choices before generating images. The goal is to collect
enough information to write a strong visual prompt strategy, not to interrogate
the user.

Ask a compact set such as:

```text
Before I generate visual drafts, choose:

1. Style: premium minimal (recommended), richer commercial, or bold keynote.
2. Audience: client/executive (recommended), internal team, or public/social.
3. Fidelity: high visual polish with draft approval (recommended), faster first
   pass, or visual-only.
```

If the uploaded image already strongly suggests a style, make that the
recommended option and explain it in a few words.

## Must Ask

Ask before proceeding when any of these are unclear:

- `purpose`: presentation, sales, interview, class, event, proposal, portfolio
- `audience`: executive, client, student, internal team, public
- `language`: Chinese, English, bilingual
- `page_count`: if the user did not specify and the deck is more than a small
  quick draft
- `mode`: if they may care about object-level editing versus speed
- `visual_direction`: if multiple plausible styles fit the source image
- `prompt_strategy`: if the user's request is too short to produce strong image
  prompts without choosing style, density, tone, or audience
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
- `prompt_strategy`: create one before image generation whenever the brief is
  short or visual quality is important
- `draft_generation`: one separate 16:9 image per slide
- `asset_batch_size`: 1 global batch, 1 PNG batch, then slide-specific batches
- `final_review`: show or report draft validation before PPT assembly

## Approval Points

Use these checkpoints for high-fidelity visual decks:

1. Brief approval: confirm topic, audience, page count, mode, and style.
2. Prompt strategy approval: for high-visual decks, summarize the planned art
   direction and ask whether to proceed, revise, or use a different style.
3. Visual draft approval: show or describe the 16:9 drafts and ask whether to
   proceed, revise, or choose a different style.
4. Asset batch approval: after a batch, ask whether to continue, revise the
   extraction granularity, or stop if enough assets exist.
5. Final QA: report editability, draft ratio validation, and PPTX validation.

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

For a very short prompt:

```text
I can design the image prompts first so the generated PPT visuals are less
generic. Choose the direction:
1. Premium and restrained (recommended): clean, polished, easy to edit.
2. Rich commercial: more product-ad styling and decorative assets.
3. Bold keynote: stronger contrast, bigger visual moments.
```

For asset extraction:

```text
Batch 1 is ready: global shapes and master style. Continue with:
1. Extract only essential PNGs (recommended): portrait/product/icons.
2. Extract more decorative pieces: richer but harder to edit.
3. Pause so you can review the draft direction.
```
