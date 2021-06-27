from django.shortcuts import render

def home(request):
    render(request, "home.html")

def result(request):
    sentence = request.Get['sentence']
    wordList = sentence.split()

    wordDict = {}

    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    render(request, "result.html", {'fulltext':sentence, 'count' : len(wordList), "wordDict" : wordDict.items})