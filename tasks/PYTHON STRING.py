# EX1:
a="Triceratops"
print(a.upper())
print(a.lower())
print(a.count("t"))
print(a.find("p"))
print(a.index("a"))

#EX2:
name="AyhamZaid"
country="The Kingdom of Jordan"
print("{:s} {:s}".format(name,country))

#EX3:
x="joijfowijvroijvojq"
a,i,e,o,u="a","i","e","o","u"
print("{:s} {:d}".format(a,x.count("a")))
print("{:s} {:d}".format(i,x.count("i")))
print("{:s} {:d}".format(e,x.count("e")))
print("{:s} {:d}".format(o,x.count("o")))
print("{:s} {:d}".format(u,x.count("u")))

#EX4:
firstName="Tala"
secondNmae="Mohammad"
print(firstName[0:1]+secondNmae[0:1])

#EX5:
string="Allosaurus"
print(string[0:4])
print(string[3:7])
print(string[6:])
print(string[2:])
print(string[8:])

#EX6:
a="i hate python"
print(len(a))

#EX7:
a = "jordan"
print("b" in (a)) 
a = "Amman"
print("a" in ("Amman")) 
a = "Egypt"
print("t" in (a)) 
# a="Khuraibet  Al-Souq"
# print(' ' in (a)) 
# b="love python***" 
# print(b.strip("x"))

#EX9:
name = "ayham zaid"
print(" {:s}[AZ]".format(name))

#EX10:
Y= "Orange"
print(Y[0:2]+Y[4:])
X="ME"
print(X*2)

#EX11:
w="Ayham"
print(w[1:])
print(w[0:1]+w[2:])
print(w[0:3]+w[4:])
e="Mohammad"
print("".join(reversed(e)))

#EX12:
a,b,c,d,e,f= "cow","pig","horse","goat","dog","cat"
a1,b1,c1,d1,e1,f1= 50,30,3,3,2,3
print("there are {:d}{:s},{:d}{:s},{:d}{:s},{:d}{:s},{:d}{:s},{:d}{:s} on the farm".format(a1,a,b1,b,c1,c,d1,d,e1,e,f1,f))