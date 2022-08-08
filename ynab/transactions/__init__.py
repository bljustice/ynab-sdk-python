from typing import Dict

from ynab.client import YNABClient

class Transactions(YNABClient):

    def __init__(self, personal_token):

        super(Transactions, self).__init__(personal_token)

    def get_transactions_by_budget_id(self, budget_id: str, since_date: str='') -> Dict:
        """
        Gets all accounts for a given budget id
        """
        if since_date:
            params = {
                'since_date': since_date
            }
        else:
            params = {}
        endpoint = f'{budget_id}/transactions'
        r = self._make_request(endpoint, **params)
        r.raise_for_status()
        return r.json()
