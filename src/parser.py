from lxml import html

def extract_structure(html_path: str) -> dict:
    with open(html_path, "r", encoding="utf-8") as f:
        tree = html.fromstring(f.read())

    # Title: first <h1>
    title_nodes = tree.xpath("//h1")
    title = title_nodes[0].text_content().strip() if title_nodes else ""

    # Author line: .author-line paragraph or first <p>
    author_nodes = tree.xpath("//p[contains(@class, 'author-line')]")
    if author_nodes:
        authors_text = author_nodes[0].text_content().strip()
    else:
        p_nodes = tree.xpath("//p")
        authors_text = p_nodes[0].text_content().strip() if p_nodes else ""
    authors = [a.strip() for a in authors_text.split("–")[0].split(",") if a.strip()]

    # Abstract: .abstract paragraph
    abstract_nodes = tree.xpath("//p[contains(@class, 'abstract')]")
    abstract = abstract_nodes[0].text_content().strip() if abstract_nodes else ""

    sections = []
    h2_nodes = tree.xpath("//h2")
    for h2 in h2_nodes:
        sec_title = h2.text_content().strip()
        paragraphs = []
        sibling = h2.getnext()
        while sibling is not None and sibling.tag not in ("h2", "h1"):
            # skip button rows / non-text containers
            if sibling.tag == "p":
                paragraphs.append(sibling.text_content().strip())
            sibling = sibling.getnext()
        sections.append({"title": sec_title, "paragraphs": paragraphs})

    # References: from <h2> with text "References" onward
    references = []
    refs_headings = tree.xpath("//h2[normalize-space(text())='References']")
    if refs_headings:
        node = refs_headings[0].getnext()
        while node is not None:
            if node.tag in ("div", "section"):
                for p in node.xpath(".//p"):
                    txt = p.text_content().strip()
                    if txt:
                        references.append(txt)
            elif node.tag == "p":
                txt = node.text_content().strip()
                if txt:
                    references.append(txt)
            node = node.getnext()

    return {
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "sections": sections,
        "references": references,
    }