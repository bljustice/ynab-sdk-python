from ynab import YNABClient

class Budgets(YNABClient):

    def __init__(self, personal_token):

        super(Budgets, self).__init__(personal_token)
        self.endpoint = 'budgets'

    def get_all_budgets(self):
        """
        Gets all budgets for a given personal YNAB token
        """

        params = {
            'include_accounts': 'true',
        }
        r = self._make_request(self.endpoint, **params)
        r.raise_for_status()
        return r.json()

    def get_budget_by_id(self, budget_id: str) -> dict:
        """
        Gets budget data by budget ID
        """
        budget_by_id_endpoint = f'{self.endpoint}/{budget_id}'
        r = self._make_request(budget_by_id_endpoint)
        r.raise_for_status()
        return r.json()
