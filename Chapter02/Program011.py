#Program 11 WAP to Print Sum of Digit.
print("This is Program 11 for 'DSA with Python' Series");

a=int(input('input a Four Digit number:'));
print (a);
b=int(a%10);
c=int(a/1000)%10;
d=int(a/10)%10;
e=int(a/100)%10;
f=int(b+c);
g=int(d+e);
        
print("1st Digit",b);
print("4th Digit",c);
print("2th Digit",d);
print("3th Digit",e);
print("Sum of 1st and 4th Dight :",f);
print ("Sum of 2nd and 3rd Digit :",g);
