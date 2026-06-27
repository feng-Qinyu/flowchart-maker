---
name: flowchart-maker
description: Use when the user wants to create, revise, beautify, validate, or export a flowchart, process diagram, workflow diagram, system flow, Mermaid diagram, HTML flowchart, SVG-style diagram, PPT-ready diagram, or whiteboard-style diagram. This skill is for workflows where the diagram may need repeated AI-driven edits and layout checks.
---

# Flowchart Maker

## Purpose

Create editable flowcharts with a two-layer workflow:

- Mermaid is the logic source.
- HTML/CSS is the presentation layer for polished layout, interaction, export, and visual QA.

Use this skill when the user wants a flowchart that can be corrected, reflowed, beautified, compared across styles, or exported.

## Default Workflow

1. Clarify only missing essentials:
   - purpose: knowledge base, formal report, interactive demo, whiteboard discussion, or product UI
   - output format: Mermaid, HTML, PNG, SVG, PPT-ready image, or all relevant files
   - required style constraints, if any
2. Create or update the Mermaid source first.
3. If the logic is ambiguous, ask the user to verify the Mermaid-level flow before visual polishing.
4. Convert the accepted flow into an HTML presentation version when the user needs better layout or visual quality.
5. For `sketch` + `editable` HTML flowcharts, start from `assets/editable-flowchart-template.html` unless the user asks for a different implementation. Replace the nodes, initial positions, labels, and edge list while preserving the template's editing, dragging, shape-aware ports, solid arrowheads, save/reset/export PNG/export JSON controls, and internal workspace whitespace.
6. For `mono` + `editable` HTML flowcharts, start from `assets/mono-editable-flowchart-template.html`. Preserve editability, dragging, auto-rerendered arrows, save/reset/export JSON/export PNG controls, plain browser background, black/gray linework, and no grid background.
7. For `glass` + `editable` HTML flowcharts, start from `assets/glass-editable-flowchart-template.html`. Preserve editability, dragging, auto-rerendered arrows, save/reset/export JSON/export PNG controls, dark atmospheric background, translucent panels, subtle glow, and readable light text.
8. For `blueprint`, `neon`, `editorial`, `pastel`, `brutal`, or `dark` + `editable` HTML flowcharts, use the stable editable interaction skeleton from the existing templates, then apply the requested visual theme. Preserve dragging, editable text, shape-aware ports, auto-rerendered arrows, save/reset/export JSON/export PNG controls, centered initial layout, and real workspace whitespace.
9. When the user asks for multiple themes, create one standalone HTML file per theme. Do not put all themes into one combined gallery page unless the user explicitly asks for a comparison page.
10. Before completion, check layout quality:
   - no overlapping nodes
   - no visible text overflow
   - arrows do not cross important text
   - grouped containers have enough padding
   - long labels wrap cleanly
   - narrow screens either remain readable or use horizontal scrolling
   - the main loop or feedback path is visible
11. If layout fails, adjust positions, dimensions, wrapping, or grouping and check again.
12. Return local paths for created files and state what was verified.

## User and AI Division

User decides:

- whether the business logic is correct
- which nodes or relationships are wrong
- intended use and preferred visual style

AI handles:

- Mermaid logic edits
- HTML/CSS layout and styling
- node sizing, spacing, grouping, arrows, and wrapping
- screenshot or browser checks when available
- export steps when requested

## Style Selection

Choose one visual style and one delivery mode unless the user asks for comparison.

Visual styles:

- `sketch`: default. Hand-drawn comic whiteboard style for concept explanation, knowledge cards, teaching, and personal knowledge-base diagrams.
- `mono`: black-and-white wireframe style for technical docs, README diagrams, engineering explanations, and draw.io-like neutral diagrams.
- `glass`: translucent tech style for product architecture, AI platforms, control consoles, MCP, automation, and polished technical demos.
- `formal`: professional architecture/report style for leadership reports, enterprise solution pages, PPT-ready architecture diagrams, and formal delivery documents.
- `blueprint`: clean engineering blueprint style for system architecture, data flow, platform modules, and technical design notes.
- `neon`: cyber neon style for AI, MCP, automation, agent workflows, and technical communication.
- `editorial`: magazine editorial style for methodology diagrams, opinion diagrams, report openings, and polished explanatory graphics.
- `pastel`: soft colorful style for product explanations, user flows, lightweight training, and approachable internal materials.
- `brutal`: high-contrast brutalist style for strong conclusions, conflict/comparison diagrams, and social/shareable technical graphics.
- `dark`: restrained dark professional style for formal technical explanations, architecture diagrams, and presentation-ready reports.

