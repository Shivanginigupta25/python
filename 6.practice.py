n = int(input())
l= { }
for i in range(n):
    key = input()
    value = int(input())
    l.update({key: value})
print(l)
