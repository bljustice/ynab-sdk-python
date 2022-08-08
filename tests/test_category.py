from unittest import mock

from . import TestCommon
from ynab.categories import Categories

class CategoryTests(TestCommon):

    def setUp(self):

        self.client = Categories(self.personal_token)

        self.mock_response = mock.Mock(status_code=200)
        self.mock_response.json.return_value = {
            'data': {
                'category_groups': [
                    {
                        'id': 'b828f-940c-b954',
                        'name': 'Internal Master Category',
                        'hidden': False,
                        'deleted': False,
                        'categories': [
                            {   
                                'id': '15f436-6606-f9c21',
                                'category_group_id': 'b828-f269-413',
                                'name': 'Inflow: Ready to Assign',
                                'hidden': False,
                                'original_category_group_id': None,
                                'note': None,
                                'budgeted': 0,
                                'activity': 0,
                                'balance': 100000,
                                'goal_type': None,
                                'goal_creation_month': None,
                                'goal_target': 0,
                                'goal_target_month': None,
                                'goal_percentage_complete': None,
                                'goal_months_to_budget': None,
                                'goal_under_funded': None,
                                'goal_overall_funded': None,
                                'goal_overall_left': None,
                                'deleted': False
                            }
                        ]
                    }
                ]
            }
        }

    @mock.patch('requests.get')
    def test_get_categories_by_budget_id(self, mock_get):

        mock_get.return_value = self.mock_response

        result = self.client.get_categories_by_budget_id(self.budget_id)
        self.assertIsInstance(result, dict)
        self.assertIn('category_groups', result.get('data').keys())
        self.assertEqual(len(result.keys()), 1)
