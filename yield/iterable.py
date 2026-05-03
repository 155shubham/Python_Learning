def loopthrough(n):
    for i in range(n):
        yield i


def loopthrough_without_yield(n):
    for i in range(n):
        print(i)


if __name__ == "__main__":
    for i in loopthrough(5):
        print(i)
        print("Doing some work...")

    # this will throw error because the generator is
    # exhausted after the first loop
    # for i in loopthrough(5):
    #     print(i)
    #     print("Doing some work...")

    loopthrough_without_yield(5)
    print("Doing some work...")
