import sys
import os
import time

from PDF import PDF
from Classification import Classification

if __name__ == "__main__":
    start_time = time.time()
    results = []
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "/space/Training + Ebooks/"
        pdf = PDF(path)
        pdf.extract_titles()
        results = pdf.get_results()
        classifier = Classification()
        classifier.classify(results)
        print(classifier.classifications)
    end_time = time.time()
    print("Process finished in %ssecs" %((end_time - start_time)))