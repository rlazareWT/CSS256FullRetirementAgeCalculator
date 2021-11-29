Feature: Full Retirement Age
  As a US citizen,
  I want to determine my full retirement age,
  so that I can plan for the future.

  Scenario Outline: The correct year is returned for year between 1900 and the current year
    Given the birth year must be between 1900 and the current year
    When the user enters a valid birth year
    Then the retirement age for birth year "<birth>" is "<year>" years and "<month>" months

    Examples: Retirement ages
      | birth | year  | month |
      | 1900  | 65    | 0     |
      | 1905  | 65    | 0     |
      | 1936  | 65    | 0     |
      | 1937  | 65    | 0     |
      | 1938  | 65    | 2     |
      | 1939  | 65    | 4     |
      | 1940  | 65    | 6     |
      | 1941  | 65    | 8     |
      | 1942  | 65    | 10    |
      | 1943  | 66    | 0     |
      | 1944  | 66    | 0     |
      | 1945  | 66    | 0     |
      | 1946  | 66    | 0     |
      | 1947  | 66    | 0     |
      | 1948  | 66    | 0     |
      | 1949  | 66    | 0     |
      | 1950  | 66    | 0     |
      | 1951  | 66    | 0     |
      | 1952  | 66    | 0     |
      | 1953  | 66    | 0     |
      | 1954  | 66    | 0     |
      | 1955  | 66    | 2     |
      | 1956  | 66    | 4     |
      | 1957  | 66    | 6     |
      | 1958  | 66    | 8     |
      | 1959  | 66    | 10    |
      | 1960  | 67    | 0     |

  Scenario: ValueError Exception is raised if the birth year is negative
	Given the birth year must be a positive number
	When the user enters “-1899”
	Then the program raises a ValueError Exception

  Scenario: ValueError exception is raised if the birth year is before 1900
	Given the birth year must after 1900
	When the user enters 1899
	Then the program raises a ValueError Exception

  Scenario: ValueError Exception is raised if the birth month is less than 1
	Given the birth month must be between 1 and the current 12
	When the user enters “1” for the month
	Then the program raises a ValueError Exception

  Scenario: The correct retirement year and month tuple is returned for November 1944
	Given the birth month must be between 1 and the current 12 and the birth year between 1900 and the current year
	When the user enters the birth date of November 1944 and retirement age of 66 years and 0 months
	Then The retirement date shown is November 2010

  Scenario: The correct retirement year and month tuple is returned for December 1944
	Given the birth month must be between 1 and the current 12 and the birth year between 1900 and the current year
	When the user enters the birth date December 1944 and retirement age of 66 years and 0 months
	Then The retirement date shown is December 2010

  Scenario: ValueError Exception is raised if the birth month is greater than 12
	Given the birth month must be between 1 and the current 12
	When the user enters “13” for the month
	Then The program raises a ValueError Exception

