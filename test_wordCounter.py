from unittest import TestCase


class TestWordCounter(TestCase):
    def test_split(self):
        self.listA=['I','m']
        self.strA='I m'
        self.assertEqual(self.listA,self.strA.split())
        #self.fail()

    def test_count(self):
        self.fail()
