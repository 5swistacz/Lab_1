
class WordCounter(object):
    def __init__(self,text):
        self.text=text
    def split(self):
        self.list_of_words=self.text.split()
    def count(self):
        self.split()
        self.new_list=[x for x in self.list_of_words if x.isalnum()]
        self.new_list=[x for x in self.new_list if not x.isdigit()]
        self.number_of_words=len(self.new_list)
        return self.number_of_words