import timeit

num = 10000

def method1():
    l = []
    for n in xrange(num):
        l = l + [n]
    print l[0]

def method2():
    l = []
    for n in xrange(num):
        l.append(n)
    print l[0]

def method3():
    l = [n for n in xrange(num)]
    print l[0]

def method4():
    l = range(num)
    print l[0]

def list_operations():
    l = [1, 2, 3, 4, 5]
    m = [99, 100]

    l.extend(m) #extends the original list
    print l

    slice = l[5:7] #slicing the list
    print slice

    k = [0]*5 #repetitive values declaration
    print k

def dynamic_lists():
    import sys
    n = 10
    data = []
    for i in range(n):
        a = len(data)
        b = sys.getsizeof(data);
        print 'length:{0:1d}, size in bytes:{1:3d}'.format(a, b)
        data.append(i)
    print data

def 

#method1()
#method2()
#method3()
#method4()
#list_operations()
dynamic_lists()
#print timeit.timeit("method1()", "from __main__ import method1, num", number=5)
#print timeit.timeit("method2()", "from __main__ import method2, num", number=5)
#print timeit.timeit("method3()", "from __main__ import method3, num", number=5)
#print timeit.timeit("method4()", "from __main__ import method4, num", number=5)