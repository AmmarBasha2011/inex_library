from fastapi import FastAPI
from typing import Callable

class FastAPIServer:
    """
    A class to create a FastAPI server.
    """

    def __init__(self):
        """
        Initializes a FastAPI server.
        """
        self.app = FastAPI()

    def add_endpoint(self, path: str, function: Callable, method: str = "GET"):
        """
        Adds a new endpoint to the server.

        Args:
        - path (str): The path of the endpoint.
        - function (Callable): The function to be called when the endpoint is accessed.
        - method (str): The HTTP method to use (default: "GET").
        """
        self.app.add_api_route(path=path, methods=[method], endpoint=lambda request: function(**request.query_params))

    def add_cors(self):
        """
        Adds CORS support to the server.
        """
        from fastapi.middleware.cors import CORSMiddleware

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def run(self, host: str = "0.0.0.0", port: int = 8000):
        """
        Starts the FastAPI server.

        Args:
        - host (str): The host to listen to (default: "0.0.0.0").
        - port (int): The port to listen to (default: 8000).
        """
        import uvicorn
        uvicorn.run(self.app, host=host, port=port)