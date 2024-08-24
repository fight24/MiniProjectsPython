from Art_Calc import logo


# Addition
def add_number(f_num, s_num):
    """ add two number """
    return f_num + s_num


# Subtraction
def sub_num(f_num, s_num):
    """ sub two number """
    return f_num - s_num


# Multiplication
def mul_num(f_num, s_num):
    """ Mul two number """
    return f_num * s_num


# Division
def div_num(f_num, s_num):
    """ div two number """
    return f_num / s_num


operations = {
    "+": add_number,
    "-": sub_num,
    "*": mul_num,
    "/": div_num
}


def calc():
    should_continue = True
    print(logo + "\n")
    num1 = int(input("What is the first number?: "))
    while should_continue:

        for sym in operations:
            print(sym)
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What is the next number?: "))
        calc_func = operations[operation_symbol]
        answer = calc_func(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calc()


calc()
