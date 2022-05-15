words = ['hello', 'world', 'spam', 'eggs']
for word in words:
    print(word + "!")
#just a comment to say nothing
str='testing for loop'
count=0
for x in  str:
    if (x=='t'):
        count +=1
print(count)
#print no of t found in the given string
letters=['a','b','c']
for a in letters:
    print(a)
#print the list simply
a = list (range(10,20))
print (a)
#range
a= list(range(1,67,6))
print (a)
for i in range (6):
    print("jelly")
#range in loop yaaay
#let's go to the slices now how cool is that
#remember your first interview question hahhhaha
a= [0,1,2,3,4,5,6,7,8,9,10,11,12]
print(a[:3])
print(a[2:4])
print(a[1:6:2])
print(a[:-1])
print(a[:-0])
print(a[::-1])
#example of recursion fffffffffffffff
print(a[::2])

list= [1,1,2,3,5,8,13]
print(list[list[4]])
#double list omg
for i in range (20):
    if not i%2==0:
        print(i+1)
        #table of 2 or even number from 0 to 20
#sum of n numbers
N = int(input())
a = sum (range(0 , N+1))
print(a)
nums = [1,2,3]
nums.append(4)
print(nums)
#an example of function

print('hello me'.replace("me",'world'))
print("spam, eggs, ham".split())
#now go deeper
text= input()
word= input()
def search(text,word):
    if word in text:
        return('word found')
    else:
        return('word not found')
print(search(text,word))
#chotta google
str=input()
count = 0
for x in str:
    if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
        count+=1
print(count)
#vowel checker
str= input()
inp= input()
inpl=int(str.count(inp))
print(inpl)
#letter count in str
x= [2,4,6,8]
x.reverse()
print(x)
x.sort()
print(x)
print(min(x))
print(max(x))
#list functions up
# list comprehensions down

cubes = [i**3 for i in range(5)]
print(cubes)
#can contain if too
sqs =[i**2 for i in range (10) if i%2==0]
print(sqs)
#abs return absolute value like abs(-2) = 2
#now let's move to the dictonaries
#key:value pair
#use of get fn - same as indexing but returns another value if key not found
a={1:23,
   'apple':'orange',
   3:"hello world",
   9:'suprise ft doakes'}
print(a.get(1,'ok'))
print(a.get(7,'l'))
print(a.get('orange')) # coz it's vlaue not key
print(a.get(12345,'not found'))
#let's go to tuples now
#ah wait remember - dict{ list[ tuples (  gotcha newbie!!
words =( 'hello','ok','bye')
print(words)
#tuple unpacking simplest
a=(2,5,6)
b,c,d = a
print(b)
print(c)
print(d)
#args or *c whaterver ykr
#a,b,*c,d and the list is 1,2,3,4,5,6,7,8 then c will took 3-7
a,b,*c,d=[1,2,3,4,5,6,7,8,9,10]
print(a)
print(b)
print(c)
print(d)
#operators union | intersection &  diff -(a-b items in a but not in b) symm diff ^(a^b itmes in either but not both)
#userdefined ds
# stack lifo push pop is_empty
s=stack()
s.push(a)
s.push(b)
s.push(c) - ['c','b','a']
s.pop()  - ['b','a']
#queue - enqueue to back , dequeue remove from start fifoooooo
q=queue()
e=enqueue(1)
en(2)
en(3) -[3,2,1]
de()  -[3,2]
#ll  a= ll()
a.add_at_front(5)
a.add_at_end(8)
a.add_at_front(9)   - 9 => 5 => 8
print(a.get_last_node())  8
# numpy- numerical python..... mean avg of values , median middle value, std the measure of spread i.e
#how spread our data is
#numpy numpy arrays - ndarrays - n dimensional arrays
import numpy as np
x= np.array([1,2,3,4])
print(x[0])
#numpy arrays are homogenous i.e can contain single datatype atm
import numpy as np
x= np.array([2,6,4])
x=np.append(x,5)
x= np.delete(x,0)
x=np.sort(x)
print(x)
# array properties
import numpy  as np
x= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x.ndim) #no of dimensions
print(x.size) #no of elements in array
print(x.shape) #no of elements stored along each dim of the array

