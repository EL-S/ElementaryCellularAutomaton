import itertools as i
rule = 30
r = dict(zip(["".join(x) for x in i.product(*[["0","1"]]*3)][::-1],[int(x) for x in str(bin(rule)[2:].zfill(8))]))

s = [0,1,0]

while True:
    s = [0] + list(map(lambda c,p,n: r[str(p)+str(c)+str(n)], s, [0]+s, s[1:]+[0])) + [0]
