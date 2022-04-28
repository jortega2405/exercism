def exchange_money(budget, exchange_rate):
    return float(budget / exchange_rate)


def get_change(budget, exchanging_value):
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    return int(budget / denomination)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    rate = exchange_rate * (1 + spread / 100)
    aux = exchange_money(budget, rate)
    return aux - aux % denomination


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    rate = exchange_rate * (1 + spread / 100)
    return int(exchange_money(budget, rate) - exchangeable_value(budget, exchange_rate, spread, denomination))
