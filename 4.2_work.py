language_num = input("Введите 1, чтобы был русский, введите 2, чтобы был английский: ")
match language_num:
    case "1":
        print("Привет, Мир")
    case "2":
        print("Hello World")
    case _:
        print("Вы ввели неправильное число")