Delivery modes:

- `mermaid`: best for knowledge bases, docs, version control, and fast logic iteration.
- `editable`: best when the user wants to manually drag nodes, correct arrows, or edit labels after AI generation.
- `static`: best for final HTML/SVG/PNG export after the layout is accepted.
- `interactive`: best for demos, training, clickable explanations, and product prototypes.

Recommended default:

- Use `sketch` as the default visual style.
- Start with `mermaid` only to confirm logic when the flow is unclear.
- Move to `editable` when the user may correct layout, arrows, or wording manually.
- Move to `static` after the editable version is accepted.
- Use `mono` when the user asks for black-and-white, wireframe, draw.io-like, engineering-document, README, or minimal technical style.
- Use `glass` when the user asks for translucent, glassmorphism, tech, AI platform, console, dark polished, product architecture, or modern interface style.
- Use `formal` only when the user explicitly asks for formal report, architecture, consulting, enterprise, leadership, or PPT style.
- Use `blueprint` when the user asks for engineering blueprint, system architecture, data flow, module relationships, or technical design style.
- Use `neon` when the user asks for cyber, neon, AI, MCP, automation, futuristic, or technical communication style.
- Use `editorial` when the user asks for magazine, report opening, methodology, viewpoint, or polished explanatory graphic style.
- Use `pastel` when the user asks for soft, friendly, light training, product walkthrough, or low-pressure explanation style.
- Use `brutal` when the user asks for bold, high-contrast, poster-like, strong conclusion, or social-share style.
- Use `dark` when the user asks for dark professional, formal technical, stable report, architecture, or presentation style.

## Visual Style Rules

### `sketch`

Use this style by default.

Purpose:

- Explain concepts in a friendly, easy-to-read way.
- Make the diagram feel like a hand-drawn whiteboard or comic-style explanation.
- Lower the reading burden for knowledge cards, teaching materials, and exploratory thinking.

Visual requirements:

- Hand-drawn feeling: slightly casual lines, light irregularity, soft shadows, playful but controlled colors.
- Use colorful category accents such as purple, blue, green, amber, orange, and teal.
- Prefer comic/handwritten-feeling fonts when available, such as Comic Sans MS, Marker Felt, Bradley Hand, or system fallbacks.
- Nodes should have a single clear border. Do not add inner pale duplicate borders by default.
- Do not add a big outer frame, hero title, explanatory paragraph, or separate paper/canvas background unless requested.
- Arrows should be modest, readable, and preferably small solid arrowheads for editable diagrams.
- Keep the chart itself centered, with real workspace whitespace around it when editable.
- The result should feel like "a clear concept diagram drawn on a whiteboard", not a formal consulting slide.

Avoid in `sketch`:

- Dense enterprise boxes.
- Heavy section frames.
- Big black title bars.
- Number badges everywhere.
- Formal architecture-page composition.

### `mono`

Use this style when the user asks for black-and-white, wireframe, draw.io-like, README, engineering document, or minimal technical style.

Purpose:

- Present process logic with minimal visual decoration.
- Make the diagram feel like a clean engineering diagram rather than a hand-drawn whiteboard or formal presentation slide.
- Keep the result easy to inspect, edit, export, and paste into technical docs.

Visual requirements:

- Use a plain browser/page background. Do not add a grid background by default.
- Use black, white, and neutral gray only unless the user explicitly asks for accent colors.
- Use rectangular nodes with a single black border, small radius, and no decorative shadows.
- Use simple black arrows with small solid arrowheads.
- Use dashed gray arrows only for feedback, async, or secondary flows.
- Keep typography utilitarian and readable; prefer system sans-serif or neutral document fonts.
- Keep node content concise and avoid single-character Chinese wrapping.
- Keep editable diagrams fully functional: draggable nodes, editable text, auto-rerendered arrows, save/reset/export JSON/export PNG controls.
- The chart should initialize centered with real canvas whitespace around it for manual adjustment.

