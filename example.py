from tasks import add


def main():
    result = add.delay(37, 4515)
    print(result.status)
    print(result.get())
    print(result.state)


if __name__ == '__main__':
    main()
