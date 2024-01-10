import decimal


def run_timing():
    """Ask the user repeatedly for numeric input. Print the average
    time and number of runs."""
    sum_of_runtime, num = 0, 0
    time = input("Enter 10 km run time: ")
    while time:
        sum_of_runtime += float(time)
        num += 1
        time = input("Enter 10 km run time: ")
    try:
        print(f'Average time: {sum_of_runtime/num:.2f}')
    except ZeroDivisionError:
        print("0 runs -> 0 time")


def return_new_float():
    """Return a float consisting of before digits before the decimal
    point and after digits after. Thus, if we call the 2function with
    1234.5678, 2 and 3, the return value should be 34.567."""
    float_num = float(input("Enter float: "))
    int_num1 = int(input("Enter int: "))
    int_num2 = int(input("Enter int: "))
    result = float_num % 10**int_num1
    result = int(result * 10**int_num2)/10**int_num2
    return result


def true_float_sum():
    """Take two strings from the user, turn them into decimal
    instances, print the floating-point sum of the user’s two inputs."""
    num_1 = input("Enter 1 float: ")
    num_2 = input("Enter 2 float: ")
    num_1 = decimal.Decimal(num_1)
    num_2 = decimal.Decimal(num_2)
    return num_1 + num_2


if __name__ == '__main__':
    print(true_float_sum())
    run_timing()
    print(return_new_float())
