St = 'Print only the words that start with s in this sentence'
stringlist = St.split()
for items in stringlist:
    if items[0].lower()=='s': #case insensitive search
        print(f'The word "{items}" starts with the character s')
    else:
        print(f'The word "{items}" does not start with the character s')

#Print numbers in range
for item in range(0,11):
    print(f'The current number is {item}')

#list comprehension of numbers divisible by 3

mylist=[]
for item in range(0,51):
    if item%3==0:
         mylist.append(item)
print(mylist)

#method 2
mylist=[]
mylist=[item for item in range(0,51) if item%3==0]
print(mylist)

#check length of word in string
str='Print every word in this sentence that has an even number of letters'
strlist=str.split()
for word in strlist:
    if len(word)%2==0:
        print(f'The length of the word "{word}" is {len(word)} characters and is even')

#print words for numbers
for number in range(1,101):
    if(number%3==0 and number%5==0): #if a number is a multiple of 3 and 5 it will be a multiple of 3, so logically we need to check for 3 and 5 so as to not tag the wrong string
        print('FizzBuzz')
    elif (number%5==0):
        print('Buzz')
    elif (number%3==0):
        print('Fizz')
    else:
        print('The number is not divisible by either 3 or 5')

#print first characters of each string
St = 'Create a list of first letters of every word in this string'
newlist=[]
listindex=0
stringlist = St.split()
for items in stringlist:
    newlist.append(items[0])
    print(f'The word "{items}" starts with the character "{newlist[listindex]}"')
    listindex+=1

#method 2
[word[0] for word in St.split()]