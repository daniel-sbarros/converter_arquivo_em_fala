import os
import tkinter as tk
from tkinter import filedialog

from lib.convert_text_to_voice import convert_text_to_voice
from lib.ler_docx import ler_docx
from lib.ler_pdf import ler_pdf
from lib.ler_txt import ler_txt


def get_extension(file_path: str):
    return os.path.splitext(file_path)[1].replace(".", "")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.pdf *.doc *.docx *.txt" )])

    if get_extension(file_path) == "txt":
        convert_text_to_voice(ler_txt(file_path))
    elif get_extension(file_path) == "pdf":
        convert_text_to_voice(ler_pdf(file_path))
    elif get_extension(file_path) == "docx" or get_extension(file_path) == "doc":
        convert_text_to_voice(ler_docx(file_path))
    else:
        print('Arquivo de formato inválido.')

