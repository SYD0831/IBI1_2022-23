#we	are	consider	the	East<->West	direction	by	comparing	longitude	positions.
#Positive numbers represent the west longitude and negative numbers represent the east longitude
#a->Edinburgh	b->Los	Angeles	c->Haining
#d:the	longitude	distance	that	Rob	travelled	to	Los	Angeles,The distance of this trip
#e:the	longitude	distance	that	Rob	travelled	to	Haining ,The distance of last trip
a=-3.19
b=-188.24
c=116.39
d = a-b
e = c-a
if d == e:
	print("d=e","Rob travelled the same distance both times")
elif d > e:
	print("d>e","Rob travelled further than on his previous international trip")
else:
	print("d<e","Rob didn't travel further than on his previous international trip")
# python  variables.py
#d>e Rob travelled further than on his previous international trip
#By comparing the longitude distance, we found that Rob went farther to Los Angeles than he did to Haining,
#and he did travel farther than he did on his last international trip.






X=True
Y=False
W=X and Y
Z=X or Y
print("the values of W is",W)
print("the values of Z is",Z)
#the values of W is False
#the values of Z is True

