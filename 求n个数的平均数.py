n=input("please enter the number of the num:")

sum=0;

for i in range(int(n)):
	x=input("the {}ed number is :".format(i+1))
	sum+=int(x);
aver=sum/int(n);
print("average num is:",aver)
