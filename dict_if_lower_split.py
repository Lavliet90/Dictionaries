#!/usr/bin/env python
# coding: utf-8

# In[ ]:


''''
When Anton read War and Peace, he wondered how many words and in what quantity are used in this book.
Help Anton write a simplified version of such a program that can count words separated by a space 
and display the resulting statistics.
The program should read one line from standard input and output for each unique word in this line 
the number of its repetitions (case-insensitive) in the "word number" format (see example output).
The order of output of words can be arbitrary, each unique word should be output only once.
''''
text=str(input())
mydict={}
for word in text.lower().split():
    if word in mydict:
        mydict[word]+=1
    else:
        mydict[word]=1
mydict1=str(mydict)
for key,value in mydict.items():
    print(key,value)

