def count_names(names: list[str]) -> dict[str, int]:
    result = {}
    for name in names:
        result[name] = result.get(name, 0) + 1
    return result
