import pytest
from pytest_bdd import scenario, parsers, given, when, then
import retirement

EXTRA_TYPES = {'Number': int, 'Tuple': tuple}

CONVERTERS = {'birth': int, 'year': int, 'month': int}


@scenario('../features/retirement.feature', 'The correct year is returned for year between 1900 and the current year')
def test_retirement_age():
	pass


@scenario('../features/retirement.feature', 'ValueError Exception is raised if the birth year is negative')
def test_negative_age():
	pass


@scenario('../features/retirement.feature', 'ValueError exception is raised if the birth year is before 1900')
def test_before_1900():
	pass


@scenario('../features/retirement.feature', 'ValueError Exception is raised if the birth month is less than 1')
def test_less_than_0():
	pass


@scenario('../features/retirement.feature', 'The correct retirement year and month tuple is returned for November 1944')
def test_november_1944():
	pass


@scenario('../features/retirement.feature', 'The correct retirement year and month tuple is returned for December 1944')
def test_december_1944():
	pass


@scenario('../features/retirement.feature', 'ValueError Exception is raised if the birth month is greater than 12')
def test_greater_than_12_months():
	pass


@given("the birth year must be between 1900 and the current year")
def step_impl():
	pass


@when("the user enters a valid birth year")
def step_impl():
	pass


@then(parsers.cfparse(
	'the retirement age for birth year "{birth:Number}" is "{year:Number}" years and "{months:Number}" months',
	extra_types=EXTRA_TYPES))
@then('the retirement age for birth year "<birth>" is "<year>" years and "<months>" months')
def step_impl(birth, year, months):
	my_tuple = year, months
	assert retirement.calculate_retirement_age(birth) == my_tuple


@given("the birth year must be a positive number")
def step_impl():
	pass


@when("the user enters “-1899”")
def step_impl():
	pass


@then("the program raises a ValueError Exception")
def step_impl():
	with pytest.raises(ValueError):
		retirement.calculate_retirement_age(-1899)


@then("The program raises a ValueError Exception")
def step_impl():
	with pytest.raises(ValueError):
		retirement.calculate_retirement_age(1899)


@then("The program raises a ValueError Exception")
def step_impl():
	with pytest.raises(ValueError):
		retirement.calculate_retirement_date(1944, 0, 66, 0)


@given("the birth year must after 1900")
def step_impl():
	pass


@when("the user enters 1899")
def step_impl():
	pass


@given("the birth month must be between 1 and the current 12")
def step_impl():
	pass


@when("the user enters “1” for the month")
def step_impl():
	pass


@given("the birth month must be between 1 and the current 12 and the birth year between 1900 and the current year")
def step_impl():
	pass


@when("the user enters the birth date of November 1944 and retirement age of 66 years and 0 months")
def step_impl():
	pass


@then("The retirement date shown is November 2010")
def step_impl():
	assert retirement.calculate_retirement_date(1944, 11, 66, 0) == (2010, 11)


@when("the user enters the birth date December 1944 and retirement age of 66 years and 0 months")
def step_impl():
	pass


@then("The retirement date shown is December 2010")
def step_impl():
	assert retirement.calculate_retirement_date(1944, 12, 66, 0) == (2010, 12)


@when("the user enters “13” for the month")
def step_impl():
	pass


@then("The program raises a ValueError Exception")
def step_impl():
	with pytest.raises(ValueError):
		retirement.calculate_retirement_date(1944, 13, 66, 0)
