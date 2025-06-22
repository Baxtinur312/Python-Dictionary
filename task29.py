def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    return [name for name, info in users.items() if info.get("active")]

# Misol
users = {
    "Ali": {"active": True},
    "Vali": {"active": False},
    "Sami": {"active": True}
}
print(get_active_users(users))  
