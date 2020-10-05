# Exercise 6

## Mutation Tests

Running the mutation test:
`make mutation-tests`

Output:
```

Tests
==========


- Mutation testing starting -

These are the steps:
1. A full test suite run will be made to make sure we
   can run the tests successfully and we know how long
   it takes (to detect infinite loops for example)
2. Mutants will be generated and checked

Results are stored in .mutmut-cache.
Print found mutants with `mutmut results`.

Legend for output:
🎉 Killed mutants.   The goal is for everything to end up in this bucket.
⏰ Timeout.          Test suite took 10 times as long as the baseline so were killed.
🤔 Suspicious.       Tests took a long time, but not long enough to be fatal.
🙁 Survived.         This means your tests needs to be expanded.
🔇 Skipped.          Skipped.

1. Using cached time for baseline tests, to run baseline again delete the cache file

2. Checking mutants
⠙ 32/32  🎉 32  ⏰ 0  🤔 0  🙁 0  🔇 0

```

Mutation Config:
```
[mutmut]
paths_to_mutate=software_testing/exercises/exercise6/
tests_dir=tests/unit/exercises/exercise6/
```

## Links:
- [Simple Program Implementation in Python](https://github.com/rafaelleinio/software-testing/blob/master/software_testing/exercises/exercise6/income_tax_calculator.py)
- [Unit Tests Implementation](https://github.com/rafaelleinio/software-testing/blob/master/tests/unit/exercises/exercise6/test_income_tax_calculator.py)
- [Mutation Tests with Mutmut](https://github.com/boxed/mutmut)
