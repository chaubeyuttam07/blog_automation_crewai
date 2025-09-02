from crewai import Agent, LLM


ollama_llm = LLM(
    model="ollama/gpt-oss:20b",   
    base_url="http://localhost:11434", 
    temperature=0.7
)



youtube_script_writer = Agent(
    role="YouTube Script Writer",
    goal="Write engaging YouTube scripts from given topics",
    backstory="Creative content creator specializing in YouTube.",
    llm=ollama_llm,   
    allow_delegation=False,
    verbose=True
)


blog_writer = Agent(
    role="Blog Writer",
    goal="Expand YouTube scripts into detailed blog articles",
    backstory="Professional content writer who crafts compelling blog posts.",
    llm=ollama_llm, 
    allow_delegation=False,
    verbose=True
)
