#for循环
for i in range(1,10):
	for x in range (2,i):
		if i%x==0:
			print(i,"equals",x,"*",i//x)
			break;
	else:
		print(i,"is a prime number")             
