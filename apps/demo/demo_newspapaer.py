from newspaper import Article

url = "https://beecode.ljlx.com/competition/competition.html"
article = Article(url)
article.download()
article.parse()
print(article.text)
print(article.nlp())
