d1, d2, d3 = map(int, input().split())

ans = min(d1 + d2 + d3,2 * (d1 + d2),2 * (min(d1, d2) + d3))

print(ans)
