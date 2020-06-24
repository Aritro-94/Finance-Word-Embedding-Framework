# -*- coding: utf-8 -*-
"""Github_upload.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Oh98mHJ8u1vD9kpwsrEHd9hP54TZDSZY
"""

# Imports
import numpy as np
import spacy
import nltk
nltk.download("punkt")
nltk.download("words")
nltk.download("stopwords")
from nltk.tokenize import word_tokenize,sent_tokenize

# !pip install glove_python
from glove import Corpus,Glove

## Creating the Corpus

list_of_books1=["Introduction to Structured Finance","The Handbook of Financial Instruments","Accounting - ACC110016","Bodie, Kane _ Marcus - Investments","Finance - I","Finance II","Financial Accounting","McGraw.Hill.Accounting.For.Managers","George Soros - The New Paradigm for Financial Markets","Liaquat Ahamed - Lords of Finance","The Intelligent Investor","Investment Banking_ Valuation, Leveraged Buyouts, and Mergers and Acquisitions"]
list_of_books2=["Barbarians at the Gate","Common Sense on Mutual Funds","Extraordinary Popular Delusions and the Madness of Crowds","Fundamentals of Corporate Finance","Guide to Financial Management","International corporate finance","Investment Leadership and Portfolio Management","Investment Management","Lessons in Corporate Finance","Liar's Poker","Mastering Market Timing","Mergers and acquisitions in banking and finance","Random Walk Down Wall Street","Reducing the Risk of Black Swans","Strategy, Value and Risk","The Alchemy of Finance","The Little Book of Behavioral Investing","Venture Capital and the Finance of Innovation"]

list_of_books=list_of_books1+list_of_books2

## The files are being read,
## Named Entity is being removed here, 
## and after that text is being stored

nlp=spacy.load('en_core_web_sm')
nlp.max_length=4000000 #4M

text_data=[]
for i in range(len(list_of_books)):
    dire="/content/gdrive/My Drive/Glove Project/{}.txt".format(list_of_books[i])
    with open(dire, 'r') as file:
      text=file.read().replace('\n', ' ')
      doc=nlp(text)
      book=[]
      ents=[e.text for e in doc.ents]
      for item in doc:
        if item.text in ents:
          pass
        else:
          book.append(item.text)
      book_text=" ".join([sent for sent in book]) 
      sent_list=sent_tokenize(book_text)
      word_in_sent_list=[word_tokenize(sent) for sent in sent_list]
      file.close()

    text_data.append(word_in_sent_list)

## "text_data" which is the output is in the format of nested list, 1st level nest is the book number,
## 2nd level nest is a sentence in the book, 3rd level nest is a word in the sentence of the book.

## Pre-Processing Steps

## Defining Functions 

# This function lower cases the corpus
def lower(sup_cor):
  clean_sup_cor=[]
  for sent in sup_cor:
      n_sent=[]
      for x in sent:
          y=x.strip().lower()
          n_sent.append(y)
      clean_sup_cor.append(n_sent)    
  return(clean_sup_cor)

# This corpus removes non english words  

def remove_non_eng_words(clean_sup_cor):
  import nltk
  lexicon=nltk.corpus.words.words()
  lex=[]
  for word in lexicon:
    lex.append(word.lower())
  lex_set=set(lex)
  clean_cor=[]
  for sent in clean_sup_cor:
    n_sent=[]
    null=[]
    for word in sent:
      if word in lex_set:
        n_sent.append(word)
      else:
        null.append(word)

    clean_cor.append(n_sent)
  return(clean_cor)


