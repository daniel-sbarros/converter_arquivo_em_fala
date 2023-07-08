import PyPDF2


# def ler_pdf(file_path):
#     with open(file_path, 'rb') as pdf_file:
#         pdf_reader = PyPDF2.PdfReader(pdf_file)
#         text = ""
#         for page in pdf_reader.pages:
#             text += page.extract_text()
#         return text

def ler_pdf(file_path):
    pdf_pages = []
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page_num in range(len(pdf_reader.pages)):
            pdf_page = pdf_reader.pages[page_num]
            pdf_pages.append(pdf_page.extract_text())

    return pdf_pages