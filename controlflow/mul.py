def print_multiples(n):
    i = 1
    while i <= 6:
        print(n * i, '\t')
        i += 1


def print_m_table():
    i = 1
    while i <= 6:
        print_multiples(i)
        i += 1


print_m_table()
