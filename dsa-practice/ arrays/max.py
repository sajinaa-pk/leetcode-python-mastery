

def tofindMax(arr):
    for i in range(len(arr)):
        if i == 0:
            max = arr[i]
        elif arr[i] > max:
            max = arr[i]
    # print("Max:", max)
                                     
# tofindMax([10,20,30])


def tofindMax(arr):
    if not arr:  # Handle empty array
        return None
    
    max_val = arr[0]  # Initialize with first element
    for i in range(1, len(arr)):  # Start from second element
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val  # Return instead of print (more flexible)

# print("Max:", tofindMax([10, 20, 30]))


def torevers(arr):
    if not arr:
        return None    
    new_list=[]
    for i in range(len(arr)-1,-1,-1):
       new_list.append(arr[i])
    print(new_list)
              
torevers([5,6])
    
# def reverse_forward(arr):
#     new_list = []
#     for i in range(len(arr)):
#         # Access elements from the end moving forward
#         new_list.append(arr[len(arr) - 1 - i])
#     return new_list

