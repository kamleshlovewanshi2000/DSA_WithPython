"""
# Method - I

def rotateArray(L,d,n):
    k = L.index(d)
    new_list = []
    new_list = L[k+1:] + L[0:k+1]
    return new_list

d = 2
n = 7
L = [1,2,3,4,5,6,7]
print(rotateArray(L,d,n))

# Time complexity : O(n)
# Auxiliary Space : O(n)
"""

# Method - II

def leftRotate(arr,d,n):
    d = d%n
    g_c_d = gcd(d,n)
    for i in range(g_c_d):
        # move i-th value of blocks
        temp = arr[i]
        j = i
        while True:
            k = j+d
            if k>=n:
                k = k-n
            if k==i:
                break
            arr[j] = arr[k]
            j = k
            arr[j] = temp
# Utility Function
# Function to print an array
def printArray(arr,size):
    for i in range(size):
        print("% d" % arr[i], end=" ")

# Function to get gcd of a and b
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

# Driver Code
arr = [1,2,3,4,5,6,7]
n = len(arr)
d = 2
leftRotate(arr,d,n)
printArray(arr,n)



