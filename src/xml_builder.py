 
from lxml import etree

def build_xml_tree(data: dict) -> etree._Element:
    root = etree.Element("article")

    # front
    front = etree.SubElement(root, "front")

    title_group = etree.SubElement(front, "title-group")
    article_title = etree.SubElement(title_group, "article-title")
    article_title.text = data.get("title", "")

    contrib_group = etree.SubElement(front, "contrib-group")
    for author in data.get("authors", []):
        contrib = etree.SubElement(contrib_group, "contrib")
        contrib.set("contrib-type", "author")
        contrib.text = author

    abstract_el = etree.SubElement(front, "abstract")
    abstract_el.text = data.get("abstract", "")

    # body
    body = etree.SubElement(root, "body")
    for sec in data.get("sections", []):
        sec_el = etree.SubElement(body, "sec")
        title_el = etree.SubElement(sec_el, "title")
        title_el.text = sec.get("title", "")
        for para in sec.get("paragraphs", []):
            p_el = etree.SubElement(sec_el, "p")
            p_el.text = para

    # back + references
    back = etree.SubElement(root, "back")
    ref_list = etree.SubElement(back, "ref-list")
    for ref_text in data.get("references", []):
        ref_el = etree.SubElement(ref_list, "ref")
        ref_el.set("ref-type", "bib")
        ref_el.text = ref_text

    return root

def write_xml(xml_root, output_path: str) -> None:
    xml_bytes = etree.tostring(
        xml_root,
        pretty_print=True,
        xml_declaration=True,
        encoding="utf-8",
    )
    with open(output_path, "wb") as f:
        f.write(xml_bytes)