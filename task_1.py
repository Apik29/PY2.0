import logging

logging.basicConfig(filename='logs.log', filemode='w+', encoding='utf-8', level=logging.ERROR)


def my_func_div(divisor, dividend):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        logging.error(f'Вы не можете делить на 0')

print(my_func(0, 300))