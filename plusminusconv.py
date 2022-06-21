'''

Write a function solution that, 
given a string S of length N, 
replaces all occurrences of "plus" with "+" and all occurrences of "minus" with "-".

Examples:

1. Given S = "minusplusminus", the function should return "-+-".

2. Given S = "plusminusminusplus", the function should return "+--+"

'''
def solution(S):
    # your code here
    return S.replace('plus', '+').replace('minus', '-')
print(solution("minusplusminus"))
print(solution("plusminusminusplus"))