def phonebook_menu(phonebook: dict[str, str]) -> None:
    while True:
        print("\n1: Qo‘shish\n2: Ko‘rish\n3: Qidirish\n0: Chiqish")
        choice = input("Tanlang: ")
        if choice == "1":
            name = input("Ism: ")
            phone = input("Telefon: ")
            phonebook[name] = phone
        elif choice == "2":
            for name, phone in phonebook.items():
                print(f"{name}: {phone}")
        elif choice == "3":
            name = input("Qidirilayotgan ism: ")
            print(phonebook.get(name, "Topilmadi"))
        elif choice == "0":
            break
        else:
            print("Noto‘g‘ri tanlov")

