#1
a=[1,4,3,7,6]
print(a)
a.append(8)
print(a)
a.remove(a[1])
print(a)

sum=0
for i in a:
    sum+=int(i)
print(sum)


#2
cities=('Dhaka','Rangpur','Rajshahi','Sylhet','Khulna')
print(cities[2])
cities=list(cities)
cities.append('Chittagong')
cities=tuple(cities)
print(cities)


#3
d={
    'math':90,
    'physics':95,
    'chemistry':85
}
d['biology']=80
print(d.keys())

s=0
for i in d.values():
    s+=int(i)
print('average is : ',+s/3)

