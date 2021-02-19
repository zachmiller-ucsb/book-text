#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:08:27 2021

@author: zachary
"""
import os.path

def promptforfiles():
    val = 'x'
    files = []
    while not val.isspace():
        infilename = input('Enter a file to analyze: ')
        if os.path.isfile(infilename):
            files.append(infilename)
        else:
            print('File does not exist.')
        val = input('If this was the last file you wish to analyze, press spacebar. Otherwise press any letter key.')
    return files

def cleanup(master):
    cleanedup = []
    for en in master:
        cleanishstring = ''
        en = en.lower()
        for ch in en:
            if 'a' <= ch and ch <= 'z' or ch.isspace() or ch == '–' or ch == '-' or ch == '/' or ch == '\\':
                cleanishstring += ch
        cleanishlist = cleanishstring.split()
        cleanishlist1 = []
        for wordish in cleanishlist:
            wordishlist = wordish.split('–')
            for mostlyword in wordishlist:
                cleanishlist1.append(mostlyword)
        cleanishlist2 = []
        for almostword in cleanishlist1:
            wordlist = almostword.split('/')
            for word in wordlist:
                cleanishlist2.append(word)
        cleanedup += cleanishlist2
    return cleanedup

def countwords(listofwords):
    wordcounts = {}
    for word in listofwords:
        if word in wordcounts:
            wordcounts[word] += 1
        else:
            wordcounts[word] = 1
    return wordcounts

def countletters(listofwords):
    listofletters = []
    for word in listofwords:
        wordletters = [l for l in word]
        listofletters += wordletters
    lettercounts = {}
    for letter in listofletters:
        if letter in lettercounts:
            lettercounts[letter] += 1
        else:
            lettercounts[letter] = 1
    return lettercounts

def countbigrams(listofwords):
    listofbigrams = []
    for word in listofwords:
        wordbigrams = [word[i:i + 2] for i in range(len(word) - 2)]
        listofbigrams += wordbigrams
    bigramcounts = {}
    for bigram in listofbigrams:
        if bigram in bigramcounts:
            bigramcounts[bigram] += 1
        else:
            bigramcounts[bigram] = 1
    return bigramcounts

def counttrigrams(listofwords):
    listoftrigrams = []
    for word in listofwords:
        wordtrigrams = [word[i:i + 3] for i in range(len(word) - 3)]
        listoftrigrams += wordtrigrams
    trigramcounts = {}
    for trigram in listoftrigrams:
        if trigram in trigramcounts:
            trigramcounts[trigram] += 1
        else:
            trigramcounts[trigram] = 1
    return trigramcounts

def sortthedict(stats):
    tuples = [(v,k) for k, v in stats.items()]
    tuples.sort(reverse=True)
    tuples2 = [(k,v) for v, k in tuples]
    sorteddict = dict(tuples2)
    return sorteddict

def aggstatswords(master):
    copy = cleanup(master)
    wordstats = sortthedict(countwords(copy))
    numberwords = sum(wordstats.values())
    for k in wordstats:
        wordstats[k] /= numberwords
    return wordstats

def aggstatsletters(master):
    copy = cleanup(master)
    letterstats = sortthedict(countbigrams(copy))
    numberletters = sum(letterstats.values())
    for k in letterstats:
        letterstats[k] /= numberletters
    return letterstats

def aggstatsbigrams(master):
    copy = cleanup(master)
    bigramstats = sortthedict(countbigrams(copy))
    numberbigrams = sum(bigramstats.values())
    for k in bigramstats:
        bigramstats[k] /= numberbigrams
    return bigramstats

def aggstatstrigrams(master):
    copy = cleanup(master)
    trigramstats = sortthedict(counttrigrams(copy))
    numbertrigrams = sum(trigramstats.values())
    for k in trigramstats:
        trigramstats[k] /= numbertrigrams
    return trigramstats

def analysis():
    files = promptforfiles()
    words = {}
    letters = {}
    bigrams = {}
    trigrams = {}
    for f in files:
        openf = open('infile','r')
        master = openf.readlines()
        words[f] = aggstatswords(master)
        letters[f] = aggstatsletters(master)
        bigrams[f] = aggstatsbigrams(master)
        trigrams[f] = aggstatstrigrams(master)
    return [words,letters,bigrams,trigrams]

#mr = ['I like to eat \n','meat-pies, corn–roast/chicken, \n','and your mom\'s kugel']
#sortthedict(countwords(cleanup(mr)))
