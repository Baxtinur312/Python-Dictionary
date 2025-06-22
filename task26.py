def merge_dicts(a: dict, b: dict) -> dict:
    merged = a.copy()
    merged.update(b)
    return merged

print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))



