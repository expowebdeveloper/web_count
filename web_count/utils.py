from collections import Counter
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

def most_common(data,n:int):
	tokens = tokenizer.tokenize(data)
	tokens = list(map(lambda a: a.lower(),tokens))
	word_count_dict = Counter(tokens)
	return dict(word_count_dict.most_common(n))