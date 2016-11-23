import unittest
import budget


class BudgetTestCase(unittest.TestCase):

    def test_raises_error_for_short_grant_lengths(self):
        with self.assertRaises(ValueError):
            b = budget.Budget()
            b.awardBudgetCutProblem([100], 150)

    def test_raises_error_for_long_grant_lengths(self):
        with self.assertRaises(ValueError):
            b = budget.Budget()
            b.awardBudgetCutProblem([10 for i in range(200)], 150)

    def test_raises_error_for_budgets_below_limit(self):
        with self.assertRaises(ValueError):
            b = budget.Budget()
            b.awardBudgetCutProblem([100, 20, 30], b.LOW_BUDGET - 1)

    def test_raises_error_for_budgets_above_limit(self):
        with self.assertRaises(ValueError):
            b = budget.Budget()
            b.awardBudgetCutProblem([100, 20, 30], b.HIGH_BUDGET + 1)

    def test_raises_error_for_grants_below_limit(self):
        with self.assertRaises(ValueError):
            b = budget.Budget()
            b.awardBudgetCutProblem([b.LOW_GRANT - 1, 20, 30], 150)

    def test_raises_error_for_grants_above_limit(self):
        with self.assertRaises(ValueError):
            b = budget.Budget()
            b.awardBudgetCutProblem([50, 20, b.HIGH_GRANT + 1], 150)

    def test_returns_no_limit_for_high_budget(self):
        b = budget.Budget()
        assert b.awardBudgetCutProblem([100, 20, 30], 180) == b.NO_LIMIT

    def test_returns_expected_value_for_low_budget(self):
        b = budget.Budget()
        assert b.awardBudgetCutProblem([100, 50, 200], 180) == 65
