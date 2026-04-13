import csv
from fileinput import filename


from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    with open(filename, "r") as file:
        password= file.read().strip()
    encrypted_password = caesar_encrypt(password)
    with open(filename,"w") as file:
        file.write(encrypted_password)


def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    data = []

    with open(filename, "r") as file:
        lector = csv.reader(file)

        for row in lector:
            if len(row) < 3:
                continue
            data.append(row)

    for index, row in enumerate(data):
        if index != 0:
            row[2] = caesar_encrypt(row[2])

    with open(filename, "w", newline='') as file:
        escritor = csv.writer(file)
        escritor.writerows(data)


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    rows = []  
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                rows.append(row)

    found = False

    for i in range(1, len(rows)): 
        if rows[i][0].strip() == website.strip():
            rows[i][2] = caesar_encrypt(password)
            found = True

    if not found:
        return False

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return True


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        encrypted_password = caesar_encrypt(password)
        writer.writerow([website_name, username, encrypted_password])   


if __name__ == "__main__":
    encrypt_single_pass("examples/example1.txt")
    encrypt_passwords_in_file("examples/example2.csv")
    r=change_password("examples/example3.csv", "testsite.com", "newsecurepass")
    print(r)
    add_login("examples/example3.csv", "newsite.com", "newuser", "mypassword123")