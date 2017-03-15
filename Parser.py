import re

class Parser(object):

    def __init__(self,content,path):
        self.content = content
        self.path = path

    def __str__(self):

        if not re.search("PrChecker.Downs", self.content):
            return "\n Nothing Find in file "+self.path
        else:
            return "\"PrChecker.Downs\" found in file "+self.path