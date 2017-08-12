import numpy as np

list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6]
list3 = [1,2,3]

#Converting the normal list as numpy narray
npList1 = np.array(list1);
npList2 = np.array(list2);
npList3 = np.array(list3);


def poor_dot_product(list1, list2, list3):
    dot = 0
    for e,f,g in zip(list1,list2,list3):
        # e, f, g -- values iterated in each list
        print ("e, f, g ::", e,f,g);
        dot += e*f*g
        print ("====" * 10)

    print (dot);


poor_dot_product(list1,list2, list3);

print ("direct dot product :: " )
print (npList3*npList2*npList1)