import numpy as np
x=np.arange(2,10,3) #create an array that contains arange of evenly spaced interals similar to range we read previous
print(x)
import numpy as np
x=np.arange(2,8,2)
x= np.append(x,x.size)
x=np.sort(x)
print(x[1])
print(len(x))
#reshape can change dimensions of arrays
import numpy as np
x= np.arange(1,7)
print(x)
z= x.reshape(3,2) #we changed 1d array to 3,2 here
print(z)
y=z.reshape(6)  # can also do opposite
print(y)
a=z.flatten() #same result as reshape yooooo
print(a)
#list slicing
import numpy as np
x=np.arange(1,10)
print(x)
print(x[0:2])
print(x[5:])
print(x[:2])
print(x[-3:])
print(x[::-1]) #reverse of a string
import numpy as np
x=np.arange(1,10)
print(x[(x>5)&(x%2==0)]) #nothing special just uding conditions
#stats with numpy is soo simple
import numpy as np
x=np.array([14,18,19,24,26,33,42,55,67])
print(np.mean(x))
print(np.median(x))
print(np.var(x)) #variance
print(np.std(x)) #standard daviation
#pandas ---- panel data
#primary comps - series and dataframe s- a coloum , d- multi D table made up of a collection of series
import pandas as pd
data = {
    'ages': [13, 15, 26, 42],
    'heights': [165, 180, 176, 185]
}
df = pd.DataFrame(data)
print(df)
#default indexing with 0,1,2 etc
import pandas as pd
data= {
    'ages' : [13,15,26,42],
    'heights' : [146,167,185,178],
    'a':['lol']
}
df = pd.DataFrame(data, index=['James', 'bob', 'amy', 'dave']) #customized indexing
print(df)
print(df.loc["bob"])  #cam access a row using it's index using loc function
print(df['ages'])   #can select a single  column
#for multiple columns use -
print(df[['ages','heights']])
import pandas as pd
data= {
    'ages' : [13,15,26,42],
    'heights' : [146,167,185,176]
}
df = pd.DataFrame(data, index=['James', 'bob', 'amy', 'dave']) #customized indexing
print(df)
print(df.iloc[2])
print(df.iloc[:3])
print(df.iloc[1:3])  #iloc same as slicing in python lists
print(df[(df['ages']>18)&(df['heights']>180)])

#functional programming- higher order function=> take other functions as arguments or return them as results
#like f(g(x))
def a(func,arg):
    return func(func(arg))
def b(x):
    return x+5
print(a(b,10))
#lambdas - anonymous function
def a(f,arg):
    return f(arg)
print(a(lambda x:2*x+x,5)) #it's lambda not ....
print((lambda x:x**2+5*x+4)(-4)) #it's simple btc

#maps and filter=> higher order fn , operates on lists or other iterables
#map takes a fn and an iterable as arg, and returns a new iterable with the fn applied to each arg
def a(x):
    return x+5
nums =[11,22,33,44,55]
result = list(map(a,nums))
print(result)
#can get same easily with lambda
nums=[11,22,33,44,55]
result=list(map(lambda x:x+5,nums))
print(result)
#filter -- filters an iterable by leaving only the items that match a condition
nums=[11,22,33,44,55]
res=list(filter(lambda x:x%2==0,nums))
print(res)
#extract all items<5
nums = [1,2,5,8,3,0,7]
r= list(filter(lambda x:x<5,nums))
print(r)
#gnerators - type of iterables, generated using fn and the yield statement
def countd():
    i=5
    while i>0:
        yield i
        i-=1
for i in countd():
    print(i)
#generators don't have memory restrictions i.e. can be infinite
def a():
    while True:
        yield 7
for i in a():
    print(i) #infinite loop
def m():
    word= ''
    for ch in "spam":
        word += ch
        yield word
print(list(m()))  #yield save every move hehheheh
#decorators your interview que ****
#decs - fns that modify other fns
#just an example of fn
def func():
    print("helloooo")
