#!/usr/bin/env python
import sys
import word_counter

if __name__ == '__main__':

    if len(sys.argv)<2:
        print("podaj nazwe pliku")
        sys.exit(0)

    filename=sys.argv[1]
    print("Wybrano plik: "+filename)

    file= open(filename,'r')
    content=file.read()
    number_of_words= word_counter.WordCounter(content)
    number= number_of_words.count()
    print("Liczba wyrazow: "+str(number))
