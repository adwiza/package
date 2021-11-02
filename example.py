from tasks import multiply_roulette
import time


def main(number_of_jobs=10):
    results = [
        multiply_roulette.delay(10, 30)
        for _ in range(number_of_jobs)
    ]
    time.sleep(0.5)
    pending_tasks = []
    for i, result in enumerate(results):
        if result.status == 'SUCCESS':
            print(f'{result.id} -&gt; {result.get()}')
        else:
            print(f'{result.id} is {result.state}')
            pending_tasks.append(i)

    print('Ждем застрявшие задачи')
    for result in [results[i] for i in pending_tasks]:
        print(f'{result.id}', end=' ')
        print(f'-&gt; {result.get()}')


if __name__ == '__main__':
    main()
