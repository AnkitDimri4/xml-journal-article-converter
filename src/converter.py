 
from .parser import extract_structure
from .xml_builder import build_xml_tree, write_xml

def process_article(input_path: str, output_path: str) -> None:
    data = extract_structure(input_path)
    root = build_xml_tree(data)
    write_xml(root, output_path)