# Python Program / Project

def Quick(arr, low, high):
    if low < high:
        m = partition(arr, low, high)
        Quick(arr, low, m-1)
        Quick(arr, m+1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    flag = False
    while(not flag):
        while(i<=j and arr[i]<=pivot):
            i = i+1
        while(i<=j and arr[j]>=pivot):
            j = j-1

        if(j<i):
            flag = True
        else:
            temp = arr[i]
            arr[i]= arr[j]
            arr[j] = temp
    temp = arr[low]
    arr[low] = arr[j]
    arr[j] = temp
    return j

n = int(input("Enter how many students in First Year: "))
arr = []
i = 0

for i in range(n):
    item = float(input("Enter percentage marks: "))
    arr.append(item)

print("You have entered following students percentage list: ")
print(arr)

print("The sorted percentage list usning Quick Sort is: ")
Quick(arr, 0, n-1)

print(arr)
print("Top five scores is: ")
for i in range(len(arr)-1, 1, -1):
    print(arr[i])
