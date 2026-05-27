# Visual Prompt Strategy

Use this reference before generating slide images when the user gives a short
brief, when style quality matters, or when previous images look too plain.

## Trigger

Create a visual prompt strategy when any of these are true:

- the user gives only a topic, one sentence, or a rough product/profile request
- no clear style, audience, or usage context is provided
- multiple visual directions would fit the same source image
- the user complains that generated images look simple, generic, or template-like
- the deck depends on AI-generated visual drafts before asset reconstruction

Do not call the image model directly from a vague request such as "make a good
PPT". Ask or infer first, then design the image prompt plan.

## Short-Brief Questions

Ask only high-impact questions. Use 1-3 questions, with 2-3 options each and a
custom-answer path.

Recommended questions:

```text
Before I generate the PPT visual drafts, choose a direction:

1. Visual style: polished corporate profile (recommended), editorial portfolio,
   or energetic tech/product.
2. Density: clean and premium (recommended), richer and more decorative, or
   information-dense.
3. Tone: trustworthy/professional (recommended), youthful/confident, or bold
   keynote.
```

If the user says "you decide", choose the option that best matches the supplied
image or use case and continue.

## Strategy Output

Write a compact `visual_prompt_strategy.md` or equivalent section before image
generation. Include:

- `creative_direction`: a named art direction, not just generic keywords
- `audience_and_use`: who will see the deck and what impression it should make
- `source_image_read`: visual cues from uploaded product/person/reference images
- `palette`: 3-5 colors with roles, including background and accent colors
- `visual_language`: materials, lighting, depth, texture, geometry, motion cues
- `composition_system`: grid, focal object placement, recurring blank text zones
- `slide_rhythm`: how covers, section pages, feature pages, and closing pages
  differ while staying consistent
- `asset_strategy`: which parts should become PNG assets and which should become
  native PPT shapes
- `negative_constraints`: what the image model must avoid
- `per_slide_prompt_plan`: one prompt brief per slide

Keep this strategy practical. It should be specific enough that another agent
could generate the same style consistently, but short enough to edit quickly.

## Prompt Design Rules

- Start with the deck-level art direction, then add slide-specific composition.
- Describe the page as a presentation visual draft, not a poster or thumbnail.
- Always reserve named text zones such as "left 38 percent clean for editable
  title and bullets" or "top band left empty for title".
- Describe the focal object scale and position.
- Specify lighting, material, texture, and depth if the visual should feel
  premium.
- Specify what should remain abstract or blank so later PPT text stays readable.
- Include explicit "not a contact sheet, not a collage" constraints for every
  full-page draft prompt.
- Use a consistent style anchor phrase across all slides.

## Anti-Template Rules

Avoid prompts that only say:

- clean modern corporate
- high-end product style
- beautiful PPT
- minimalist business deck
- professional blue presentation

Replace them with concrete design language:

- "white studio portrait system with cobalt-blue geometric lower bands, soft
  shadowed glass panels, crisp executive ID-card rhythm"
- "mint-green product launch system with translucent acrylic platforms, soft
  botanical edge details, and generous left-side copy whitespace"
- "editorial portfolio system with cropped portrait scale, magazine-like white
  margins, restrained blue rule lines, and small modular information cards"

## Example Strategy Skeleton

```markdown
# Visual Prompt Strategy

## Creative Direction
Executive Identity System: a crisp white-and-cobalt profile deck inspired by the
uploaded headshot's blue lower-third geometry, formal suit styling, and clean
studio background.

## Palette
- white: main background
- cobalt blue: title/accent geometry
- pale blue: translucent layered shapes
- charcoal: body text and icon contrast

## Composition System
Use a 16:9 slide canvas. Keep the main portrait or product on one side and a
clean editable text zone on the other. Reuse diagonal blue bands, thin vertical
rules, rounded information panels, and subtle shadows. Keep text areas blank in
the generated images.

## Negative Constraints
No readable slide text, no fake logo, no watermark, no collage, no contact
sheet, no crowded dashboard, no distorted face/product, no tiny decorative
noise in text zones.

## Per-Slide Prompt Plan
1. Cover: large portrait crop on right, cobalt lower-band motif, left text zone.
2. Profile: portrait thumbnail plus three native-card zones, airy white field.
3. Experience: abstract product-management workflow diagram made of shapes.
4. Strengths: three modular cards with subtle icon placeholders.
5. Case Study: layered timeline and product roadmap motif.
6. Closing: confident portrait silhouette, diagonal blue accents, open CTA zone.
```

## When Images Still Look Weak

If the first drafts look bland:

1. Strengthen the `creative_direction` into a more specific design system.
2. Add source-image cues, not just generic style adjectives.
3. Add richer composition instructions per slide.
4. Add stronger negative constraints against templates, flat icons, fake text,
   and crowded decorative elements.
5. Regenerate one slide as a style test before spending time on all pages.