Avoid in `mono`:

- Grid backgrounds unless explicitly requested.
- Hand-drawn fonts, playful icons, colorful category borders, or comic styling.
- Heavy title bars, large decorative labels, gradients, glass effects, or presentation-like background treatments.
- Static-only HTML when the user expects the flowchart-maker editable workflow.

### `glass`

Use this style when the user asks for translucent, glassmorphism, tech, AI platform, console, product architecture, modern interface, or dark polished style.

Purpose:

- Present technical flows with a polished product-interface feeling.
- Make the diagram feel suitable for AI platforms, runtime architecture, MCP, automation, and product demos.
- Preserve the editable workflow while giving the diagram a more atmospheric visual language than `mono`.

Visual requirements:

- Use a dark atmospheric background with restrained gradients or soft light fields.
- Use translucent panels with thin light borders, subtle shadows, and readable light text.
- Use light cyan/blue-white arrows for primary flows.
- Use muted mint/cyan dashed arrows for feedback, async, or secondary flows.
- Keep glow effects subtle enough that arrows and text remain clear.
- Keep nodes readable and avoid overly low contrast text.
- Keep editable diagrams fully functional: draggable nodes, editable text, auto-rerendered arrows, save/reset/export JSON/export PNG controls.
- The chart should initialize centered with real canvas whitespace around it for manual adjustment.

Avoid in `glass`:

- Bright neon cyberpunk overload; use `neon` if that style exists and is requested.
- Heavy blur that makes text or borders hard to read.
- Decorative backgrounds that compete with arrows or node text.
- Static-only HTML when the user expects the flowchart-maker editable workflow.

### `formal`

Use this style only when requested or clearly appropriate for official materials.

Purpose:

- Present a complete architecture, process, or platform relationship in a professional report style.
- Make the diagram feel structured, credible, and PPT-ready.

Visual requirements:

- Use precise grids, clean rectangular cards, and consistent alignment.
- Allow section frames, system boundary boxes, title bars, labels, and role markers when they improve structure.
- Use a restrained palette and clearer hierarchy; colors classify domains, not decoration.
- Arrows should emphasize control flow, data flow, feedback flow, or dependency flow.
- Higher information density is acceptable if text remains readable and no elements overlap.
- Suitable for leadership reports, solution decks, architecture explanations, and enterprise delivery materials.

Avoid in `formal`:

- Excessive hand-drawn irregularity.
- Cartoon-like looseness.
- Casual visual jokes or overly playful icons.

### `blueprint`

Use this style for engineering-blueprint diagrams.

Purpose:

- Explain system architecture, data flow, platform modules, and technical design structures.
- Make the diagram feel like a clean technical drawing rather than a decorative poster.

Visual requirements:

- Use a deep navy or blueprint-blue background with cyan or blue-white lines.
- Use crisp rectangular nodes, thin borders, compact shadows, and technical typography.
- Use cyan arrows with small solid arrowheads; dashed cyan lines may represent feedback or secondary flows.
- Keep the background clean by default. Do not add a grid background unless the user explicitly requests it.
- If a grid is requested, use one subtle full-page grid only. Do not add local grid patches, inner duplicate node borders, or extra grid-like boxes behind individual nodes.
- Keep editable diagrams fully functional: draggable nodes, editable text, auto-rerendered arrows, save/reset/export JSON/export PNG controls.

Avoid in `blueprint`:

- Heavy decorative grids that compete with the diagram.
- Extra inner borders that look like unintended grid lines.
- Bright neon glow overload; use `neon` for that.

### `neon`

Use this style for cyber, AI, MCP, and automation communication diagrams.

Purpose:

- Present technical flows with a high-energy cyber interface feeling.
- Make AI, agent, MCP, automation, and futuristic workflows more visually memorable.

Visual requirements:

