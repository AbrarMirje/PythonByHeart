def closures(num):
    def actual(x):
        return x ** num
    return actual

f = closures(2)
g = closures(3)

print(f(3))
print(g(3))