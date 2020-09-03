# Exercise 3

## Problem Definition:
Define equivalence classes and a set of test cases suitable for the equivalence class partitioning criteria for the program with the following description:

The program must determine whether an identifier is valid or not in Silly Pascal (a variant of Pascal). A valid identifier must:
- Start with a letter
- Contain only letters or digits
- Must be a minimum of one character
- Maximum of six characters in length

Implement the `isValid (string): boolean` function that takes a string and returns true if the string can be a Silly Pascal identifier and false otherwise. Create the tests for this function.

## Equivalence Classes Analysis:

| Input Condition                 | Valid Class         | Invalid Class  |
|---------------------------------|---------------------|----------------|
| Start with a letter             | Yes (1)             | No (2)         |
| Contains only letters or digits | Yes (3)             | No (4)         |
| Allowed Length                  | 1 <= [L] <= 6 (5)   | [L] == 0 (6)   |
|                                 |                     | [L] > 6 (7)    |

## Test Cases

| Test Cases         | Classes Covered |
|--------------------|-----------------|
| ("abc123", True)   | (1), (3), (5)   |
| ("1abc", False)    | (2)             |
| ("a bc", False)    | (4)             |
| ("", False)        | (6)             |
| ("abcdefg", False) | (7)             |

## Links:
- [Function Implementation](https://github.com/rafaelleinio/software-testing/blob/master/software_testing/exercises/exercise3/is_valid.py)
- [Tests Implementation](https://github.com/rafaelleinio/software-testing/blob/master/tests/unit/exercises/exercise3/test_is_valid.py)
