#write conditions to iterate through a list and fetch odd numbers
i_list=[10,11,23,44,28,36,45,67,97,99,98,0.4]
for item in i_list:
    if item%2>0:
        print(f'The number {item} is an odd number')
    elif item%2==0:
        print(f'The number {item} is an even number')
dictionary={'k1':1,'k2':2,'k3':3,'k4':5,'k6':7,'k7':11}
for key,val in dictionary.items():
      print(f'The prime number is {val}')
#pass - filler for a loop without any condition, #continue - based on a condition will skip that iteration and move to the top of the loop, break - breaks the current iteration and also break the loop itself
x=0
while x==0:
    pass

while(x<11):
    x+=1
    if(x==2):
        continue
else:      
    print(x)
