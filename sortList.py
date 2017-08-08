number_List=["3","1"]
place=""
place = number_List[0]

def swap():
    if number_List[0] > number_List[1]:
        number_List[0] = number_List[1]
        number_List[1] = place

    if number_List[0] < number_List[1]:
        print(number_List)
#
# #variable "place" set as an empty varaible (place holder)
# #place holder set to 0th index and equals 1st index; makes [3,3]
# #1st index set to place holder, so it is changed to the 0th index
#
swap()
#

print("Bubble Sort Algorithm")

List = [78, 36, 120, 95, 20]
n = len(List)

def numbers():
    for j in range(n):
        for i in range(0, n-1):                                                 #"j" represents how many times function runs through list, "i" represents the last index from the pair that the loop is on
                                                                                #loop moves through list 5 times (0 to 4), swapping values until they are sorted
            if List[i] > List[i+1]:                                              #range is out of bounds when it reaches the last index, which does not have another index after it
                List[i], List[i+1] = List[i+1], List[i]

            print("List: ", List, "j: ", j, "i: ", i)

numbers()
