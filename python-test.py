print ("hello world")
a="hello world"
a=a.upper()
#check length of the string
b=len(a)
#get the first character from the string
c=a[0]
#get the last character from the string
d=a[-1]
print (b)
print (c)
print (d)
#reverse the string and remove the last word from the string, the output will be olleh
e=a[len(a)-7::-1]
#reverse the string
print(e[::-1])
#Useful to split a string
print(a.rsplit())
#string formatting
str1='quick'
str2='brown'
str3='fox'
print(f'The {str1} {str2} {str3}')
#float formatting
flt=121/119
print('The float is {f:1.2f}'.format(f=flt))
#dictionary value reassignment
dic={'key1':1, 'key2':'String'}
print(dic['key1'])
dic['key1']='Sunday'
print(dic['key1'])
#to eliminate duplicates in a list cast it to a set, set is an unordered list of unique value
mylist = [1,1,2,1,2,3,3,2,2,1]
print (f'the list with duplicate values is  {mylist}')
set_mylist=set(mylist)
print(f'The list which was convereted to a set is {set_mylist}')