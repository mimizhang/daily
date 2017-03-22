# -*- coding: utf-8 -*-
import hmac
import hashlib

# arrayOfByte = bytearray(32)
# arrayOfByte[0] = 87
# arrayOfByte[1] = 256-77
# arrayOfByte[2] = 119
# arrayOfByte[3] = 94
# arrayOfByte[4] = 256-103
# arrayOfByte[5] = 256-72
# arrayOfByte[6] = 256-114
# arrayOfByte[7] = 256-108
# arrayOfByte[8] = 104
# arrayOfByte[9] = 256-97
# arrayOfByte[10] = 256-11
# arrayOfByte[11] = 256-84
# arrayOfByte[12] = 103
# arrayOfByte[13] = 256-59
# arrayOfByte[14] = 256-1
# arrayOfByte[15] = 256-21
# arrayOfByte[16] = 113
# arrayOfByte[17] = 256-68
# arrayOfByte[18] = 256-96
# arrayOfByte[19] = 256-57
# arrayOfByte[20] = 256-122
# arrayOfByte[21] = 117
# arrayOfByte[22] = 73
# arrayOfByte[24] = 256-16
# arrayOfByte[25] = 256-69
# arrayOfByte[26] = 256-79
# arrayOfByte[27] = 256-77
# arrayOfByte[28] = 80
# arrayOfByte[29] = 256-98
# arrayOfByte[30] = 256-99
# arrayOfByte[31] = 54

python：
def toHex(str):
    lst = []
    for ch in str:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0' + hv
        lst.append(hv)
    return reduce(lambda x, y: x + y, lst)

hmac.new(toHex('57b3775e99b88e94689ff5ac67c5ffeb71bca0c786754900f0bbb1b3509e9d36'), '/api/getProductData?productCode=6921355240023'.encode(), digestmod=hashlib.sha256).digest()












