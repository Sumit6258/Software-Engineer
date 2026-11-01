# Extraction Report

> **Generated file.** Produced by `tools/build.py` from `curriculum/curriculum.json` (parsed from the authoritative syllabus). Do not edit by hand; change the source data or the generator instead.

How the source syllabus was read, what was interpreted, and what was removed. Nothing is dropped silently.

## Source file

| Property | Value |
| --- | --- |
| File | `curriculum/source/Software_Engineering_Topics.docx` |
| Size | 145882 bytes |
| SHA-256 | `a3bc28b0e956eb5965fd187c6c4024a9f48ddb7121f6f1f52345bd0390cf9df7` |

## How the hierarchy was recovered

The `.docx` has no heading styles and every bullet has list level 0, so nesting is not stored as indentation. The hierarchy was recovered from the document's own markers:

| Source marker | Meaning in this repository |
| --- | --- |
| Outline level 0 (`PART …`) | Part |
| Outline level 1 beginning `N.` | Numbered subject area |
| Outline level 1 without a number | Section heading inside a part (Part XV) |
| Outline level 2 | Sub-section inside a subject (treated as a group) |
| Plain paragraph beginning `- ` | Group, which becomes a chapter |
| Bullet paragraph | Topic |
| Plain paragraph followed by bullets | Sub-group label (or, if it ends with `:`, a group) |
| Table | One topic per row (languages, frameworks, technology categories, stages, roles) |
| Image caption followed by a name and description | Technology card; one topic per card |

## Parser decisions that add structure

These decisions affect structure only. No topic text was changed.

- **32 subjects** have bullets that appear directly under the subject heading with no group heading. They were collected into a synthesized group named “Core topics”: S07, S13, S18, S20, S21, S25, S27, S28, S29, S34, S35, S38, S39, S40, S43, S45, S46, S47, S48, S49, S50, S51, S52, S53, S55, S56, S59, S60, S61, S62, S63, S64.
- S08: language table converted to synthesized group 'Major programming languages' (one topic per row).
- S38: label 'Advanced:' became group 'Advanced topics'.
- S39: label 'Advanced:' became group 'Advanced topics'.
- S45: label 'Advanced:' became group 'Advanced topics'.
- S51: label 'Advanced:' became group 'Advanced topics'.

## Source noise that was removed

The document was exported from a chat interface and still contains web-image captions and citation chips. They are not curriculum topics.

| Kind | Count |
| --- | --- |
| citation-chip | 2 |
| image-caption-link | 11 |
| trailing-link-text | 3 |

<details><summary>Every removed item</summary>

| Kind | Text | Body element |
| --- | --- | --- |
| image-caption-link | Postgresql Logo PNG Transparent With Clear Background ID 473068 \| TOPpng | 1070 |
| image-caption-link | Kanbel Technologies | 1073 |
| image-caption-link | Building a web3 frontend with React - DEV Community | 1252 |
| image-caption-link | Angular in 2024: What’s New and Why It’s Still a Top Choice for Web Developers \| by Rama Jonnada \| Medium | 1255 |
| image-caption-link | La versatilidad para integrar Vue Desarrolladores Páginas Web | 1258 |
| image-caption-link | Svelte: Web development made simple - Productive Programmer - Stories, Tips & Frustrations | 1261 |
| image-caption-link | AWS Signature Version 4 - Overview (ODC) \| OutSystems | 1608 |
| trailing-link-text | AWS official website | 1610 |
| image-caption-link | Data Platform: Building An Azure DataHub \| PTR | 1611 |
| trailing-link-text | Azure official website | 1613 |
| image-caption-link | Google Cloud to provide AI and cloud services to Brazilian energy firm Eneva - DCD | 1614 |
| trailing-link-text | Google Cloud official website | 1616 |
| citation-chip | NIST+2 | 2713 |
| image-caption-link | Qué es un motor gráfico, sus tipos y los videojuegos populares \| Blog PcComponentes | 2751 |
| image-caption-link | The first preview version of Unreal Engine 5 is available for download | 2754 |
| citation-chip | IBM Technology Atlas+1 | 3019 |

</details>

The removed caption links pointed at an image host and were discarded. The three official-site links (AWS, Azure, Google Cloud) were kept as the `url` of those provider cards after removing tracking parameters.

## Claims in the source that this repository has not verified

Three closing notes in the source refer to external organisations: NIST's AI Risk Management Framework and Generative AI Profile (subject 46), and IBM's published quantum roadmap and the post-quantum cryptography distinction (subject 54). In the source these carried citation chips whose sources were not preserved. They are retained verbatim in [COMPLETE-CURRICULUM.md](../COMPLETE-CURRICULUM.md) but must be verified against the primary documents before being repeated in a lesson.
