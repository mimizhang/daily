# 10进制转36进制
def _10_2_36(num):
    loop = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = []
    while num != 0:
        a.append(loop[num % 36])
        num = int(num / 36)
    a.reverse()
    out = ''.join(a)
    return out


# 36进制转10进制
def _36_2_10(str):
    loop = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    re_str = str[::-1]
    out = 0
    for index, char in enumerate(re_str):
        out += (loop.find(char)) * (36 ** index)
    return out


print(_10_2_36(2587539610541))
print(_36_2_10('LA2212997'))
