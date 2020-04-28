# from nltk.tokenize import sent_tokenize, word_tokenize


# example_text="hello Mr. abhinav , how are you . Today is a good day for learning nltk"

# print(sent_tokenize(example_text))
# print("--------------------------")
# print(word_tokenize(example_text))
# -----------------------------------------------------------------------

# stop words
# from nltk.corpus import stopwords
# stop_words=set(stopwords.words("english"))
# # print(stop_words)
# #filtering words
# words=word_tokenize(example_text)
# filtered=[]
# for w in words:
# 	if w  not in stop_words:
# 		filtered.append(w)
# print(filtered)

# ----------------------------------------------------

# stemming ,, removing the ing parts , like ride and riding 
# from nltk.stem import PorterStemmer
# ps=PorterStemmer()
# text=word_tokenize(example_text)
# for w in text:
# 	print(ps.stem(w))
# -------------------------------------------------

# speach tagging
# import nltk
# from nltk.corpus import state_union
# from nltk.tokenize import PunktSentenceTokenizer       # this is  areinforment learning sentence tokeniser which is already trained  but if we want we can train it

# train_text= state_union.raw("2005-GWBush.txt")
# sample_text=state_union.raw("2006-GWBush.txt")
# custom_sent_tokenizer=PunktSentenceTokenizer(train_text)
# tokenized=custom_sent_tokenizer.tokenize(sample_text)
# # print(train_text)
# def process_content():
# 	try:
# 		for i in tokenized:
# 			words=nltk.word_tokenize(i)
# 			tagged=nltk.pos_tag(words)
# 			print(tagged)
# 	except Exception as e:
# 		print(str(e))


# process_content()

#chunking ,, this is used to get nowns and adverbs in a speech..
#very imapotant in indentifying names
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer       # this is  areinforment learning sentence tokeniser which is already trained  but if we want we can train it

train_text= state_union.raw("2005-GWBush.txt")
sample_text=state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer=PunktSentenceTokenizer(train_text)
tokenized=custom_sent_tokenizer.tokenize(sample_text)
# print(train_text)
def process_content():
	try:
		for i in tokenized:
			words=nltk.word_tokenize(i)
			tagged=nltk.pos_tag(words)

			#chunking
			chunkGram=r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""

			chunkParser=nltk.RegexParser(chunkGram)

			chunked=chunkParser.parse(tagged)

			chunked.draw()

			# print(tagged)
	except Exception as e:
		print(str(e))



