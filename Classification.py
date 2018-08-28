import multiprocessing
import time
class Classification(object):
    def __init__(self):
        self.keyword_filename = "keywords.txt"
        self.read_keywords()
        self.classifications = {}


    def read_keywords(self):
        self.keywords = []
        with open(self.keyword_filename, 'r') as self.keyword_file:
            self.keywords = [ keyword.strip('\n') for keyword in self.keyword_file]


    def classify(self, titles):
        num_workers = int(multiprocessing.cpu_count() / 2)
        print("Starting with %d workers" % num_workers)
        pool = multiprocessing.Pool(processes=num_workers)
        mp = pool.imap_unordered(self.classify_title, titles)
        pool.close()
        pool.join()

    def classify_title(self, title):
        print("Classify title")
        title = str.lower(title)
        self.classifications[title] = []
        for keyword in self.keywords:
            if keyword in title:
                print("Found %s for %s" % (keyword, title))
                self.classifications[title].append(keyword)
