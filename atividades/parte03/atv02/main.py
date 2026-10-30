from mod import fi, li

def main():
    try:
        li()
        fi()
    except Exception as e:
        print(f'{e}')

if __name__ == "__main__":
    main()