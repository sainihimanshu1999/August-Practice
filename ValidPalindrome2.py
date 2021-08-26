'''It is a very basic but very premetive approach in finding palindrome, we can remove at most on character and then we
have to see whether this string is a palindrome or not'''


def validPalindrome(s):
    low = 0
    high = len(s)-1

    while low<high:
        if s[low]!=s[high]:
            one = s[low:high]
            two = s[low+1:high+1]

            return one == one[::-1] or two == two[::-1]


        low += 1
        high -=1

    return True