from conversion import run


def main():
    input_str = input("Insert value for converting (ex: meter:2.5): ")
    for line in run(input_str):
        print(line)


if __name__ == "__main__":
    main()
