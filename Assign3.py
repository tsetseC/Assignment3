#Answers for Assignment3 218029604 Tsetse CK
#python Assign3.py

#PROBLEM 1
#Given the string
s='fullstackslp'
#use the indexing to print out the following
#f
print(s[0])

#p
print(s[11])

#stack
print(s[4:9])

#slp
print(s[9:12])

#cks
print(s[7:10])

#reverse string
s = 'fullstackslp'[::-1]
print(s)

#PROBLEM2 LISTS
#Given this nested list:
l=[3,7,[5,[1,4,'hello']]]
#Reassign "hello" to be "goodbye"

l[2][1][2]='goodbye'
print(l)


#PROBLEM3 DICTIONARIES
#using keys and indexing, grab 'hello' from the following dictionaries

d1={'simple_key':'hello'}
print(d1['simple_key'])

d1={'k1':{'k2':'hello'}}
print(d1['k1']['k2'])

d1={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d1['k1'][0]['nest_key'][1])

#PROBLEM4 SETS
#use a set to find the unique values pf the list below

mylist=[1,1,1,1,1,2,2,2,2,3,3,3,3]
new_list=set(mylist)
print(new_list)

#PROBLEM 5 FORMATTING
#Given the variables
age=49
name="Kyle"

#use print formatting to print the following string
#Hello my name's dog is Kyle and he looks 45 years old

mystring="Hello my name's dog is {} and he looks {} years old".format(name,age)
print(mystring)