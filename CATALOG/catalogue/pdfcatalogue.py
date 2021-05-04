import os
import shutil
from catalogue import log, parser, search_pdf, database


def main():
    for dir in ["log", "db"]:
        if not os.path.exists(dir):
            os.mkdir(dir)
    catalogue_logger = log.Logger("log/catalogue.log")
    catalogue_logger.logger.debug(f"Starting catalogue")
    catalogue_parser = parser.Parser(logger=catalogue_logger.logger, commands=["list", "find", "most_common"])
    command, folder, n, dest_path, words = catalogue_parser.parse_arguments()
    search = search_pdf.Search(folder, logger=catalogue_logger.logger)
    if command == "list":
        for file in search.get_catalogue().keys():
            print(f"{file}")
    if command == "find" and not dest_path:
        for file in search.search_words(words):
            print(f"{file}")
    if command == "find" and dest_path:
        for file in search.search_words(words):
            catalogue_logger.logger.debug(f"Copying file {file} in {dest_path}")
            shutil.copy(file, dest_path)


    if command == "most_common":
        for k,v in search.get_most_common(n):
            print(f"{k} {v}")
