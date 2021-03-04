v = []
def solution(n, b):
    v.append(n)
    print(n)
    print(v)
    x = "".join(sorted(n, reverse=True))
    print(x)
    y = "".join(sorted(n))
    print(y)
    z = subtract(x, y, b)
    print(z)
    if z in v:
        print(len(v) - 1)
        return len(v) - 1
    else:
        n = z
        solution(n, b)
        

def subtract(m, s, b):
    m_list = list(m)
    s_list = list(s)
    k = len(s)
    d = []
    for i in range(k - 1, -1, -1):
        m_int = int(m_list[i])
        s_int = int(s_list[i])
        m_previews = int(m_list[i - 1])
        if m_int < s_int:
            m_previews -= 1
            m_list[i - 1] = m_previews
            m_int += b
        d.insert(0, str(m_int - s_int))
    return "".join(sorted(d))


# solution('1211', 10)

solution('210022', 3)