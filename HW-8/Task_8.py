import re


def to_camel_case(key):
    words = re.split(r"[^a-zA-Z0-9]", key)
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


def convert_to_camel_case(data):
    if isinstance(data, dict):
        return {
            to_camel_case(key): convert_to_camel_case(value)
            for key, value in data.items()
        }
    else:
        return data
