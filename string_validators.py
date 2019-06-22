#!/usr/bin/python3
# t = type(s)
# for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
#     print(any(method(c) for c in s))

str = input()
print(any(c.isalnum()  for c in str))
print(any(c.isalpha() for c in str))
print(any(c.isdigit() for c in str))
print(any(c.islower() for c in str))
print(any(c.isupper() for c in str))


# for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
#         any(eval("c." + test + "()") for c in s)
