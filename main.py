import sys
import os


NUM_WORKERS = 4
from PDF import PDF
def check_dir(path):
    for dirpath, dnames, fnames in os.walk(path):
        for f in fnames:

            if f.endswith("pdf"):
                pdf = PDF(os.path.join(dirpath, f))
                title = pdf.get_title()
                print(title)

            else:
                print("File is not pdf ", file=sys.stderr)
if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "/space/Training + Ebooks/"
        check_dir(path)