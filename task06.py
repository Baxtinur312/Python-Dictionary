kod = input("Enter the code(Numbers only): ")

correct_codes = ["3275", "3276", "3277", "3278", "3279"]
if kod == correct_codes[0] or kod in correct_codes[1:]:
    print("Correct code! " + kod)
else:
    print("Topilmadi")
    