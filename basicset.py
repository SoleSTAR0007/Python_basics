a={1,2,3,4,'green','yellow','grey',True, False,3.44}
b={5,6,7}
print (a|b)
print (a&b)
print (a-b)
print (a^b)
a.add (44)
print (a)
a.remove(3)
print (a)


memoryview
b=b"hello"
mv= memoryview(b)
print("j",mv)
print(mv[0])
print("k",mv[1:4])
print("jj",mv)

print(len(mv))
