from PyPDF2 import PdfFileReader


class Reader:
    def __init__(self):
        pass

    def extract_information(self, pdf_path):
        with open(pdf_path, 'rb') as f:
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()

        txt = f"""
        Information about {pdf_path}: 

        Author: {information.author}
        Creator: {information.creator}
        Producer: {information.producer}
        Subject: {information.subject}
        Title: {information.title}
        Number of pages: {number_of_pages}
        """

        return txt, information