from __future__ import division
from collections import Counter
from collections import defaultdict

n =  int(raw_input().strip())
numbers = map(int,raw_input().strip().split())

def mean(numbers,n):
    print(round(sum(numbers) / n,1))

def median(numbers):
    numbers.sort(key=int)
    c = len(numbers) // 2
    median = (numbers[c-1] + numbers[c]) / 2
    print(median)

def mode(numbers):
    " Method to get the  mode of given numbers"
    d = {x:numbers.count(x) for x in numbers}
    v = defaultdict(list)

    for key, value in sorted(d.iteritems()):
        v[value].append(key)
    print(min(v[max(v.keys())]))



mean(numbers, n)
median(numbers)
mode(numbers)
