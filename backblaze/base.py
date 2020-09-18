from httpx import BasicAuth

from .routes import Auth


class Base:
    def __init__(self, key_id: str, key: str,
                 auth_url: str = "https://api.backblazeb2.com/b2api/v2/"
                 ) -> None:
        """Used to interact with B2 account.

        Parameters
        ----------
        key_id : str
            Application Key ID.
        key : str
            Application Key
        """

        self._auth = BasicAuth(
            key_id,
            key
        )

        self.auth_url = auth_url

    def format_routes(self, api_url: str, download_url: str) -> None:
        pass

    @property
    def _auth_url(self) -> str:
        auth = Auth(self.auth_url)
        auth.format()

        return auth.get
