from bloomdata.wallet import Wallet
import pytest

@pytest.fixture
def empty_wallet():
    return Wallet()


@pytest.fixture
def wallet_20():
    return Wallet(20)


def test_empty_wallet(empty_wallet):
    assert empty_wallet.balance == 0


def test_wallet_20(wallet_20):
    assert wallet_20.balance == 20


def test_wallet_20_spend_10(wallet_20):
    assert wallet_20.spend_cash(10) == 'remaining balance: 10'
    assert wallet_20.balance == 10


def test_spend_all_cash(wallet_20):
    assert wallet_20.spend_cash(15) == \
        f'remaining balance: {wallet_20.balance}'

