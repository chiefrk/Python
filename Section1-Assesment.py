#Numbers - ordered sequence of numbers, int and float
#Strings - ordered sequence of characters
#Lists - ordered sequence of objects, can be sorted
#Dictionary - key value pairs, no sorting
#tuples - like lists however does not allow duplication, immutable
lab1=((5*5)+(5**2)+(800/10)-30)+(1/4) #** indicates power of not ^
print(lab1)
#q3 44, 29, 34
#q4 8.5
#q5 square root in python is **.5, square is represented as **
q5=4**.5
#q6 s[1]
#q7 s[-1], s[4]
#q8
q8=[]
q8.append(0)
q8.append(0)
q8.append(0)
print(q8)
q8_m2=[]
q8_m2.insert(0,0)
q8_m2.insert(1,0)
q8_m2.insert(2,0)
print(q8_m2)
q8_m3=[0]*3
print(q8_m3)
#q9
list3 = [1,2,[3,4,'hello']]
a=list3[2]
a[2]='goodbye'
list3.pop()
list3.append(a)
print(list3)
#or more efficient method
list3[2][2]='goodbye'
print(list3)
#q10
list4 = [5,3,4,6,1]
list4.sort()
print(list4)
#or another option
sorted(list4)
print(list4)
#q11
d = {'simple_key':'hello'}
op=d['simple_key']
print(op)
d = {'k1':{'k2':'hello'}}
op_1=d['k1']
print(op_1)
op_1=op_1['k2']
print(op_1)
#or more efficient method
print(d['k1']['k2'])
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
op_2=d['k1']
print(op_2)
op_2=op_2.pop()
print(op_2)
op_2=op_2['nest_key']
print(op_2)
op_2=op_2[1]
op_2=op_2[0]
print(op_2)
#or a more efficient method
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
op_5=d['k1'][0]['nest_key'][1][0]
print(f'the output of the string is {op_5}')
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
op_3=d['k1']
print(op_3)
op_3=op_3.pop()
print(op_3)
op_3=op_3['k2']
op_3=op_3.pop()
print(op_3)
op_3=op_3['tough']
op_3=op_3.pop()
op_3=op_3[0]
print(op_3)
#much more effect method is 
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
op_6=d['k1'][2]['k2'][1]['tough'][2][0]
print(f'The string ouput of the single expression is {op_6}')
#dictionaries cannot be sorted as they are based on key value pair, they are mappings and not a sequence
#q12 tuples are immutable t=(1,2,3), tuples allow duplication
#create sets using the set function
mylist=[1,2,3,4,4,5,5]
tup=set(mylist)
print(tup)
#q13
#false, false, false, true, false, false