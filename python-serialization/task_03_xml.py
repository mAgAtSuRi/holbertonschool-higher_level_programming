#!/usr/bin/python3
import xml.etree.ElementTree as ET

"""Module for XML serialization and deserialization"""


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into XML and save it to filename"""
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=False)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """Deserialize XML from filename and return a Python dictionary"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text  # keep everything as string
        return result
    except Exception:
        return None
