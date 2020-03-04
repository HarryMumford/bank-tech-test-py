from src.account import Account

def test_deposit_returns_balance():
    assert Account().deposit(100) == 100

def test_withdraw_returns_balance():
    a = Account()
    a.deposit(200)
    assert Account().withdraw(100) == 100

