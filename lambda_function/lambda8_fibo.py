ans = lambda a,b: lambda c:a+b+c
x = ans(100,20)

print(x)
print(x(30))

sq = lambda x: x.capitalize()
pr=  lambda fun,n: lambda x: n.upper() + " " + fun(x)

ans = pr(sq,"royal")("enfield")
print(ans)

sq_even = 
cb_odd = lambda x: x**3
pri = lambda x: lambda x: x**2 if x%2 == 0 else cb_odd(x)
print(pri(10))