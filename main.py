import sys
import os
from PDF import PDF
if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "/home/kostas/Downloads"
    for dirpath,dnames,fnames in os.walk(path):
        for f in fnames:
            if f.endswith("pdf"):
                pdf = PDF(os.path.join(dirpath, f))
                print(pdf.get_page_text(0))

