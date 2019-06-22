#!/usr/bin/python3

n = int(input())
lists =list(map(int, input().strip().split()))[:n]

lists_pos = []
lists_neg = []
lists_zero = []
for l in lists:
	if l > 0:
		lists_pos.append(l)
	if l < 0:
		lists_neg.append(l)
	if l == 0:
		lists_zero.append(l)

print("postive ratio : ","%.6f"%(len(lists_pos)/n))
print("negative ratio : ","%.6f"%(len(lists_neg)/n))
print("negative ratio : ","%.6f"%(len(lists_zero)/n))