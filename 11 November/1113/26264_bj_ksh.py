N = int(input())
memo = input()
B, S = 0, 0

while memo:
    if memo[-1] == 'y':
        S += 1
        memo = memo[:-8]
    else:
        B += 1
        memo = memo[:-7]

if B > S:
    print('bigdata?')
elif S > B:
    print('security!')
else:
    print('bigdata? security!')