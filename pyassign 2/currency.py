"""currency.py: Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.
"""

from urllib.request import urlopen


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""

    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?\
from={0}&to={1}&amt={2}'.format(currency_from, currency_to, amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')

    if jstr.find('true') == -1:
        jstr = eval(jstr.replace('false', '"false"'))
        print(jstr['error'])

    else:
        jstr = eval(jstr.replace('true', '"true"'))
        amount_to = float(jstr['to'].split()[0])
        return amount_to


def test_exchange():
    assert(exchange('USD', 'EUR', 2.5) == 2.0952375)
    assert(exchange('USD', 'CNY', 34) == 221.8891)
    assert(exchange('USD', 'JPY', 7) == 762.01002815)
    assert(exchange('USD', 'GBP', 561) == 429.898227)
    assert(exchange('USD', 'SGD', 1.67) == 2.258508)


def testAll():
    """test all cases"""
    test_exchange()
    print("All tests passed")
