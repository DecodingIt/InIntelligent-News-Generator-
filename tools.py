import os
from exa_py import Exa

class ExaSearchToolset:
    @classmethod
    def search(cls, query: str):
        """Search for news articles based on the query."""
        return cls._exa().search(f"{query}", use_autoprompt=True, num_results=3)

    @classmethod
    def find_similar(cls, url: str):
        """Search for news articles similar to a given URL.
        The URL passed in should be a URL returned from 'search'.
        """
        return cls._exa().find_similar(url, num_results=3)

    @classmethod
    def get_contents(cls, ids: str):
        """Get the contents of a news article.
        The IDs must be passed in as a list, a list of IDs returned from 'search'.
        """
        if isinstance(ids, str):
            ids = eval(ids)  # Ensure ids is evaluated from string format to list

        if not isinstance(ids, list):
            raise ValueError("The 'ids' parameter must be a list or a string representation of a list.")

        contents = str(cls._exa().get_contents(ids))
        contents = contents.split("URL:")
        contents = [content[:1000] for content in contents]
        return "\n\n".join(contents)

    @classmethod
    def tools(cls):
        return [
            cls.search,
            cls.find_similar,
            cls.get_contents
        ]

    @classmethod
    def _exa(cls):
        return Exa(api_key=os.environ.get('EXA_API_KEY'))
