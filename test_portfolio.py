import pytest
from portfolio import Portfolio, Shares

def test_empty_portfolio():
    p = Portfolio()
    assert p.cost() == 0.0

def test_buy_one_stock():
    p = Portfolio()
    ibm = Shares("IBM", 100, 176.48)
    p.buy(ibm)
    assert p.cost() == 17648.0

def test_buy_two_stocks():
    p = Portfolio()
    ibm = Shares("IBM", 100, 176.48)
    hpq = Shares("HPQ", 100, 36.15)
    p.buy(ibm)
    p.buy(hpq)
    assert p.cost() == 21263.00

def test_not_enough_arguments_to_buy():
    p = Portfolio()
    with pytest.raises(TypeError):
        p.buy()