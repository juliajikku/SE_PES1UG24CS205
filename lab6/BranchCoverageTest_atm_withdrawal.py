
import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup


# ---------------- WITHDRAW TESTS ----------------

def test_simple_withdrawal():
    assert withdraw(5000, 1000, "savings", True) == 4000


def test_current_account_withdrawal():
    assert withdraw(60000, 20000, "current", True) == 40000


def test_unknown_account():
    with pytest.raises(ValueError, match="unknown account"):
        withdraw(5000, 1000, "business", True)


def test_zero_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, 0, "savings", True)


def test_negative_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, -100, "savings", True)


def test_amount_not_multiple_of_100():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, 150, "savings", True)


def test_savings_limit_exceeded():
    assert withdraw(50000, 26000, "savings", True) == "limit exceeded"


def test_current_limit_exceeded():
    assert withdraw(60000, 51000, "current", True) == "limit exceeded"


def test_other_bank_fee():
    assert withdraw(5000, 1000, "savings", False) == 3980


def test_other_bank_fee_above_10000():
    assert withdraw(20000, 11000, "current", False) == 8970


def test_other_bank_fee_at_10000():
    assert withdraw(15000, 10000, "current", False) == 4980


def test_insufficient_funds():
    assert withdraw(500, 1000, "savings", True) == "insufficient funds"


def test_insufficient_funds_with_fee():
    assert withdraw(1010, 1000, "savings", False) == "insufficient funds"


# ---------------- PIN CHECK TESTS ----------------

def test_correct_pin():
    assert pin_check(1234, 1234, 0) == "ok"


def test_incorrect_pin_first_attempt():
    assert pin_check(1111, 1234, 0) == "retry"


def test_incorrect_pin_second_attempt():
    assert pin_check(1111, 1234, 1) == "retry"


def test_incorrect_pin_third_attempt():
    assert pin_check(1111, 1234, 2) == "card blocked"


def test_card_already_blocked():
    assert pin_check(1234, 1234, 3) == "card blocked"


# ---------------- NOTE BREAKUP TESTS ----------------

def test_note_breakup_500():
    assert note_breakup(500) == (1, 0, 0)


def test_note_breakup_700():
    assert note_breakup(700) == (1, 1, 0)


def test_note_breakup_400():
    assert note_breakup(400) == (0, 2, 0)


def test_note_breakup_300():
    assert note_breakup(300) == (0, 1, 1)


def test_note_breakup_100():
    assert note_breakup(100) == (0, 0, 1)


def test_note_breakup_1200():
    assert note_breakup(1200) == (2, 1, 0)


def test_note_breakup_invalid_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        note_breakup(150)
