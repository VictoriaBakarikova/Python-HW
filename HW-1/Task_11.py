ip_adress = input("Введите IP-адрес: ")
parts = ip_adress.split(".")
is_valid = True
if len(parts) != 4:
    is_valid = False
else:
    for part in parts:
        if not part.isdigit():
            is_valid = False
            break
        if not (0 <= int(part) <= 255):
            is_valid = False
            break
if is_valid:
    print("Correct IP")
else:
    print("Incorrect IP")
