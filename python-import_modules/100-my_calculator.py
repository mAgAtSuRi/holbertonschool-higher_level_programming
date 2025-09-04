#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1
    import sys

    operator = {
        "+": calculator_1.add,
        "-": calculator_1.sub,
        "*": calculator_1.mul,
        "/": calculator_1.div,
    }
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    op = sys.argv[2]
    result = operator[op](int(sys.argv[1]), int(sys.argv[3]))
    print(
        "{} {} {} = {}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            result
        )
    )
