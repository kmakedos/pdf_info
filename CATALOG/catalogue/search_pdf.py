import os
from collections import Counter

flatten = lambda t: [item for sublist in t for item in sublist]

class Search:
    def __init__(self, path=".", dest_path=None, logger=None, db=None):
        self._path = path
        self._catalogue = {}
        self._counter = Counter()
        self._logger = logger
        self._forbidden = ["and", "or", "not", "is", "are", "at", "to", "the", "it", "ed", "vol","jpg", "jpeg", "pdf", "txt", "png"
                           "for", "-", "of", "index", "in", "on", "with", "&", "an", "by", "pdf", ",", "htm", "html", "for"]

        self._forbidden += [letter for letter in "abcdefghjijklmnopqrstuvwxyz1234567890(){}[]@"]
        self._logger.debug(f"Initializing forbidden words {self._forbidden}")
        self.search_path(self._path)

    def search_path(self, path=None):
        if not path:
            path = self._path
        self._logger.debug(f"Parsing path {path}")
        for root, dirs, files in os.walk(path, topdown=True):
            for name in files:
                # self._logger.debug(f"Parsing filename {name}")
                # Remove extension (eg .txt, .pdf), should be a more clever way to do this
                filename = " ".join(name.split('.')[:-1])
                if filename not in self._catalogue.keys():
                    self._catalogue[filename] = [os.path.join(root, name)]
                else:
                    self._catalogue[filename].append(os.path.join(root, name))
                new_words = [word for word in filename.split() if word.lower() not in self._forbidden]
                self._counter.update(new_words)

    def get_catalogue(self):
        return self._catalogue

    def get_most_common(self, n):
        return self._counter.most_common(n)

    def _search_word(self, word):
        if word in self._catalogue.keys():
            return self._catalogue[word]
        else:
            return []

    def search_words(self, words):
        results = []
        max_score = len(words)
        self._logger.debug(f"Searching {words} in our catalogue")
        for name in self._catalogue.keys():
            score = 0
            for word in words:
                if word in name:
                    score += 1
            if score == max_score:
                results.append(self._search_word(name))
                self._logger.debug(f"{name} added in our results")
        return flatten(results)



