# lowest cgpa from three user inputs
cg1=input("enter 1st cgpa : ")
cg2=input("enter 2nd cgpa : ")
cg3=input("enter 3rd cgpa : ")

cg1=float(cg1)
cg2=float(cg2)
cg3=float(cg3)

if cg1<cg2 and cg1<cg3:
    print("1st friend has lowest cgpa")
elif cg2<cg1 and cg2<cg3:
    print("2nd friend has lowest cgpa")
else:
    print("3rd friend has lowest cgpa")


#average cgpa

avg=(cg1+cg2+cg3)/3
txt=f"average cgpa is : {avg}"
print(txt)