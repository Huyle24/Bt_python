s = 4 - 2/4 - 1/5 - 1/6
t = 1
e = 1
i = 1
while e >= pow(10,-6):
    t = t*16
    e = (4/(8i+1) � 2/(8i+4) � 1/(8i+5) � 1/(8i+6)) / t
    s = s + e
    i = i + 1
print(s)