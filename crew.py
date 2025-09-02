from crewai import Crew, Process
from agents import youtube_script_writer, blog_writer
from tasks import script_writing_task, blog_writing_task

def main():

    crew = Crew(
        agents=[youtube_script_writer, blog_writer],
        tasks=[script_writing_task, blog_writing_task],
        process=Process.sequential
    )

 
    crew.kickoff()

if __name__ == "__main__":
    main()
