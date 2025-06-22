def group_by_length(words: list[str]) -> dict[int, list[str]]:
    result = {}
    for word in words:
        length = len(word)
        result.setdefault(length, []).append(word)
    return result

 