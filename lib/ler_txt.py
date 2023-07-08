def ler_txt(path):
    text = ""
    with open(path, 'r') as file:
        for row in file:
            text += row.strip() + "\n"
    return text.strip()
