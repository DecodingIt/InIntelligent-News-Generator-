from textwrap import dedent
from crewai import Agent


class NewsAgents:
    def news_fetch_agent(self):
        return Agent(
            role="News Fetcher",
            goal='Fetch the latest news articles and updates on specified topics',
            backstory=dedent("""\
                As a News Fetcher, your mission is to gather the most recent and relevant news articles 
                on specified topics from a variety of reliable sources. Your work ensures comprehensive 
                coverage and up-to-date information."""),
            verbose=True
        )

    def news_analysis_agent(self):
        return Agent(
            role='News Analyst',
            goal='Analyze the fetched news articles to summarize key points and trends',
            backstory=dedent("""\
                As a News Analyst, your role is to critically analyze the fetched news articles, 
                identifying key points, trends, and significant events. Your summaries will provide 
                valuable insights and a clear understanding of the news landscape."""),
            verbose=True
        )
