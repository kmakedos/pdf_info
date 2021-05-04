import shelve


class DB:

    def __init__(self, db_path):
        self._db = shelve.open(db_path)

    def get(self, key):
        return self._db[key]

    def put(self, key, value):
        self._db[key] = value