- Use a dark background with restrained cyan, magenta, violet, or green accents.
- Use glowing but readable lines and borders; glow must not blur arrow endpoints or text.
- Use solid neon arrows for primary flow and dashed neon lines for feedback or secondary flow.
- Keep text contrast high and avoid low-contrast gray text on dark backgrounds.
- Keep editable diagrams fully functional: draggable nodes, editable text, auto-rerendered arrows, save/reset/export JSON/export PNG controls.

Avoid in `neon`:

- Excessive glow that makes arrows fuzzy.
- Dense scanlines or visual effects that reduce readability.
- Decorative elements that occupy unused workspace without carrying meaning.

### `editorial`

Use this style for magazine-like explanatory diagrams.

Purpose:

- Present methodology, viewpoints, report openings, and polished explanatory graphics.
- Make the diagram feel composed and editorial rather than technical-console-like.

Visual requirements:

- Use warm paper-like backgrounds, serif or editorial typography, strong title hierarchy inside nodes, and a small number of accent colors.
- Use restrained shadows and clean rectangular cards.
- Use black or warm ink arrows with small solid arrowheads.
- Keep the background pure by default. Do not add decorative circles or large background geometry unless explicitly requested.
- Keep editable diagrams fully functional: draggable nodes, editable text, auto-rerendered arrows, save/reset/export JSON/export PNG controls.

Avoid in `editorial`:

- Background circles, ornaments, or magazine decorations that distract from the flow.
- Overly corporate section frames.
- Neon, glass, or dashboard-like effects.

### `pastel`

Use this style for soft, approachable flowcharts.

Purpose:

- Explain user flows, product processes, training content, and lightweight internal materials.
- Make the diagram feel friendly while keeping the structure clear.

Visual requirements:

- Use soft low-saturation node colors and a clean light background.
- Use rounded but controlled nodes; keep radius moderate and professional.
- Use blue, teal, or soft purple arrows with small solid arrowheads.
- Keep the background pure by default. Do not add large decorative circles or blobs unless explicitly requested.
- Maintain enough contrast for all text and arrows.
- Keep editable diagrams fully functional: draggable nodes, editable text, auto-rerendered arrows, save/reset/export JSON/export PNG controls.

Avoid in `pastel`:

- Large decorative circles, blobs, or background ornaments.
- Low-contrast text that becomes hard to read.
- Overly childish colors or oversized rounded cards.

### `brutal`

Use this style for high-impact, high-contrast diagrams.

Purpose:

- Emphasize strong conclusions, comparisons, conflicts, and shareable technical graphics.
- Make the diagram feel bold and direct.

Visual requirements:

- Use a strong flat background, commonly yellow or another high-contrast color.
- Use thick black borders, bold typography, hard shadows, and simple geometric nodes.
- Use thick black arrows with small solid arrowheads; keep endpoints precise.
- Keep the background clean by default. Do not add decorative red blocks, tilted squares, or poster ornaments unless explicitly requested.
- Keep editable diagrams fully functional: draggable nodes, editable text, auto-rerendered arrows, save/reset/export JSON/export PNG controls.

Avoid in `brutal`:

- Extra decorative red blocks or shapes in unused corners.
- Thin low-contrast lines.
- Crowded text; brutal style needs fewer, stronger words.

### `dark`

Use this style for restrained dark professional diagrams.

Purpose:

- Present architecture, technical process, or formal report diagrams in a stable dark theme.
- Make the output feel professional rather than cyberpunk.

Visual requirements:

- Use a deep gray or near-black background, white or off-white text, and one or two restrained accent colors.
- Use clean rectangular nodes with thin borders and subtle shadows.
- Use warm or blue accent arrows with small solid arrowheads.
- Keep the background clean by default. Do not add decorative side rails, vertical accent bars, or large ornaments unless explicitly requested.
- Keep editable diagrams fully functional: draggable nodes, editable text, auto-rerendered arrows, save/reset/export JSON/export PNG controls.

Avoid in `dark`:

- Cyber neon glow overload; use `neon` for that.
- Decorative vertical rails or side bars.
- Low-contrast text, borders, or arrows.

## File Pattern

