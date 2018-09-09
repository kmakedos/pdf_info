import sys
import time

from PDF import PDF
from Classification import Classification


def read_keywords(keyword_filename):
    keywords = []
    with open(keyword_filename, 'r') as keyword_file:
        for keyword in keyword_file:
            keyword = keyword.strip('\n')
            keywords.append(str.lower(keyword))
    keyword_file.close()
    return keywords

if __name__ == "__main__":
    start_time = time.time()
    results = []
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "/media/kostas/Home/Ebooks-Videos/Selected Ebooks"
        pdf = PDF(path)
        pdf.extract_titles()
        results = pdf.get_results()
        keywords = read_keywords("keywords.txt")
        classifier = Classification(keywords)
        classifier.classify(results[0])
        for each_obj in classifier.get_classifications():
            for each_dict in each_obj:
                for k,v in each_dict.items():
                    print(k,v)

    end_time = time.time()
    print("Process finished in %ssecs" %((end_time - start_time)))