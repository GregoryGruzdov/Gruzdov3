def percents(x, y):
    '''what percentage of X is Y'''
    one_percent_of_x = x / 100
    result = y/one_percent_of_x
    return result


def print_percents(x, y):
    '''print what percentage of X is Y'''
    print(str(y) + ' is ' + str(percents(x, y)) + '% of ' + str(x))

# print('Эта программа считает, сколько процентов от Первого введенного вами числа составит Пторое введенное число.')
# print('Введите Первое число')
# x=int(input())
# print('Введите Второе число')
# y=int(input())


print_percents(200, 50)