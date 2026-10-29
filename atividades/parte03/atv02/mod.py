li = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def fi(x):
    fibonacci = []
    if x == 0:
        print(f'O termo é 0')
    elif x == 1:
        for n in fibonacci:
            print(x)