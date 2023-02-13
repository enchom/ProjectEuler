def calc_sum(x):
    x = x * (10 ** 500)
    L = 1
    R = x
    best = 0
    
    while L <= R:
        mid = (L + R) // 2
        if mid * mid <= x:
            best = mid
            L = mid + 1
        else:
            R = mid - 1
    
    if best * best == x:
        return 0
        
    text_num = str(best)
    assert len(text_num) > 100
    text_num = text_num[:100]
    
    ans = 0
    for c in text_num:
        ans += ord(c) - ord('0')
    
    return ans

ans = 0
for i in range(1, 101):
    ans += calc_sum(i)

print(ans)