Use a task-specific folder under the current project, usually:

```text
output/flowcharts/<slug>/
  <slug>.mmd
  <slug>.md
  <slug>.html
  <slug>.png
  <slug>.svg
```

Only create export files that are requested or needed for delivery.

## HTML Requirements

For HTML flowcharts:

- Use semantic HTML and CSS variables.
- Use stable node dimensions with `min-width`, `max-width`, `min-height`, and wrapping.
- Use SVG for precise arrows when manual positioning is needed.
- Use horizontal scrolling for wide diagrams instead of compressing nodes until unreadable.
- Keep cards at 8px radius or less unless the existing design requires otherwise.
- Avoid decorative gradients, unrelated icons, or visual noise.
- Include enough labels so the diagram can stand alone.
- Draw only the flowchart by default. Do not add a title, explanatory paragraph, hero text, legend, or outer board/frame unless the user asks for it.
- When generating multiple requested themes, create one standalone HTML file per theme unless the user explicitly asks for a combined gallery or comparison page.
- Center the diagram in the HTML viewport and avoid vertical scrolling when the diagram can reasonably fit in one screen.
- Keep arrows modest in size. Arrowheads should land near the intended node edge and must not cover node text.
- For Chinese text, avoid single-character wrapping. Prefer wider nodes, explicit line breaks at phrase boundaries, `word-break: keep-all`, and `white-space: nowrap` for short headings.
- Decision diamond text must be visually centered inside the diamond. Avoid large vertical gaps between heading and subtitle; use flex/grid centering or explicit absolute positioning when needed.
- Do not create a separate canvas/paper background behind the chart unless requested. Let the browser page background be the chart background.
- For hand-drawn diagrams, render arrows behind nodes by default. Endpoints must connect from source edge to target edge, not to node centers or text blocks.
- For editable diagrams, arrows must connect by shape-aware ports: rectangles connect at edge midpoints; diamonds connect at their visible corners. Offset arrowheads slightly outside the node so they point to the border without entering the shape.
- Prefer small solid arrowheads for editable diagrams. Avoid large open arrowheads because they blur easily and make endpoint alignment look wrong.
- Editable diagrams should occupy about two thirds of the browser viewport by default, leaving whitespace around the chart for manual adjustment.
- The whitespace around an editable diagram must be inside the draggable canvas/workspace, not just empty browser margin created by scaling the whole canvas down.
- Editable diagrams should initialize with the chart group centered both horizontally and vertically within the editable canvas.
- Use a single visible border per node by default; do not add inner pale duplicate borders unless explicitly requested.
- For `mono` diagrams, do not use a grid background by default. Use a plain page background with black, white, and neutral gray linework.
- For `glass` diagrams, keep the dark background and translucent panels readable. Avoid excessive blur, heavy glow, or decorations that compete with arrows.
- For `blueprint` diagrams, do not use a grid background by default. Avoid inner duplicate borders or local grid-like patches around nodes.
- For `editorial`, `pastel`, `brutal`, and `dark` diagrams, keep the background clean by default. Avoid decorative circles, blobs, corner blocks, side rails, or ornaments unless the user explicitly requests them.

## Editable HTML Template Rules

Use `assets/editable-flowchart-template.html` for `sketch` + `editable` diagrams. Preserve these behaviors:

- Every node is draggable inside one large workspace.
- Node text and edge labels are `contenteditable`.
- Arrows rerender automatically after dragging or text edits.
- Ports are shape-aware: rectangles connect at edge midpoints; diamonds connect at visible corners.
- Arrowheads are small, solid, and close to node borders.
- The chart group initializes centered inside the larger editable workspace.
- The visible flow initially occupies about two thirds of the editable workspace, leaving real draggable whitespace around it.
- Nodes use a single border by default; no inner duplicate pale border.
- Local save/reset/export controls remain available unless the user requests a static artifact only.
- The toolbar should include image export. The default template exports the current canvas as `flowchart.png`.

When adapting the template, update the `edges` array and initial `left/top/width` values together. After any coordinate changes, load or preview the file and check that:

