from unittest import mock

from . import TestCommon
from ynab.transactions import Transactions

class CategoryTests(TestCommon):

    def setUp(self):

        self.client = Transactions(self.personal_token)

        self.mock_response = mock.Mock(status_code=200)
        self.mock_response.json.return_value = {
            "data": {
                "transactions": [
                    {
                        "id": "string",
                        "date": "string",
                        "amount": 0,
                        "memo": "string",
                        "cleared": "cleared",
                        "approved": True,
                        "flag_color": "red",
                        "account_id": "string",
                        "payee_id": "string",
                        "category_id": "string",
                        "transfer_account_id": "string",
                        "transfer_transaction_id": "string",
                        "matched_transaction_id": "string",
                        "import_id": "string",
                        "deleted": True,
                        "account_name": "string",
                        "payee_name": "string",
                        "category_name": "string",
                        "subtransactions": [
                            {
                                "id": "string",
                                "transaction_id": "string",
                                "amount": 0,
                                "memo": "string",
                                "payee_id": "string",
                                "payee_name": "string",
                                "category_id": "string",
                                "category_name": "string",
                                "transfer_account_id": "string",
                                "transfer_transaction_id": "string",
                                "deleted": True
                            }
                        ]
                    }
                ],
                "server_knowledge": 0,
            }
        }
    @mock.patch('requests.get')
    def test_get_transactions_by_budget_id(self, mock_get):

        mock_get.return_value = self.mock_response

        result = self.client.get_transactions_by_budget_id(self.budget_id)
        self.assertIsInstance(result, dict)
        self.assertIn('transactions', result.get('data').keys())
        self.assertIn('approved', result.get('data').get('transactions')[0])
