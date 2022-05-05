
def print_rangoli(size):
    size=(n*4)-3
    blank="-"
    Alphabet="-abcdefghijklmnopqrstuvwxyz"
    count_middle=0
    decresing=0
    add1=0
    for i in range (n-1):
        print(blank*((size//2)-decresing)+Alphabet[n]+blank*((size//2)-decresing)+(blank)*(decresing+add1))
        count_middle -=1
        decresing+=2
        add1+=2

    


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)