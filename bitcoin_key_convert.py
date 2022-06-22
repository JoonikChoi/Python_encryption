swap_flag = 0

#공개된 고정 좌표 G
G = [0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8]
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
pK = [0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8]


def Euclidian(a,b):
    global swap_flag
    a_temp = a
    b_temp = b
    q, r, t, r = 0, 0, 0, 0

    s_1, s_2 = 1, 0
    t_1, t_2 = 0, 1
    if a < b:
        a, b = b, a  # swap
        swap_flag = 1

    while (True):
        q = a // b
        r = a - (q * b)
        s = s_1 - (q * s_2)
        t = t_1 - (q * t_2)

        if r == 0:
            break

        a = b
        b = r
        s_1 = s_2
        s_2 = s
        t_1 = t_2
        t_2 = t

    if swap_flag == 0:
        inverse = s_2
    else:
        inverse = t_2
    if inverse < 0:
        inverse = inverse % p

    return inverse

def calc_public_key(p, q, modula):

    x1 = p[0]
    y1 = p[1]
    x2 = q[0]
    y2 = q[1]

    if p == q:
        lamda_deno = 2 * y1
        inverse = Euclidian(lamda_deno, modula)
        lamda = ((3 * ((x1 ** 2)) * inverse + 0)) % modula

    if p != q:
        lamda_deno = x2 - x1
        inverse = Euclidian(lamda_deno, modula)
        lamda = ((y2 - y1) * inverse) % modula

    x3 = (lamda ** 2 - x1 - x2) % modula
    y3 = (lamda * (x1 - x3) - y1) % modula
    return x3, y3

def doubleAndadd(bit_list):
    global pK
    for i in bit_list:
        pK = calc_public_key(pK, pK, p)
        if i == 1:
            pK = calc_public_key(pK, G, p)

    return pK

private_key = input('private key input(hex): ')
private_key = bin(int(private_key,16))
bit_list = list(map(str, private_key))

del bit_list[0]
del bit_list[0]
del bit_list[0]
bit_list = list(map(int, bit_list))

public_key = doubleAndadd(bit_list)

print('공개 키 :', '[', hex(public_key[0]), ',', hex(public_key[1]),']')
