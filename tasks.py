from crewai import Task
from agents import youtube_script_writer, blog_writer


script_writing_task = Task(
    description="Write a detailed YouTube script for the topic: 'The Future of AI Agents'",
    agent=youtube_script_writer,
    expected_output="A conversational YouTube script with intro, body, and outro."
)


blog_writing_task = Task(
    description="Expand the YouTube script into a blog post with SEO-friendly structure.",
    agent=blog_writer,
    expected_output="A detailed blog article with proper headings and explanations.",
     max_tokens=800  
)
