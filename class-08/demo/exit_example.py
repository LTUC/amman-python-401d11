# from sys import exit

def main():
    name = input('Please Enter your Name:')
    end_game = 'a'
    while end_game != "q":
        print(f'{name}, please press q to quit')
        end_game = input(" >")
    quit_game('Thanks for Playing')


def quit_game(message):
    exit(message)
    pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit_game(' Ctrl+C Detected!')