from ynab.client import YNABClient

class Budgets(YNABClient):

    def __init__(self, personal_token):

        super(Budgets, self).__init__(personal_token)

    def get_all_budgets(self):
        """
        Gets all budgets for a given personal YNAB token
        """

        r = self._make_request('')
        r.raise_for_status()
        return r.json()

    def get_budget_by_id(self, budget_id: str) -> dict:
        """
        Gets budget data by budget ID
        """
        r = self._make_request(budget_id)
        r.raise_for_status()
        return r.json()
