from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def secret(request):
    return render(request, 'secrets.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            #Increase word count
            worddictionary[word] +=1
        else:
            #Add word to dictionary
            worddictionary[word]=1

    sortedWord = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist), 'sortedWords':sortedWord})