- initial nodes are not too close
- arrows are visible before any user dragging
- arrowheads point to the expected node boundary
- the user can drag nodes into the surrounding whitespace

Use `assets/mono-editable-flowchart-template.html` for `mono` + `editable` diagrams. Preserve these behaviors:

- Every node is draggable inside one large workspace.
- Node text, edge labels, and group titles are `contenteditable` where applicable.
- Arrows rerender automatically after dragging or text edits.
- The toolbar includes save, reset, export JSON, and export PNG.
- Visual styling remains black-and-white/gray, with a plain page background and no grid by default.
- Nodes use a single black border, compact radius, and no decorative shadows.
- Arrows use small solid black arrowheads; secondary feedback lines may be dashed gray.
- Initial layout should keep the chart centered and leave real draggable whitespace around the chart.

Use `assets/glass-editable-flowchart-template.html` for `glass` + `editable` diagrams. Preserve these behaviors:

- Every node is draggable inside one large workspace.
- Node text, edge labels, and group titles are `contenteditable` where applicable.
- Arrows rerender automatically after dragging or text edits.
- The toolbar includes save, reset, export JSON, and export PNG.
- Visual styling remains dark, translucent, and interface-like, with readable light text.
- Nodes use translucent panels, thin light borders, subtle shadows, and no heavy visual clutter.
- Arrows use small solid light arrowheads; secondary feedback lines may be dashed mint/cyan.
- Initial layout should keep the chart centered and leave real draggable whitespace around the chart.

For `blueprint`, `neon`, `editorial`, `pastel`, `brutal`, and `dark` + `editable` diagrams, preserve these behaviors even when no dedicated asset template exists:

- Every node is draggable inside one large workspace.
- Node text and edge labels are `contenteditable` where applicable.
- Arrows rerender automatically after dragging or text edits.
- The toolbar includes save, reset, export JSON, and export PNG.
- Ports are shape-aware: rectangles connect at edge midpoints; diamonds connect at visible corners.
- Decision diamond text is centered inside the diamond, with no large gap between heading and subtitle.
- Initial layout should keep the chart centered and leave real draggable whitespace around the chart.
- Avoid decorative background ornaments by default; visual style should come from color, typography, borders, arrows, and node treatment.

## Layout QA

When possible, open the HTML in a browser and inspect at desktop and mobile widths. For important deliverables, use a browser automation or screenshot workflow to confirm:

- chart is not blank
- all nodes are visible
- no node overlaps another node
- no critical text is clipped
- arrows are visible and do not obscure labels
- grouped areas fit their child nodes
- arrow starts and ends visually connect to the intended source/target edges
- feedback arrows are visible enough to understand the loop
- dense areas, especially bottom-right clusters, are checked manually in the rendered preview

Do not rely only on static checks for HTML flowcharts. After edits, render a preview by browser automation when available, or by macOS QuickLook (`qlmanage -t`) as a fallback, then inspect the generated image before final response.

If no rendered preview is possible, run the static checker in `scripts/check_flowchart_html.py` and state clearly that only static checks were performed.

## Bundled Resources

- `assets/flowchart-template.html`: starting point for an HTML/CSS flowchart.
- `assets/editable-flowchart-template.html`: stable `sketch` + `editable` HTML flowchart template with draggable nodes, editable text, shape-aware arrows, internal workspace whitespace, save/reset/export PNG/export JSON controls, and small solid arrowheads.
- `assets/mono-editable-flowchart-template.html`: stable `mono` + `editable` HTML flowchart template with draggable nodes, editable text, plain background, black/gray wireframe styling, save/reset/export PNG/export JSON controls, and small solid arrowheads.
- `assets/glass-editable-flowchart-template.html`: stable `glass` + `editable` HTML flowchart template with draggable nodes, editable text, dark atmospheric background, translucent panels, light arrows, save/reset/export PNG/export JSON controls, and small solid arrowheads.
- `blueprint`, `neon`, `editorial`, `pastel`, `brutal`, and `dark` do not yet have dedicated bundled templates. Build them by reusing the stable editable interaction skeleton and applying the style rules above.
- `scripts/check_flowchart_html.py`: lightweight static checker for common HTML output omissions.
