import os


def main():
    print(__file__)
    print(os.path.dirname(__file__))
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if __name__ == '__main__':
    main()
