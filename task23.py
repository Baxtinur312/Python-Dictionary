def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    result = {}
    for idx, num in enumerate(numbers):
        result.setdefault(num, []).append(idx)
    return result


