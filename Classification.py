import multiprocessing


class Classification(object):
    def __init__(self, keywords):
        self.keywords = keywords
        self.classifications = []
        self.num_workers = int(multiprocessing.cpu_count() / 2)
        print("Starting with %d workers" % self.num_workers)


    def classify(self, titles):
        pool = multiprocessing.Pool(processes=self.num_workers)
        wp = pool.map_async(self.classify_title, titles, callback=self.classifications.append)
        pool.close()
        pool.join()
        wp.wait()


    def classify_title(self, title):
        title_keywords = []
        title = str.lower(title)
        for keyword in self.keywords:
            if keyword in title:
                title_keywords.append(keyword)
        return {title:title_keywords}

    def get_classifications(self):
        return self.classifications