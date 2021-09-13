#Filter, Map , Reduce

nums = [1,2,4,6,8,9,10]

evens = (filter(lambda n : n % 2 == 0,nums))
print(evens)

inc = list(map(lambda n : n + 2,evens))
print(inc)

sum = reduce(lambda a,b : a+b,inc)
print(sum)
