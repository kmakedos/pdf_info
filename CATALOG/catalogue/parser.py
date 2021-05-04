import argparse
import sys


class Parser:
    def __init__(self, logger, commands):
        self._logger = logger
        self._logger.debug("Parser Starting")
        self.default_parser = argparse.ArgumentParser(description="PDF Catalogue command line tool",
                                                      usage=sys.argv[0]+" ")
        self.default_parser.add_argument("command", choices=commands, help="Command")
        self.default_parser.add_argument("--folder", default=".")
        self.default_parser.add_argument("--n", help="n number of words", default=5)
        self.default_parser.add_argument("--dest", help="Destination path", default=None)
        self.default_parser.add_argument("--words", nargs=argparse.REMAINDER, default="")


    def parse_arguments(self):
        user_args = vars(self.default_parser.parse_args())
        command = user_args.pop("command")
        folder = user_args.pop("folder")
        n = int(user_args.pop("n"))
        dest_path = user_args.pop("dest")
        words = user_args.pop("words")
        self._logger.debug(f"Doing a {command} in {folder} with terms {words}")
        return command, folder, n, dest_path, words