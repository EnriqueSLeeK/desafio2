
def count_check(string):

    count_a = 0
    has_a = False

    for c in string:
        if c == 'a' or c == 'A':
            count_a += 1
            has_a = True
    
    return [has_a, count_a]

def main():
    print(count_check('lsdkfjhasl;dkfj;asldkjfa;sdfkjlasdf;l'))
    print(count_check('aaaaabbbbaaaaacccca'))
    print(count_check('aaaaa'))


if __name__ == '__main__':
    main()
