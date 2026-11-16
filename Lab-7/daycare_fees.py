from math import isfinite


def parse_enrolment(text):
    if not isinstance(text, str):
        return "", 0.0

    age_group, separator, hours = text.partition(":")
    if not separator:
        return "", 0.0

    try:
        hours_value = float(hours.strip())
        if not isfinite(hours_value):
            return age_group.strip().title(), 0.0
    except (ValueError, TypeError, OverflowError):
        return age_group.strip().title(), 0.0

    return age_group.strip().title(), hours_value


def hours_average(hours_csv):
    if not isinstance(hours_csv, str):
        return 0

    values = []

    for item in hours_csv.split(","):
        try:
            values.append(int(item.strip()))
        except (ValueError, TypeError, OverflowError):
            continue

    if not values:
        return 0

    return sum(values) // len(values)


def payable_fee(text):
    if not isinstance(text, str):
        return 0.0

    fee, separator, discount = text.partition("|")
    if not separator:
        return 0.0

    try:
        fee_value = float(fee.strip())
        discount_value = float(discount.strip())

        if not isfinite(fee_value) or not isfinite(discount_value):
            return 0.0

        total = fee_value * 1.18 - discount_value

        if not isfinite(total):
            return 0.0

        return max(total, 0.0)

    except (ValueError, TypeError, OverflowError):
        return 0.0


def main():
    print("==== Running parse_enrolment ====")
    user_input = input("Enter age group:hours (e.g. toddler:25): ")
    result = parse_enrolment(user_input)
    print("Age Group and Hours:", result)

    print("\n==== Running hours_average ====")
    user_input = input("Enter weekly hours as CSV (e.g. 20,25,30): ")
    result = hours_average(user_input)
    print("Average Hours:", result)

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 3000|250): ")
    result = payable_fee(user_input)
    print("Payable Fee:", result)


if __name__ == "__main__":
    main()
