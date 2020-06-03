"""
i=[]
x=0
while x>=0:
    num = input("Enter a number: ")
    if num=="done": 
        break
    else:
        try:
            num1=int(num)
            print(i)
        except:
            print('Invalid input')
            print(i)
            continue
    i.insert(x,num1)
    x=x+1
largest=max[i]
smallest=min[i]  
print("Maximum", largest)
print("Minimum", smallest)
"""
largest = None
smallest = None
i=[]
x=0
while x>=0:
    num = input("Enter a number: ")
    try:
        num1=int(num)
    except:
        if num=='done':
            break
        else:
            print('Invalid input')
            continue
    i.insert(x,num1)
    x=x+1
largest=max(i)
smallest=min(i) 
print("Maximum is", largest)
print("Minimum is", smallest)
