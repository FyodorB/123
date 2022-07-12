def main(a, b):
    return pow(a, 2) + pow(b, 2)


def main_multi(a, b):
    return pow(a, 2) * pow(b, 2)


def main_min(a, b):
    return pow(a, 3) - pow(b, 2)

def main_del(a, b):
    return pow(a, 2) / pow(b, 2)


if __name__ == "__main__":
    print(main(2, 2))
    print(main_min(2, 2))
    print(main_multi(2, 2))
    print(main_del(2, 1))
