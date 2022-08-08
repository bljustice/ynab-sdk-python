import os
from unittest import mock

from . import TestCommon
from ynab.accounts import Accounts

class AccountTests(TestCommon):

    def setUp(self):

        self.client = Accounts(self.personal_token)

        self.mock_response = mock.Mock(status_code=200)
        self.mock_response.json.return_value = {
            'data': {
                'accounts': [
                    {
                        'id': 'be09-8df', 
                        'name': 'Checking',
                        'type': 'checking', 
                        'on_budget': True,
                        'closed': True,
                        'note': None,
                        'balance': 0,
                        'cleared_balance': 0,
                        'uncleared_balance': 0,
                        'transfer_payee_id': 'df7c-3191-cab', 
                        'direct_import_linked': False,
                        'direct_import_in_error': False,
                        'deleted': False
                    }
                ]
            }
        }

    @mock.patch('requests.get')
    def test_get_accounts_by_budget_id(self, mock_get):

        mock_get.return_value = self.mock_response

        result = self.client.get_accounts_by_budget_id('e13904-a485')
        self.assertIsInstance(result, dict)
        self.assertIn('data', result.keys())
        self.assertIn('balance', result.get('data').get('accounts')[0])
        