
from hypothesis import given, strategies as st
from atm_withdrawal import notes_needed, mask_card, average_withdrawal


@given(st.text() | st.none())
def test_notes_needed_no_crash(s):
    try:
        notes_needed(s)
    except Exception as e:
        assert False, f"notes_needed crashed with {s!r}: {e}"


@given(st.text() | st.none())
def test_mask_card_no_crash(s):
    try:
        mask_card(s)
    except Exception as e:
        assert False, f"mask_card crashed with {s!r}: {e}"


@given(st.text() | st.none())
def test_average_withdrawal_no_crash(s):
    try:
        average_withdrawal(s)
    except Exception as e:
        assert False, f"average_withdrawal crashed with {s!r}: {e}"


@given(st.integers(min_value=0, max_value=1000000))
def test_notes_needed_correct_result(amount):
    assert notes_needed(str(amount)) == amount // 100


@given(st.text(alphabet="0123456789", min_size=16, max_size=16))
def test_mask_card_correct_result(card):
    expected = "XXXX XXXX XXXX " + card[-4:]
    assert mask_card(card) == expected


@given(
    st.lists(
        st.integers(min_value=0, max_value=100000),
        min_size=1,
        max_size=20
    )
)
def test_average_withdrawal_correct_result(amounts):
    csv_input = ",".join(map(str, amounts))
    expected = sum(amounts) // len(amounts)

    assert average_withdrawal(csv_input) == expected
