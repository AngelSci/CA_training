import random
def breakfast():
    out = []
    l = ['spam','eggs','bacon']
    for _ in range(6):
        i = random.randint(0,2)
        out.append((l[i]+' ')*random.randint(1,3))

    return ''.join(out)
