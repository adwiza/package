import celery
from tasks import add, divide


def main():
    chain = celery.chain(add.s(17, 15), divide.s(10))
    print(chain)
    result = chain()
    print(result.state)
    print(result.get())
    print(result.state)


if __name__ == '__main__':
    main()
