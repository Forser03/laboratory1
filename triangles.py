sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
sides.sort()

smax = 0
for i in range(len(sides)):
    for j in range(i + 1, len(sides)):
        for k in range(j + 1, len(sides)):
            a, b, c = sides[i], sides[j], sides[k]
            if all([a < b+c, b < a+c, c < a+b]):
                p = (a + b + c)/2
                s = (p * (p-a) * (p-b) * (p-c)) ** 0.5
                smax = max(smax, s)

print(smax)
