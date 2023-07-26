def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None
    except TypeError:
        print("Error: invalid operand types")
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))
