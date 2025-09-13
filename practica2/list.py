from functools import reduce
lista= [1,2,3,4,5,6,7,8,9,10]

if __name__ == '__main__':
    print(list(map(lambda x : x*x, lista)))
    print(list(filter(lambda x : (x % 2)==0, lista)))
    print(reduce(lambda x,y: x+y, lista))
    print(reduce(lambda x,y: x*y, lista[:5]))

