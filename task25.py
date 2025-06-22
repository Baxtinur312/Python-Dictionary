def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    result = {}
    for person in people:
        age = person["age"]
        name = person["name"]
        result.setdefault(age, []).append(name)
    return result


