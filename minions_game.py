#!/usr/bin/python3


# str = input()

# lists = [str[i] for i in range(len(str))]

# s = input()

# vowels = 'AEIOU'

# kevsc = 0
# stusc = 0
# #BANANA
# #0 6
# for i in range(len(s)):
#     if s[i] in vowels:
#         kevsc += (len(s)-i)
#         print(kevsc)
#     else:
#         stusc += (len(s)-i)
#         print(stusc)

# if kevsc > stusc:
#     print("Kevin", kevsc)
# elif kevsc < stusc:
#     print("Stuart", stusc)
# else:
#     print("Draw")


##Way --2

def minion_game(string):
    # your code goes here
    s = string
    vowels, L = 'AEIOU', len(s)

    #K = [L-i for i in range(L) if s[i] in vowels]
    K=0
    S=0
    for i in range(L):
    	if s[i] in vowels:
    		K = K + (L-i)
    	else:
    		S = S + (L-i)
    print(K)
    #print(sum(K))

    #S = [L-i for i in range(L) if s[i] not in vowels]
    print(S)
    if K>S:
    	print("Kevin",K)
    elif S>K:
    	print("Stuart",S)
    else:
    	print("Draw")

    #print(sum(S))
    #print(['Stuart '+str(S),['Kevin '+str(K),'Draw'][K==S]][K>=S])

if __name__ == '__main__':
    s = input()
    minion_game(s)





