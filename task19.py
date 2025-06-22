scores = {"math": 90, "english": 85, "science": 92}
total = sum(value for value in scores.values() if isinstance(value, (int, float)))
print("Yig'indi:", total)  # 267
