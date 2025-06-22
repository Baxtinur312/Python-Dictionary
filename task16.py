data = {"name": "Ali",
        "age": 25, 
        "city": "Tashkent"}
key = input("Kalitni kiriting: ")
if key in data:
    del data[key]
    print(f"{key} o'chirildi.")
else:
    print("Bunday kalit yo'q")
