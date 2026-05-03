def capitalise(str):
    if len(str) <= 1:
        return str.upper()
    return str[0].upper() + str[1:]


if __name__ == "__main__":
    print(capitalise("hello world"))
    # print(capitalise("a"))
    # print(capitalise(""))
