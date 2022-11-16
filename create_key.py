#XXXXX-XXXX-XXX-XX
def keyCreate(key):
    block1 = key[0:5]
    block2 = key[5:9]
    key3 = block2
    count = 0

    for i in key3:
        if i.isdigit():
            count += 1
        else: key3 = key3.strip(i)

    if count  == 4:
        key3 = key3.strip(key3[len(key3) - 1])

    block3 = key3
    block4 = key3.strip(block3[len(block3) - 1])
    key = block1 + "-" + block2 + "-" + block3 + "-" + block4

    return key
