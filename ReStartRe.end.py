import re
s = input()
k = input()

substring = re.compile(k)
r = substring.search(s)

if not r 
    print((-1, -1))
else
    while r
        print(({}, {}).format(r.start(), r.end() - 1))
        r = substring.search(s,r.start() + 1)
