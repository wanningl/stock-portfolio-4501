import pytest
from portfolio import Portfolio

def test_empty_portfolio():
    p = Portfolio()
    assert p.cost() == 0.0

def test_buy_one_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    assert p.cost() == 17648.0

def test_buy_two_stocks():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    p.buy("HPQ", 100, 36.15)
    assert p.cost() == 21263

# 如果TypeError raised in block then pass the test, else fail
def test_not_enough_arguments_to_buy():
    p = Portfolio()
    with pytest.raises(TypeError):
        p.buy('IBM')