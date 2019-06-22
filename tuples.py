#!/usr/bin/python3

# n = int(input())

# inputs = list(map(int,input().split()))[:n]

# t = tuple(inputs)

# #print(t)

# print(hash(t))



if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))[:n]
    t = tuple(integer_list)
    print(hash(t))
