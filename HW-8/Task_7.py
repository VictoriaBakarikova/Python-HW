def serialize(object):
    if isinstance(object, list):
        return "[" + ", ".join(serialize(item) for item in object) + "]"
    elif isinstance(object, dict):
        items = [f'"{key}": {serialize(value)}' for key, value in object.items()]
        return "{" + ", ".join(items) + "}"
    elif isinstance(object, str):
        return f'"{object}"'
    elif isinstance(object, (int, float, bool)):
        return str(object).lower()
    elif object is None:
        return "null"
    else:
        raise TypeError
