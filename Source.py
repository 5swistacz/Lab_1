#!/usr/bin/env python
import re
import Parser

if __name__ == '__main__':

    file1 = open("../Logs/baseline_BdJPsiKs_MagD.log", 'r')
    file2 = open("../Logs/DR_BdJPsiKs_MagD_1k.log", 'r')
    file3 = open("../Logs/DR_NE_BdJPsiKs_MagD_1k.log", 'r')
    file4 = open("../Logs/DR_NE_BdJPsiKs_MagD.log", 'r')

    content1 = file1.read()
    content2 = file1.read()
    content3 = file1.read()
    content4 = file1.read()

    print("Looking for \"PrChecker.Downs\"")

    result1 = Parser.Parser(content1, "../Logs/baseline_BdJPsiKs_MagD.log")
    result2 = Parser.Parser(content2, "../Logs/DR_BdJPsiKs_MagD_1k.log")
    result3 = Parser.Parser(content3, "../Logs/DR_NE_BdJPsiKs_MagD_1k.log")
    result4 = Parser.Parser(content4, "../Logs/DR_NE_BdJPsiKs_MagD.log")

    print(result1)
    print(result2)
    print(result3)
    print(result4)
