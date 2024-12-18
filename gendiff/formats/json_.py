import json


def call_encoder(obj):
    if isinstance(obj, bool):
        return "true" if obj else "false"
    elif obj is None:
        return "null"
    raise TypeError(
        f'Object of type {type(obj).__name__} is not JSON serializable')


def format_json(dict_diff):
    res = json.dumps(dict_diff, indent=4, default=call_encoder)
    return res
