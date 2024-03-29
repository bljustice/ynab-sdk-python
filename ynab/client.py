import requests

class YNABClient:
    """
    Base YNAB API client that is used as the building block
    for subsets of the YNAB API
    """

    def __init__(self, personal_token: str) -> None:

        self.personal_token = personal_token

    def _make_bearer_header(self) -> dict:
        """
        Makes personal token header to pass in HTTP requests
        """
        return {
            'accept': 'application/json',
            'Authorization': f'Bearer {self.personal_token}'
        }

    def _make_request(self, api_endpoint: str, **kwargs) -> requests.Response:
        """
        Build and make a GET request to subsection of YNAB API
        """
        bearer_header = self._make_bearer_header()
        final_endpoint = f'https://api.youneedabudget.com/v1/budgets/{api_endpoint}'
        r = requests.get(final_endpoint, params={**kwargs}, headers=bearer_header)
        return r
