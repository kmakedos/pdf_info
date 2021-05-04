import catalogue.log
from catalogue import search_pdf, log, database

logger = log.Logger("test.log")


def test_catalogue():
    c = search_pdf.Search("/data/NEWSTRUCTURE/EBOOKS", logger=logger.logger)
    assert c is not None
    assert c.get_catalogue() is not None
    assert len(c.get_catalogue()) > 0


def test_search_multiple_words():
    c = search_pdf.Search("/data/NEWSTRUCTURE/EBOOKS", logger=logger.logger)
    assert c is not None
    result = c.search_words({"Python","Programming"})
    assert len(result) > 0


def test_search_most_common():
    c = search_pdf.Search("/data/NEWSTRUCTURE/EBOOKS", logger=logger.logger)
    assert c is not None
    result = c.get_most_common(n=5)
    assert len(result) > 0


def test_db():
    c = search_pdf.Search("/data/NEWSTRUCTURE/EBOOKS", logger=logger.logger)
    assert c is not None







