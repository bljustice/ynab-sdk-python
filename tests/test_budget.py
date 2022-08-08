import os
from unittest import mock

from . import TestCommon
from ynab.budgets import Budgets

class BudgetTests(TestCommon):

    def setUp(self):

        self.client = Budgets(self.personal_token)

        self.mock_response = mock.Mock(status_code=200)
        self.mock_response.json.return_value = {
            'data': {
                'budgets': [
                    {'id': 'c123-109b',
                    'name': 'budget',
                    'last_modified_on': '2022-08-07T16:53:27+00:00',
                    'first_month': '2018-07-01',
                    'last_month': '2022-08-01',
                    'date_format': {
                        'format': 'MM/DD/YYYY'
                    },
                    'currency_format': {
                        'iso_code': 'USD',
                        'example_format': '123,456.78',
                        'decimal_digits': 2,
                        'decimal_separator': '.',
                        'symbol_first': True,
                        'group_separator': ',',
                        'currency_symbol': '$',
                        'display_symbol': True
                        }
                    }
                ], 
                'default_budget': None
            }
        }

    @mock.patch('requests.get')
    def test_get_all_budgets(self, mock_get):

        mock_get.return_value = self.mock_response

        result = self.client.get_all_budgets()
        self.assertIsInstance(result, dict)
        self.assertIn('data', result.keys())

    @mock.patch('requests.get')
    def test_get_budget_by_id(self, mock_get):
        
        mock_get.return_value = self.mock_response

        result = self.client.get_budget_by_id(self.budget_id)
        self.assertIsInstance(result, dict)
        self.assertIn('budgets', result.get('data'))
        self.assertIn('id', result.get('data').get('budgets')[0])
        