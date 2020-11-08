"""
bs4 https://pypi.org/project/beautifulsoup4/ helpers.
"""

from typing import Optional, List
from bs4 import element


def select_one(tag: element.Tag, selector: str,
               attribute: str, default: Optional[str] = None) -> Optional[str]:
    """
    Perform a CSS selection and returns attribute of first found tag.
    If no elements exists, returns `default` value.

    :param tag: bs4 Tag
    :param selector: CSS selector
    :param attribute:
        HTML attribute. `text` value stands for innerText of found tag
    :param default:
        `default` value returns if no tags found by `selector`
    :return:
    """
    elem = tag.select_one(selector)
    if elem is None:
        return default
    if attribute == 'text':
        return elem.text
    return elem.get(attribute, default)


def select_text_one(tag: element.Tag, selector: str):
    """
    Perform a CSS selection and receiving tag's innerText.
    Returns empty string if no tags found.

    :param tag: bs4 Tag
    :param selector: CSS selector
    :return:
    """
    return select_one(tag, selector, 'text', '')


def select_all(tag: element.Tag, selector: str, attribute: str) -> List[str]:
    """
    Perform a CSS selection and receiving attributes of all found tags.
    Skips tags that have no attribute `attribute`.

    :param tag:
    :param selector:
    :param attribute:
    :return:
    """
    result = []
    for elem in tag.select(selector):
        if attribute == 'text':
            result.append(elem.text)
        else:
            attr_value = elem.get(attribute)
            if attr_value is not None:
                result.append(attr_value)
    return result
