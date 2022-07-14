import array

# initialized an array with array values and signed integer.
arr = array.array('i',[1,2,3,4,5])

# Printing original array.
print("The new created array is :",end=" ")
for i in range(0,5):
    print(arr[i],end=" ")

print("\n")

# using append() method to insert new value at end.
arr.append(6)
print("The appended array is :",end=" ")
for i in range(0,6):
    print(arr[i],end=" ")

# Using insert() to insert value at specific position
# insert 11 at 2nd position
arr.insert(2,11)

print("\r")

print ("The array after insertion is : ", end="")
for i in range (0, 7):
    print (arr[i], end=" ")
print("\n")
# Using pop() to remove element at 2nd position
print("The popped element is :",end="")
print(arr.pop(2))

# Printing array after popping
print("The array after popping is :", end="")
for i in range (0,6):
    print(arr[i],end=" ")
print("\r")
# using remove() to remove 1st occurrence of 1
arr.remove(1)

# printing array after removing
print("The array after removing is : ", end="")
for i in range(0, 5):
    print(arr[i], end=" ")

print("\n")

# using index() to print index of 1st occurrence of 2
print("The index of 1st occurrence of 3 is : ", end="")
print(arr.index(3))

# using reverse() to reverse the array
arr.reverse()

# printing array after reversing
print("The array after reversing is : ", end="")
for i in range(0, 5):
    print(arr[i], end=" ")