#!/usr/bin/python3


def print_formatted(number):
    length = len('{0:b}'.format(number))
    print('{0:^{length}.3}{1:^{length}.3}{2:^{length}.3}{3:^{length}.3}'.format("Dec","Oct","Hex","Bin",length=length))
    for i in range(1,number+1):
    	print('{0:{length}d} {0:{length}o} {0:{length}X} {0:{length}b}'.format(i,length=length))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)