import PyPDF2
import os
import sys
from PyPDF2.utils import PdfReadError,PdfStreamError


class PDF(object):
    def __init__(self, pdf_filename):
        try:
            self.pdf_filename = pdf_filename
            self.pdf_file = open(self.pdf_filename, 'rb')
            self.pdf_reader = PyPDF2.PdfFileReader(self.pdf_file)
        except (IOError) as e:
            print(e, file=sys.stderr)
        except (PdfReadError, PdfStreamError, ValueError,AttributeError, TypeError) as e:
            print(e, file=sys.stderr)



    def get_title(self):
        title = None
        try:
            title = self.pdf_reader.getDocumentInfo().title
            # If title is not set in file, set as title the filename without pdf extension
            if not title:
                title = os.path.splitext(os.path.basename(self.pdf_filename))[0]
        except (IOError,ValueError,AttributeError) as e:
            print(e, file=sys.stderr)
        except (PdfReadError) as e:
            print("Cannot read title from file (maybe encrypted?): ", self.pdf_filename, file = sys.stderr)
        return title


    def get_page_text(self, page):
        self.pdf_page = self.pdf_reader.getPage(page)
        return self.pdf_page.extractText()




