from Websites import Websites
from typing import Any

class Crypto:
    @staticmethod
    def token_information(data: Any = "", type: str = 'binance') -> str:
        """
        Opens a web browser with token information based on the type.

        Args:
        - data (Any): Token identifier or data.
        - type (str): Type of token platform ('binance', 'etherum', 'geckoterminal').

        Returns:
        - str: Message indicating if the operation was successful or unsupported type.
        """
        if type == 'binance':
            link = "https://bscscan.com/token/" + str(data)
            Websites.open_website(link)
            return "opened"
        elif type == 'etherum':
            link = "https://etherscan.io/token/" + str(data)
            Websites.open_website(link)
            return "opened"
        elif type == 'geckoterminal':
            link = 'https://ywp.freewebhostmost.com/really/token.php?pool=' + str(data)
            Websites.open_website(link)
            return "opened"
        else:
            return "Unsupported type"