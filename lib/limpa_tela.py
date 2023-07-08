import os

def clear():
    os_name = os.name.lower()
    if os_name == 'posix':  # Linux e macOS
        os.system('clear')
    elif os_name == 'nt':  # Windows
        os.system('cls')
    else:
        print("Não foi possível limpar o shell. Sistema operacional não suportado.")