# This function removes stop- words
def remove_stopword(clean_cor):
  from nltk.corpus import stopwords
  stop_list=stopwords.words("english")
  stop_list.remove("it")
  stop_list=stop_list+["therefore","thus","since","usually","often","hence","chapter","part","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
  stop_set=set(stop_list)
  fin_cor=[]
  for sent in clean_cor:
      n_sent=[]
      for word in sent:
          if word not in stop_set:
              n_sent.append(word)
      fin_cor.append(n_sent)
  return(fin_cor)

# removing special characters
puncts = [',', '.', '"', ':', ')', '(', '-', '!', '?', '|', ';', "'", '$', '&', '/', '[', ']', '>', '%', '=', '#', '*', '+', '\\', '•',  '~', '@', '£', 
 '·', '_', '{', '}', '©', '^', '®', '`',  '<', '→', '°', '€', '™', '›',  '♥', '←', '×', '§', '″', '′', 'Â', '█', '½', 'à', '…', 
 '“', '★', '”', '–', '●', 'â', '►', '−', '¢', '²', '¬', '░', '¶', '↑', '±', '¿', '▾', '═', '¦', '║', '―', '¥', '▓', '—', '‹', '─', 
 '▒', '：', '¼', '⊕', '▼', '▪', '†', '■', '’', '▀', '¨', '▄', '♫', '☆', 'é', '¯', '♦', '¤', '▲', 'è', '¸', '¾', 'Ã', '⋅', '‘', '∞', 
 '∙', '）', '↓', '、', '│', '（', '»', '，', '♪', '╩', '╚', '³', '・', '╦', '╣', '╔', '╗', '▬', '❤', 'ï', 'Ø', '¹', '≤', '‡', '√', ]

def space_text(x):
    x = str(x)
    for punct in puncts:
        if punct in x:
            y = x.replace(punct, f' {punct} ')
            y=x.split(" ")
        else:
            y=x
    return y



def clean_sent(l):
    lc=[]    
    for i in l:
        if i.isalpha():
            lc.append(i)
        else:
            lis=space_text(i)
            for x in lis:
                lc.append(x)
    return lc    

def space_text1(fin_cor):
  clean_flat_sup_cor=[]
  for sent in fin_cor:
      n_sent=clean_sent(sent)
      clean_flat_sup_cor.append(n_sent)
  return(clean_flat_sup_cor)


# This function removes numbers and special characters
def is_alpha(clean_flat_sup_cor):
  clean_cor=[]
  for sent in clean_flat_sup_cor:
      n_sent=[]
      for word in sent:
          if word.isalpha():
              n_sent.append(word)
      clean_cor.append(n_sent)   
  return(clean_cor)    


# This function removes null lists, as at the end some sentences loose all the words after pre-processing.
def is_blank(clean_cor):
  fin=[]
  for i in clean_cor:
      if (i!=[]):
        fin.append(i)
  return(fin)

# flattening the text_data
corpus=[]
for i in data:
  # i is a book
  for j in i:
    #j is a sentence
    corpus.append(j)
 
## "corpus" is in the desired format here, which is list of lists.
## Eg: [["good","morning"],["how","are","you"]]


## Applying the pre-processing functions
fin=is_blank(is_alpha(space_text1(remove_stopword(remove_non_eng_words(lower(corpus))))))

## Initiating the co-occurrence matrix
cor=Corpus()
## Filling up co-occurence matrix with appropriate count values
cor.fit(fin,window=3)

## Creating the Glove object
glove=Glove(no_components=100,learning_rate=0.01)
glove.fit(cor.matrix,epochs=10,verbose=False)
glove.add_dictionary(cor.dictionary)

word_list=list(glove.dictionary.keys())

embed_dic={}
for i in range(len(word_list)):
  embed_dic[word_list[i]]=glove.word_vectors[i]

## Here "embed_dic" is the word_embedding framework stored in dictionary format
## Keys -> words , Values -> Vector the word corresponds to 
## To check the content of the dictionary 
## print(embed_dic["credit"])

## Defining Functions to obtain top similar/ dissimilar words

## returns the cosine similarilty value
def cos_sim(u,v,embed_dic):
    vec1=embed_dic[str(u)]
    vec2=embed_dic[str(v)]
    num=vec1.dot(vec2)
    den=np.sqrt(sum(np.square(vec1))*sum(np.square(vec2)))
    return(float(num)/den)

## returns the dictionary of cosine similarity with every other word
def cos_sim_dic(word,embed_dic):
    word_list=list(embed_dic.keys())
    dic={}
    for i in range(len(word_list)):
        dic[word_list[i]]=cos_sim(word,word_list[i],embed_dic)
    return (dic)

## returns the dictionary of words with cosine similarities above a percentile 
def top_list(word,percentile,embed_dic):
    dic=cos_sim_dic(word,embed_dic)
    words=list(dic.keys())
    arr=[]
    items=list(dic.items())
    for i in range(len(words)):
        arr.append(items[i][1])
    thres=np.percentile(arr,float(percentile),axis=None)
    top={}
    for i in range(len(arr)):
        if (arr[i]>=thres):
            top[words[i]]=arr[i]
    return(top)            

## returns the dictionary of words with cosine similarities below a percentile
def bottom_list(word,percentile,embed_dic):
    dic=cos_sim_dic(word)
    words=list(dic.keys())
    arr=[]
    items=list(dic.items())
    for i in range(len(words)):
        arr.append(items[i][1])
    thres=np.percentile(arr,float(100-percentile),axis=None)
    bot={}
    for i in range(len(arr)):
        if (arr[i]<=thres):
            bot[words[i]]=arr[i]
    return(bot)  

# print(top_list("credit",99.9,embed_dic))

## saving the word embedding framework
file=open("/content/gdrive/My Drive/Glove Project/embedding_dictionary.txt","wb")
pickle.dump(embed_dic,file)
file.close()

# To load the pickle file
# file=open("/content/gdrive/My Drive/Glove Project/embedding_dictionary.txt","rb")
# embed_dic=pickle.load(file)
# file.close()
