
import re


def notes_needed(amount):
    """Calculate the number of 100-value notes required."""

    if not isinstance(amount, str):
        return None

    amount = amount.strip()

    if not re.fullmatch(
        r"(?:[0-9]+|[0-9]{1,3}(?:,[0-9]{3})+)",
        amount
    ):
        return None

    amount = int(amount.replace(",", ""))

    return amount // 100


def mask_card(card_number):
    """Mask a valid 16-digit card number."""

    if not isinstance(card_number, str):
        return None

    card_number = card_number.replace(" ", "").replace("-", "")

    if not re.fullmatch(r"[0-9]{16}", card_number):
        return None

    return "XXXX XXXX XXXX " + card_number[-4:]


def average_withdrawal(amounts_csv):
    """Calculate the average withdrawal amount."""

    if not isinstance(amounts_csv, str):
        return None

    amounts_csv = amounts_csv.strip()

    if not amounts_csv:
        return None

    values = amounts_csv.split(",")

    if any(
        not re.fullmatch(r"[0-9]+", value.strip())
        for value in values
    ):
        return None

    amounts = [int(value.strip()) for value in values]

    return sum(amounts) // len(amounts)


def main():
    print("==== Running notes_needed ====")
    user_input = input("Enter an amount (e.g. 2,500): ")
    result = notes_needed(user_input)
    print("Number of 100 Notes:", result)

    print("\n==== Running mask_card ====")
    user_input = input(
        "Enter a card number (e.g. 1234 5678 9012 3456): "
    )
    result = mask_card(user_input)
    print("Masked Card:", result)

    print("\n==== Running average_withdrawal ====")
    user_input = input(
        "Enter withdrawals as CSV (e.g. 500,1000,2000): "
    )
    result = average_withdrawal(user_input)
    print("Average Withdrawal:", result)


if __name__ == "__main__":
    main()
