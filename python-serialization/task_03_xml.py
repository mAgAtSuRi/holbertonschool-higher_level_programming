#!/usr/bin/python3

import xml.etree.ElementTree as ET

"""Module for Serializing and Deserializing with XML"""


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into XML and save it to filename"""
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        tree = ET.SubElement(root, key)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
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
            if text is None:
                result[child.tag] = None
            elif text.lower() in ("true", "false"):
                result[child.tag] = text.lower() == "true"
            else:
                try:
                    result[child.tag] = int(text)
                except ValueError:
                    result[child.tag] = text
        return result
    except Exception:
        return None
