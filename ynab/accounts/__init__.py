from typing import Dict

from ynab.client import YNABClient

class Accounts(YNABClient):

    def __init__(self, personal_token):

        super(Accounts, self).__init__(personal_token)

    def get_accounts_by_budget_id(self, budget_id: str) -> Dict:
        """
        Gets all accounts for a given budget id
        """
        endpoint = f'{budget_id}/accounts'
        r = self._make_request(endpoint)
        r.raise_for_status()
        return r.json()
