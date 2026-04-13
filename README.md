# XML Journal Article Converter

Python-based **XML Journal Article Converter** that takes a simple journal‑style HTML file and generates a JATS‑inspired XML article. The tool extracts the article title, authors, abstract, sections, and references, and outputs a clean, machine‑readable XML file suitable for editorial and QA workflows.

> ##### Live Link : https://ankitdimri4.github.io/xml-journal-article-converter/

## Features

- Parses journal‑style HTML articles using `lxml`
- Extracts:
  - Article title (`<h1>`)
  - Author line (author paragraph / `.author-line`)
  - Abstract paragraph (`.abstract`)
  - Section headings and paragraphs (`<h2>` + `<p>`)
  - References under a “References” heading
- Builds a JATS‑inspired XML tree:
  - `<article>`
    - `<front>`: title, authors, abstract
    - `<body>`: sections and paragraphs
    - `<back>`: reference list (`<ref-list>`)
- Outputs well‑formed, pretty‑printed XML

## Project Structure

```txt
xml-journal-article-converter/
├── src/
│   ├── parser.py         # HTML parsing and structure extraction
│   ├── converter.py      # Orchestration of parse → XML build → write
│   └── xml_builder.py    # XML tree construction and file writing
├── tests/
│   └── sample_article.html   # Sample HTML article (project summary)
├── output/
│   └── .gitkeep              # Generated XML files go here
├── convert.py                # CLI entrypoint
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/AnkitDimri4/xml-journal-article-converter.git
cd xml-journal-article-converter
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt` currently includes:

```txt
lxml>=4.9
```

If you need DOCX support later, you can add:

```bash
pip install python-docx
```

## Usage

From the project root, run:

```bash
python convert.py tests/sample_article.html output/article.xml
```

If everything is set up correctly, you should see:

```text
XML generated at: output/article.xml
```

The generated XML will be in `output/article.xml` with a structure like:

```xml
<article>
  <front>
    <title-group>
      <article-title>...</article-title>
    </title-group>
    <contrib-group>
      <contrib contrib-type="author">...</contrib>
      ...
    </contrib-group>
    <abstract>...</abstract>
  </front>
  <body>
    <sec>
      <title>Introduction</title>
      <p>...</p>
      ...
    </sec>
    ...
  </body>
  <back>
    <ref-list>
      <ref ref-type="bib">...</ref>
      ...
    </ref-list>
  </back>
</article>
```

## Testing the HTML Input

A sample HTML article is provided at `tests/sample_article.html` (your project summary page). To quickly view it in the browser during development, you can start a simple HTTP server from the project root:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/tests/sample_article.html
```

## Notes and Future Work

- This project focuses on a **minimal, JATS‑inspired structure**, not full JATS compliance.
- The HTML parser is intentionally simple and assumes a consistent article layout.
- Possible extensions:
  - Support for DOCX input via `python-docx`
  - Richer JATS tagging (figures, tables, inline citations)
  - Web UI for uploading an article and downloading XML

---

## Relevance to XML Conversion Specialist Role

This project was created to demonstrate skills that map directly to an XML Conversion Specialist position:

- **XML‑style structuring:** Converts journal‑style HTML into a JATS‑inspired XML article with `<article>`, `<front>`, `<body>`, and `<back>` sections, including title, authors, abstract, sections, and references.
- **XPath‑style extraction thinking:** Uses `lxml` to traverse and extract elements (headings, paragraphs, reference blocks), similar to how XPath/XSLT workflows operate on XML trees.
- **Parsing and validation mindset:** Focuses on producing well‑formed, pretty‑printed XML that can be inspected or validated and easily integrated into automated QA or conversion pipelines.
- **Conversion pipeline experience:** Implements an end‑to‑end conversion flow (input → parse → transform → XML output) which is the core of many XML‑to‑XML or text‑to‑XML conversion projects in publishing and educational content.

Although this tool currently converts **HTML → JATS‑style XML** rather than XML‑to‑XML with XSLT, it shows that I can work with structured content, think in terms of tags and schemas, and build reliable Python tooling around XML documents—skills that are transferable to client‑specific XML transformation and QA tasks.

---
## Author

**Ankit Dimri**  
Full-Stack & AI Developer  
📍 Dehradun, India  

[![GitHub](https://img.shields.io/badge/GitHub-AnkitDimri4-black?logo=github)](https://github.com/AnkitDimri4)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ankit%20Dimri-blue?logo=linkedin)](https://linkedin.com/in/ankit-dimri-a6ab98263)
[![LeetCode](https://img.shields.io/badge/LeetCode-Profile-orange?logo=leetcode)](https://leetcode.com/u/user4612MW/)

---

## Technologies Used in This Project

### Core

![Python](https://img.shields.io/badge/Language-Python-blue?logo=python)
![lxml](https://img.shields.io/badge/Library-lxml-lightgrey)
![XML](https://img.shields.io/badge/Format-XML-blueviolet)
![HTML](https://img.shields.io/badge/Input-HTML-orange)
![CLI](https://img.shields.io/badge/Interface-Command_Line-informational)

### Tooling & Workflow

![Git](https://img.shields.io/badge/Version_Control-Git-orange?logo=git)
![GitHub](https://img.shields.io/badge/Repo-GitHub-black?logo=github)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## Project Info

- **Project:** XML Journal Article Converter  
- **Role / Focus:** XML conversion, JATS‑style tagging, Python scripting  
- **Year:** 2026  
- **Use case:** Converting simple journal‑style HTML articles into JATS‑inspired XML for editorial and QA workflows.

---

<div align="center">
Built with ❤️ by <span>Ankit Dimri</span>
</div>

---
