from dotenv import load_dotenv
from crewai import Crew
from agents import NewsAgents
from tasks import NewsTasks
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

def main():
    load_dotenv()
    print(" Welcome to the News Fetcher")
    print(" --------------------------")
    news_topic = input("What topic do you want the latest news about?\n")

    tasks = NewsTasks()
    agents = NewsAgents()

    news_fetch_agent = agents.news_fetch_agent()
    news_analysis_agent = agents.news_analysis_agent()

    fetch_news_task = tasks.fetch_news_task(news_fetch_agent, news_topic)
    analyze_news_task = tasks.analyze_news_task(news_analysis_agent, news_topic)

    analyze_news_task.context = [fetch_news_task]

    crew = Crew(
        agents=[
            news_fetch_agent,
            news_analysis_agent
        ],
        tasks=[
            fetch_news_task,
            analyze_news_task
        ]
    )

    result = crew.kickoff()

    print(result)

if __name__ == "__main__":
    main()
    scheduler.start()
