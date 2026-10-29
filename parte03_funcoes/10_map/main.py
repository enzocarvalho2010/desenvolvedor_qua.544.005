import os

li = lambda: os.system('cls' if os.name == 'nt' else 'clear')
pg = lambda x: x*2

def main():
    # lista original
    n = [1,2,3,4,5,6,7,8,9]
    
    li()
    print(f'Lista original: {n}')

    n_pg = list(map(pg,n))
    print(f'Nova lista com pg: {n_pg}')

if __name__ == '__main__':
    main()