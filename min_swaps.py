def cycle_decomposition(permutations):
    unvisited=set(permutations)
    while unvisited:
        j=i=unvisited.pop()
        cycle=[i]
        while True:
            j=permutations[j]
            if j==i:
                break
            cycle.append(j)
            unvisited.remove(j)
        yield cycle
def minimum_swaps(seq):
    permutations=sorted(range(len(seq)),key=seq.__getitem__)
    return sum(len(cycle)-1 for cycle in cycle_decomposition(permutations))
n=int(input())
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
print("The array:",a)
print("minimum swaps",minimum_swaps(a))
