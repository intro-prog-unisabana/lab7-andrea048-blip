from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    """TODO: Parte 5 - programa principal interactivo."""
import password_manager

# Paso 1: pedir archivo
usuario = input("Enter the CSV file name:")

# Paso 2: encriptar todo el archivo
password_manager.encrypt_passwords_in_file(usuario)

# Paso 3: menú en loop
while True:
    option = input("Options: (1) Change Password, (2) Add Password, (3) Quit:")

    # 🔹 OPCIÓN 1
    if option == "1":
        web_pass = input("Enter the website and the new password:")
        parts = web_pass.split()

        if len(parts) != 2:
            print("Input is in the wrong format!")
            continue

        website, new_password = parts

        if len(new_password) < 12:
            print("Password is too short!")
            continue

        result = password_manager.change_password(usuario, website, new_password)

        if not result:
            print("Website not found! Operation failed.")
        else:
            print("Password changed.")

    # 🔹 OPCIÓN 2
    elif option == "2":
        data = input("Enter the website, username, and password:")
        parts = data.split()

        if len(parts) != 3:
            print("Input is in the wrong format!")
            continue

        website, username, password = parts

        if len(password) < 12:
            print("Password is too short!")
            continue

        password_manager.add_login(usuario, website, username, password)
        print("Login added.")

    # 🔹 OPCIÓN 3
    elif option == "3":
        break

    # 🔹 OPCIÓN INVÁLIDA
    else:
        print("Invalid option selected!")



if __name__ == "__main__":
    main()
