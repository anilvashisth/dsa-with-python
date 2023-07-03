#Program 10 WAP to Print Sum of Five Digit.
print("This is Program 10 for 'DSA with Python' Series");

a = int(input('Enter a Five Digit Number : '));

b = int(a/10)%10;
print("B :",b);
c = int(a/100)%10;
print("C :",c);
d = int(a/1000)%10;
print("D :",d);
e = int(a/10000)%10;
print("E :",e);
f = int(a/100000);
print("F :",f);
g = int(a%10);
print("G :",g);

h = int(b+c+d+e+g);
print("The Sum is :",h);
