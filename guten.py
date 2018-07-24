from collections import Counter
import random

top100Words = [ "the", "of", "to", "and", "a", "in", "is", "it",
"you","that","he","was","for","on","are",
"with","as",
"I","his",
"they",
"be",
"at",
"one",
"have",
"this",
"from",
"or",
"had","by","hot",
"word","but",
"what",
"some",
"we",
"can",
"out",
"other","were",
"all","there",
"when","up",
"use","your",
"how","said",
"an","each",
"she","which",
"do","their",
"time","if",
"will",
"way",
"about",
"many",
"then",
"them",
"write",
"would",
"like",
"so",
"these",
"her",
"long",
"make",
"thing",
"see",
"him",
"two",
"has",
"look",
"more",
"day",
"could",
"go",
"come",
"did",
"number",
"sound",
"no",
"most",
"people",
"my",
"over",
"know",
"water",
"than",
"call",
"first",
"who",
"may",
"down",
"side",
"been",
"now",
"find"
]

def getTotalUniqueWords(file):

    wordCount = Counter(file.read().split())
    totalUniqueWords = len(wordCount)

    print totalUniqueWords
    return totalUniqueWords

def getTotalNumberOfWords(file):

    totalNumberOfWords = 0

    for word in file.read().split():
        totalNumberOfWords += 1

    print totalNumberOfWords
    return totalNumberOfWords

def get20MostFrequentWords(file):

    mostFrequentWords = Counter(file.read().split()).most_common(20)

    print mostFrequentWords
    return mostFrequentWords

def get20MostInterestingFrequentWords(file):

    mostFrequentWords = Counter(file.read().split())
    counter = 0

    for word, frequency in mostFrequentWords.most_common():

        if word != "I":
            word = word.lower()

        if word not in top100Words:
            print word, frequency
            counter += 1

        elif counter >= 20:
            break

#does not account for punctuation
def get20LeastFrequentWords(file):

    leastFrequentWords = Counter(file.read().split()).most_common()
    counter = 0

    for word, freq in reversed(leastFrequentWords):
        if counter >= 20:
            break

        counter += 1
        print word, freq

def getFrequencyOfWord(file, word):

    wordInChapterCount = 0
    list = []

    for line in file:
        if "CHAPTER" in line:
            list.append(wordInChapterCount)
            wordInChapterCount = 0

        elif word in line:
            wordInChapterCount += 1

    list.append(wordInChapterCount)
    list.remove(0)

    print list


def getChapterQuoteAppears(file, quote):

    chapterCount = 0

    for line in file:
        if "CHAPTER" in line:
            chapterCount += 1


        elif quote in line:
            print chapterCount
            return chapterCount


    print "-1"
    return -1

def removePunctuations(word):

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in word:
        if char in punctuations:
            word = word.replace(char, "")

    if word != "I":
        return word.lower()

    return word

def generateSentence(file):

    wordsAfterCurrentWord = []
    getNextWord = False

    sentence = "The"
    currentWord = "the"

    for i in range(20):

        for word in file.read().split():

            word = removePunctuations(word)
            if word.lower() == currentWord:
                getNextWord = True

            elif getNextWord:
                wordsAfterCurrentWord.append(word)
                getNextWord = False

        file.seek(0)
        currentWord = random.choice(wordsAfterCurrentWord)
        sentence += " " + currentWord
        del wordsAfterCurrentWord[:]
        getNextWord = False

    print sentence + "."
    return sentence + "."

def main():

    # file = open("gullivers.txt", "r")
    # getTotalUniqueWords(file)
    #
    # file = open("gullivers.txt", "r")
    # getTotalNumberOfWords(file)
    #
    # file = open("gullivers.txt", "r")
    # get20MostFrequentWords(file)

    # file = open("gullivers.txt", "r")
    # get20MostInterestingFrequentWords(file)

    # file = open("gullivers.txt", "r")
    # get20LeastFrequentWords(file)

    # file = open("gullivers.txt", "r")
    # getFrequencyOfWord(file, "")

    # file = open("gullivers.txt", "r")
    # getChapterQuoteAppears(file, "Undoubtedly philosophers")

    file = open("gullivers.txt", "r")
    generateSentence(file)


if __name__ == "__main__":
    main()
