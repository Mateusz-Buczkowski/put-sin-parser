from unittest import TestCase
from app.main import Parser


class TestParser(TestCase):
    def test_should_create_parser(self):
        parser = Parser()
