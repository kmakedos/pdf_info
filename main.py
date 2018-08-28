import sys
import os
from PDF import PDF
import time
import multiprocessing

def find_pdf_files(path):
    pdfs = []
    for dirpath, dnames, fnames in os.walk(path):
        for f in fnames:
            if f.endswith("pdf"):
                pdf_filepath = os.path.join(dirpath, f)
                pdfs.append(pdf_filepath)
    return pdfs
def get_pdf_title(pdf_filepath):
    pdf = PDF(pdf_filepath)
    print(pdf.get_title())




if __name__ == "__main__":
    start_time = time.time()
    NUM_WORKERS = int(multiprocessing.cpu_count() / 2)
    print("Starting with %d workers" % NUM_WORKERS)
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "/space/Training + Ebooks/"
        pdfs = find_pdf_files(path)
        pool = multiprocessing.Pool(processes=NUM_WORKERS)
        mp = pool.map_async(get_pdf_title, pdfs)
        mp.wait()
    end_time = time.time()
    print("Process finished in %ssecs using %d workers" %((end_time - start_time), NUM_WORKERS))