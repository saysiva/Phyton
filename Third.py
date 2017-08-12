
list1 = [1,2,3,4,5]

list2 = [2,3,4,5,6]

list3 = [1,2,3]

print (list1);
print (list2);
print (list3);

dot = 0
for e,f,g in zip(list1,list2,list3):
    print (e);
    print (f);
    print (g);
    dot += e*f*g
    print ("====" * 10)

print (dot);
