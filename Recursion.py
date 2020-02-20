# To find sum of n natural number
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)

# To find the factorial of an integer
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

# To find nth fibonacci number
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

# To find sum of a list using slice
def sum_list(l):
    d = len(l)
    if d == 0:
        return 0
    else:
        return l[0] + sum_list(l[1:])

# To search for an element in a list using linear search
def linear_search(l, ele, pos=0):
    if pos == len(l):
        return None
    elif l[pos] == ele:
        return pos
    else:
        return linear_search(l, ele, pos + 1)

# To search for an element in a list using binary search
def binary_search(l, ele, beg=0, end=None):
    if end == None:
        end = len(l)
    if beg > end:
        return None
    else:
        mid = (beg + end) // 2
        if l[mid] == ele:
            return mid
        elif l[mid] > ele:
            return binary_search(l, ele, beg, mid - 1)
        else:
            return binary_search(l, ele, mid + 1, end)

# To check if an inputted string is palindromic or not
def palindrome(s):
    l = len(s)
    if l <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])

# To find LCM of 2 numbers
def LCM(a, b):
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            break
    else:
        i = 1
    if i == 1:
        return a * b
    else:
        return i * LCM(a // i, b // i)

# To find HCF of 2 numbers
def HCF(a, b):
    if a % b == 0:
        return b
    else:
        return HCF(b, a % b)