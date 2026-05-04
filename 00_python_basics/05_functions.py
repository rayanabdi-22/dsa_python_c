import random



def max_min(numbers):
 minimum = numbers[0]
 for num in numbers:
    if num < minimum:
        minimum = num
    #print(f"current min {minimum}")
    #print("Python 3")
 return minimum  

def getvalue():
    list = random.sample(range(50, 100),5)
    #list = {5,4,3,2,1}
    print(list)
    result =max_min(list)
    print(f"the value is {result}")

getvalue()