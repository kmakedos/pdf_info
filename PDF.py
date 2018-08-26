import PyPDF2

class PDF(object):
    def __init__(self, pdf_file):
        try:
            self.pdf_file = open(pdf_file, 'rb')
            self.pdf_reader = PyPDF2.PdfFileReader(self.pdf_file)
        except (PyPDF2.PdfReadError, IOError) as e:
            print(e.strerror)
    def get_page_text(self, page):
        self.pdf_page = self.pdf_reader.getPage(page)
        return self.pdf_page.extractText()




