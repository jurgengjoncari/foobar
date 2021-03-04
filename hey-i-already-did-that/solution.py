v = []
def solution(n, b):
    v.append(n)
    print(set(v))
    x = "".join(sorted(n, reverse=True))
    y = "".join(sorted(n))
    z = subtract(x, y, len(n), b)
    # if v.count(z) >= 4:
    #     return len(v) - 1
    # else:
    #     n = z
    #     solution(n, b)
    # n = z
    while True:
        n = z
        return solution(n, b)
        

def subtract(m, s, k, b):
    m = list(m)
    s = list(s)
    d = []
    for i in range(k - 1, -1, -1):
        m_int = int(m[i])
        s_int = int(s[i])
        m_previews = int(m[i - 1])
        if m_int < s_int:
            m_previews -= 1
            m[i - 1] = m_previews
            m_int += b
        d.insert(0, str(m_int - s_int))
    return "".join(sorted(d))


# solution('1211', 10)

solution('210022', 3)