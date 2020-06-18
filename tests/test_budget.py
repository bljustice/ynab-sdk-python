from . import TestCommon
from ynab.budgets import Budget

class BudgetTests(TestCommon):

    def setUp(self):

        self.client = Budget(self.personal_token)

    def test_get_all_budgets(self):

        result = self.client.get_all_budgets()
        self.assertIsInstance(result, dict)
        self.assertIn('data', result.keys())