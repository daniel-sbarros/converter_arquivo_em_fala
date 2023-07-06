def ler_txt(path):
    with open(path, 'r') as file:
        text = file.read()
    return text
