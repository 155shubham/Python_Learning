import time


def timer_dec(base_fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        base_fn(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
    return wrapper


@timer_dec
def brew_tea(str="Green Tea"):
    print(f"Brewing {str}")
    time.sleep(1)
    print("Tea is ready!")


@timer_dec
def make_matcha():
    print("Brewing Matcha")
    time.sleep(1)
    print("Matcha is ready!")


if __name__ == "__main__":
    # 1st way: This is the same as using the @timer_dec decorator above the brew_tea function definition
    # brew_tea = timer_dec(brew_tea)

    # 2nd way: OR decorate and call the function in one line like below
    brew_tea("Black Tea")

    make_matcha()
