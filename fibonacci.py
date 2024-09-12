
def pertence_fib_sequencia(n):

    if n == 0 or n == 1:
        return True

    seq = [0, 1]
    while seq[-1] <= n:
        if n == seq[-1]:
            return True
        seq.append(seq[-1] + seq[-2])
    return False

def main():
    print(pertence_fib_sequencia(34))
    print(pertence_fib_sequencia(0))
    print(pertence_fib_sequencia(1))
    print(pertence_fib_sequencia(11))
    print(pertence_fib_sequencia(111))

if __name__ == '__main__':
    main()
