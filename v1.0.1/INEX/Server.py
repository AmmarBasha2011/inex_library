from flask import Flask

class Server:
    """
    A class for creating and running a Flask server.

    Attributes:
    - app: Holds the Flask application instance.
    """

    def __init__(self):
        """
        Initializes the server instance with None.
        """
        self.apps = None

    def route_flask(self, location="", returnValue=""):
        """
        Adds a route to the Flask application.

        Args:
        - location: URL endpoint for the route.
        - returnValue: Value returned by the route function.

        Returns:
        - 'done' if route addition is successful.
        """
        app = self.apps
        try:
            if app is None:
                app = Flask(__name__)

            def make_route(return_value):
                def route():
                    return return_value
                return route

            endpoint = location.strip('/')
            if endpoint == '':
                endpoint = 'index'

            app.add_url_rule(location, endpoint, make_route(returnValue))
            apps = app
            return 'done'
        except Exception as error:
            raise error
        
    def run(self, check=False, debug=True, host="0.0.0.0", port="8000"):
        """
        Starts the Flask server.

        Args:
        - check: If True, runs only if __name__ == "__main__".
        - debug: Enables debug mode if True.
        - host: Host IP address to run the server on.
        - port: Port number to run the server on.

        Returns:
        - 'done' if server starts successfully.
        """
        app = self.apps
        try:
            if app is None:
                raise Exception("App not initialized")
            
            if check:
                if __name__ == "__main__":
                    app.run(debug=debug, host=host, port=port)
            else:
                app.run(debug=debug, host=host, port=port)
            return 'done'
        except Exception as error:
            raise error
