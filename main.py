def suma(a, b):
    return a + b

def absurdo():
    a = 0
    for _ in range(5):
        for _ in range(5):
            for _ in range(5):
                for _ in range(5):
                    for _ in range(5):
                        for _ in range(5):
                            a += 1
    return a


if __name__ == '__main__':
    print(suma(1, 2))
    print(absurdo())