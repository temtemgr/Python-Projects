# a file that handles logic

# claculates sum from list
def calc_sum(list: list):
    sum = 0
    for item in list:
        sum += item["price"]
    return sum