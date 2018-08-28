import sys
import os
import time

from PDF import PDF
from Classification import Classification


def read_keywords(keyword_filename):
    keywords = []
    with open(keyword_filename, 'r') as keyword_file:
        for keyword in keyword_file:
            keyword = keyword.strip('\n')
            keywords.append(keyword)
    keyword_file.close()
    return keywords

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
        keywords = read_keywords("keywords.txt")
        classifier = Classification(keywords)
        classifier.classify(results[0])
        print(classifier.get_classifications())
    end_time = time.time()
    print("Process finished in %ssecs" %((end_time - start_time)))