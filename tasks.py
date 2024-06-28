from textwrap import dedent
from crewai import Task
from tools import ExaSearchToolset


class NewsTasks:
    def fetch_news_task(self, agent, news_topic):
        return Task(
            description=dedent(f"""\
                Fetch the latest news articles and updates related to the specified topic.
                Gather information from various reliable news sources to ensure comprehensive coverage.

                News Topic: {news_topic}"""),
            expected_output=dedent(f"""\
                A collection of the latest news articles and updates related to the specified topic, 
                ensuring a wide range of perspectives and reliable information."""),
            agent=agent,
            async_execution=True,
            execute=lambda context: ExaSearchToolset.search(news_topic)
        )

    def analyze_news_task(self, agent, news_topic):
        return Task(
            description=dedent(f"""\
                Analyze the fetched news articles to identify key points, trends, and significant events 
                related to the specified topic. Summarize the findings in a concise and informative manner.

                News Topic: {news_topic}"""),
            expected_output=dedent("""\
                A detailed analysis and summary of the key points, trends, and significant events 
                from the fetched news articles."""),
            agent=agent,
            async_execution=True,
            execute=lambda context: ExaSearchToolset.get_contents(context['fetch_news_task'])
        )
