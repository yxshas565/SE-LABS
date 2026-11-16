from hypothesis import given, strategies as st
from daycare_fees import parse_enrolment, hours_average, payable_fee


@given(st.text() | st.none())
def test_parse_enrolment_no_crash(s):
    parse_enrolment(s)


@given(st.text() | st.none())
def test_hours_average_no_crash(s):
    hours_average(s)


@given(st.text() | st.none())
def test_payable_fee_no_crash(s):
    payable_fee(s)


def test_parse_enrolment_valid_input():
    assert parse_enrolment("toddler:25") == ("Toddler", 25.0)


def test_hours_average_valid_input():
    assert hours_average("20,25,30") == 25


def test_payable_fee_valid_input():
    assert payable_fee("3000|250") == 3290.0
