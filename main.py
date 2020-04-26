from connectdb import connect
from listen import Ears
from TextParser import parse
from speech import speak


class Initializer:

    def __init__(self):
        self.db = connect()
        if self.db != " ":
            while True:
                val = Ears().run()
                if str(val).lower() == 'exit':
                    break
                if val != "":
                    parse(val)


def main():
    Initializer()


if __name__ == '__main__':
    main()
