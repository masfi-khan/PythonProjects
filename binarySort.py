List = [1,5, 6, 10, 11, 17, 20, 34, 38, 58, 100, 400]
x = input("Choose a number.")

def binarySort(List, x):
    n = len(List)
    start = 0
    end = n-1
# while x > 0:
    mdpt = (start + end) / 2
    if str(x) > List[mdpt]:
        mdpt2 = (List[start] + List[mdpt]) / 2
    if str(x) < List[mdpt]:
            mdpt3 = (List[mdpt] + List[end]) / 2
    if x == mdpt3:   #check input in list
        print("Yes, that number is in the list!")
    else:
        print("Nope, not here!")

binarySort(List, x)
