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
6. Before completion, check layout quality:
   - no overlapping nodes
   - no visible text overflow
   - arrows do not cross important text
   - grouped containers have enough padding
   - long labels wrap cleanly
   - narrow screens either remain readable or use horizontal scrolling
   - the main loop or feedback path is visible
7. If layout fails, adjust positions, dimensions, wrapping, or grouping and check again.
8. Return local paths for created files and state what was verified.

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
- `formal`: professional architecture/report style for leadership reports, enterprise solution pages, PPT-ready architecture diagrams, and formal delivery documents.

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
- Use `formal` only when the user explicitly asks for formal report, architecture, consulting, enterprise, leadership, or PPT style.

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
- Center the diagram in the HTML viewport and avoid vertical scrolling when the diagram can reasonably fit in one screen.
- Keep arrows modest in size. Arrowheads should land near the intended node edge and must not cover node text.
- For Chinese text, avoid single-character wrapping. Prefer wider nodes, explicit line breaks at phrase boundaries, `word-break: keep-all`, and `white-space: nowrap` for short headings.
- Do not create a separate canvas/paper background behind the chart unless requested. Let the browser page background be the chart background.
- For hand-drawn diagrams, render arrows behind nodes by default. Endpoints must connect from source edge to target edge, not to node centers or text blocks.
- For editable diagrams, arrows must connect by shape-aware ports: rectangles connect at edge midpoints; diamonds connect at their visible corners. Offset arrowheads slightly outside the node so they point to the border without entering the shape.
- Prefer small solid arrowheads for editable diagrams. Avoid large open arrowheads because they blur easily and make endpoint alignment look wrong.
- Editable diagrams should occupy about two thirds of the browser viewport by default, leaving whitespace around the chart for manual adjustment.
- The whitespace around an editable diagram must be inside the draggable canvas/workspace, not just empty browser margin created by scaling the whole canvas down.
- Editable diagrams should initialize with the chart group centered both horizontally and vertically within the editable canvas.
- Use a single visible border per node by default; do not add inner pale duplicate borders unless explicitly requested.

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
- `scripts/check_flowchart_html.py`: lightweight static checker for common HTML output omissions.
