import docx


def ler_docx(path: str):
    doc = docx.Document(path)
    text = ""
    for paragraph in doc.paragraphs:
        text += f"{paragraph.text}\n"
    return text