func2 = func
del func    #either delete or not ans will same coz once done is done
func2()
def funcr(num):
    if num==0:
        return print
    if num ==1:
        return sum
a= funcr(1)
print(a) #print sum in 1 and print in 0 isn't that cool ?
#here comes decorator
def decor(b):
    def a():
        print("executing now")
        b()
        print("executed")
    return a
def c():
    print ("hello world")
c= decor(c)
c()
#random password generator
import random
l="abcdefghijklmnopqrstuvwxyz"
u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n="0123456789"
s="[]{}#()*;._-"
all=l+u+n+s
length=9
password="".join(random.sample(all,length))
print("Here's your new password:",password)
x = ['p','y','t','h','o','n']
for i in enumerate(x):
    print(i,end="")
#just some quiz ques
a = {'x':1, 'y':2, 'z':3}
for i,j in a.items():
    print(i,j,end="")
#another que
x= ['p','y','t','h','o','n']
y= ['1','2','3','4','5','6']
for i in zip(x,y):
    print(i,end="")
#let's run another one
from random import*
x= [0,2,4,6,8,10]
print(sample(x,5))
#list containing 5 random elements from list x
from random import*
print(sample(range(0,9),5))
#list containg 5 random nos
import sys
print(sys.version)
#print python version
import sys
print(sys.executable)
#print the location of python on comppuuuuuter drives
import keyword
print(keyword.kwlist)
#print python keywords
import math
print(math.floor(100.2))
#floor value
import math
print(math.ceil(49.7))
import datetime
print(datetime.datetime.today())
#get  datetime row
from datetime import *
print(getattr(datetime.today(),'hour'))
#return  in hours
from datetime import*
print(datetime.today().strftime('%A')) #A- day B- month D- date c- ret the day , month ,year ,full time
x='python job ready'
print(x.title()) # caps in each word automatically
x='python'
y='job'
z='questions'
print(x.strip()+y.strip()+z.strip()) #add all together as str pythonjobquestion see no space
x='python'
print(x.center(10,'*'))
x='python'
print(x.find('p')) #print the pos or index of p
x='\n'
print(x.isspace()) #returns true why ?
a=[1,2,3,4,6,7,8,9,10,11,12,13,14]
print(a[1:5],a[3:17]) #print ll
a= True
b= False
print(a==b or not b)
a=[[0,1,2,3],[4,5,6,7],[8,9,10,11]]
b=[[x[i] for x in a] for i in range(4)]
print(b)
x=['a','b','c','d','1','2','3','A','B']
print(min(x)) # acc to me lowest are nums then small caps  then upp ones gotit?
#reading data CSV - comma separated values,,,,, read_csv() fn read data in pandas
import pandas as pd
df = pd.read_csv("C:/Users/ROHIT DUMKA/Desktop/covid.csv")
print(df.head()) #head by def only first 5 values use arg for limit . can use tails too by def last 5 values
# It's done finally oh yeahhhhhhhhhh!
import pandas as a
df = a.read_csv("C:/Users/ROHIT DUMKA/Desktop/covid.csv")
df.info()
#alright so we can set our own index too
df.set_index("Date", inplace= True)
print(df.head())
df.drop("State",axis=1,inplace=True) #drop delete rows and columns axis =1 delete column while axis =0 delete row
print(df.head())
#creating columns
import pandas as pd
df = pd.read_csv("C:/Users/ROHIT DUMKA/Desktop/covid.csv")
df.drop('State', axis=1, inplace=True)
df['month']= pd.to_datetime(df['Date'],format='%d-%m-%y').dt.month_name()
df.set_index('Date',inplace=True)
print(df.head())#here's an error will do later
import pandas as a

df = a.read_csv("C:/Users/ROHIT DUMKA/Desktop/covid.csv")
df.set_index("Date", inplace= True)
print(df.head())
df.drop("State",axis=1,inplace=True)
print(df.describe()) #returns the summary statistics for all the numeric columns like mean med var std etc
#so finally you managed to deal with csv files huh oh yeah bouy