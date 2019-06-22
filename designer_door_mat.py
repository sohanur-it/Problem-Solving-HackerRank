#!/usr/bin/python3

n, m = map(int,input().split())
#pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n)]
#print(pattern)
#print('\n'.join(pattern + ['WELCOME'.center(m, '-')] ))


pattern1= [(".|."*(2*i+1)).center(m,'-') for i in range(n//2)]
#pattern = [('.|.'*(2*i+1)).center(m,'-') for i in range(n//2)]
pattern = pattern1 + ['WELCOME MOU'.center(m,'-')] +pattern1[::-1]
print("\n".join(pattern))
