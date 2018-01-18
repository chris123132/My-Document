def main():
    sum=0
    count=0
    xstr=input("please input the 1st number(enter to quit):")
    while xstr!="":
        sum+=eval(xstr)
        count+=1
        xstr=input("please input the next number:(enter to quit):")
    print("the average number is:",sum/count)

main()
