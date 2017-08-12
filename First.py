# First program
import numpy as np

def printDetails(b) :
    print("Details about ... the object ")
    print (b);
    print (b.ndim);
    print (b.shape);
    print (b.size);
    print (b.dtype);
    print (b.itemsize);
    print (b.data);
    print (type(b));
    print ("======" * 6)
    return


a = [1,2,2];
print(a);

k = np.array(a);
printDetails(k);

a = np.arange(16).reshape(4,4)
printDetails(a);

b = np.arange(16)
printDetails(b);

b = np.arange(16).reshape(2,2,4)
printDetails(b);

b = np.arange(16).reshape(2,2,2,2)
printDetails(b);

c = np.array([1,2,3]);
printDetails(c);

s = {1,2,3,4,5,3,5,5,5,5};
print(s);

u = np.linspace(0,2,10);
print (u);
