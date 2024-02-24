
#methode1

from collections import Counter
sent=input("enter a string sentence:")
word_lower = sent.lower().split()
counter=Counter(word_lower)
print(counter)
#method2
sentence="hello programers i am rabia i am leraning python from sir owaise and other resources"
word_lower=sentence.lower().split()
dic={}
for i in word_lower:
    if i in word_lower:
        #dic[i] +=1 here is key error they does not initialize
        dic[i] = dic.get(i, 0) + 1
print(dic)

#method3
sentence=input("enter sentence: ")
word_lower=sentence.lower().split()
dic={}
for i in word_lower:
    if i in word_lower:
        dic[i]=+1
print(dic)
