from unittest import TestCase
import Parser



class TestParser(TestCase):

    def test_input_stuff(self):
        content = 'some text'
        path = 'path in string format'
        parser = Parser.Parser(content,path)
        self.assertIsInstance(self,content,(str, unicode))
        self.assertIsInstance(self,path,(str, unicode))
