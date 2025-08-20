import os
from dotenv import load_dotenv
from agno.models.google import Gemini
from agno.agent import Agent

load_dotenv()

# clé API
print("Clé API chargée :", os.getenv("GOOGLE_API_KEY") is not None)

# Agent niveau 1 : simple explication
simple_agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    instructions="Tu es un assistant pédagogique qui explique simplement."
    
)

if __name__ == "__main__":
    response = simple_agent.run("Explique-moi ce qu’est le phishing en cybersécurité.")
    if hasattr(response, "content"):
        print(response.content)
    else:
        print(response)

