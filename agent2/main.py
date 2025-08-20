import os
from dotenv import load_dotenv
from agno.models.google import Gemini
from agno.agent import Agent, Memory
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.file import FileTools

def main():
    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Erreur : la clé API GOOGLE_API_KEY n'est pas définie.")
        return

    print("Clé API chargée :", True)

    # Mémoire pour garder le contexte
    agent_memory = Memory()  


    tools = [
        DuckDuckGoTools(),  
        FileTools(),       
    ]

    # Agent pédagogique avancé
    reasoning_agent = Agent(
        model=Gemini(id="gemini-1.5-flash", api_key=api_key),
        instructions=(
            "Tu es un assistant pédagogique avancé spécialisé en cybersécurité. "
            "Tu dois : \n"
            "- Fournir des explications détaillées et pédagogiques.\n"
            "- Raisonner étape par étape.\n"
            "- Donner des exemples concrets.\n"
            "- Proposer des conseils pratiques.\n"
            "- Utiliser la mémoire pour garder le contexte.\n"
            "- Si nécessaire, utiliser la recherche web pour trouver des infos récentes.\n"
            "- Pouvoir générer des rapports pédagogiques en PDF ou Markdown."
        ),
        memory=agent_memory,
        tools=tools,
        reasoning=False  
    )

    # Exemple d’interactions
    try:
        response1 = reasoning_agent.run(
            "Explique-moi ce qu’est le phishing en cybersécurité avec des exemples récents."
        )
        print("\n--- Réponse 1 ---\n")
        print(response1.content if hasattr(response1, "content") else response1)

        response2 = reasoning_agent.run(
            "Donne-moi les étapes pratiques pour détecter un email suspect."
        )
        print("\n--- Réponse 2 ---\n")
        print(response2.content if hasattr(response2, "content") else response2)

        response3 = reasoning_agent.run(
            "Crée un rapport pédagogique en Markdown expliquant le phishing, "
            "les techniques des attaquants et les bonnes pratiques de protection. "
            "Enregistre-le sous le nom 'rapport_phishing.md'."
        )
        print("\n--- Rapport généré ---\n")
        print(response3.content if hasattr(response3, "content") else response3)

    except Exception as e:
        print("Erreur lors de l'exécution de l'agent :", e)

if __name__ == "__main__":
    main()
