import nltk

def wordcloud(text):
    num = 3
    words = nltk.tokenize.word_tokenize(text)
    stopwords = nltk.corpus.stopwords.words('english')
    wordDist = nltk.FreqDist(w.lower() for w in words if w not in stopwords)
    return(wordDist.most_common(num))
print(wordcloud('hello hello world'))