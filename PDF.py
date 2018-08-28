import PyPDF2
import os
import sys
from PyPDF2.utils import PdfReadError,PdfStreamError
import multiprocessing

class PDF(object):
    def __init__(self, path):
        self.path = path
        self.results = []
        self.num_workers = int(multiprocessing.cpu_count() / 2)
        print("Starting with %d workers" % self.num_workers)

    def find_pdf_files(self):
        self.pdfs = []
        for dirpath, dnames, fnames in os.walk(self.path):
            for f in fnames:
                if f.endswith("pdf"):
                    pdf_filepath = os.path.join(dirpath, f)
                    self.pdfs.append(pdf_filepath)
        return self.pdfs

    def extract_titles(self):
        pool = multiprocessing.Pool(processes=self.num_workers)
        pdfs = self.find_pdf_files()
        mp = pool.map_async(self.get_title, pdfs, callback=self.results.append)
        mp.wait()

    def get_results(self):
        return self.results

    def get_title(self, pdf_filename):
        title = "No title"
        try:
            self.pdf_filename = pdf_filename
            self.pdf_file = open(self.pdf_filename, 'rb')
            self.pdf_reader = PyPDF2.PdfFileReader(self.pdf_file)
            title = self.pdf_reader.getDocumentInfo().title
            # If title is not set in file, set as title the filename without pdf extension
            if not title:
                title = os.path.splitext(os.path.basename(self.pdf_filename))[0]
        except (PdfReadError, PdfStreamError, ValueError,AttributeError, TypeError, IOError) as e:
            print(e, file=sys.stderr)
        return title

    def get_page_text(self, page):
        self.pdf_page = self.pdf_reader.getPage(page)
        return self.pdf_page.extractText()




