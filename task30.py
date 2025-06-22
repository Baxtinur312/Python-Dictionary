def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    return {k: v for k, v in d.items() if v != 0}

print(filter_non_zero({"a": 869, "b": 7987, "c": 9787}))
