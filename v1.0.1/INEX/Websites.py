import webbrowser

class Websites:
    @staticmethod
    def open_website(url=""):
        """
        Opens a website in the default web browser.

        Args:
        - url: The URL of the website to open.

        Returns:
        - 'opened' if successful.
        - Error message if unsuccessful.
        """
        try:
            webbrowser.open(url)
            return "opened"
        except Exception as e:
            print("An error occurred:", e)
            return "An error occurred:", e