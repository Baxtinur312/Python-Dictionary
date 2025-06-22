def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    result = {}
    for student in students:
        group = student["group"]
        name = student["name"]
        result.setdefault(group, []).append(name)
    return result

