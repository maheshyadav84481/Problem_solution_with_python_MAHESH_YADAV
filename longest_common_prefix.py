
l1 = ["geeksforgeek","geeks","geek","geezier"]
size = len(l1)
l1.sort()
end = max(len(l1[0]),len(l1[size-1]))
i = 0
while(i<end and l1[0][i] == l1[size-1][i]):
    i = i+1
    pre = l1[0][0:i]
print(pre)