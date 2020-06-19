import os

from . import TestCommon
from ynab.budgets import Budgets

class BudgetTests(TestCommon):

    def setUp(self):

        self.client = Budgets(self.personal_token)
        self.budget_id = os.environ['YNAB_BUDGET_ID']

    def test_get_all_budgets(self):

        result = self.client.get_all_budgets()
        self.assertIsInstance(result, dict)
        self.assertIn('data', result.keys())

    def test_get_budget_by_id(self):

        result = self.client.get_budget_by_id(self.budget_id)
        self.assertIsInstance(result, dict)
        self.assertIn('budget', result.get('data'))
        self.assertIn('payees', result.get('data').get('budget'))
        