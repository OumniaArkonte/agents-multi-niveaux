import os
from dotenv import load_dotenv
from agno.models.google import Gemini
from agno.agent import Agent, Memory
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.shell import ShellTools

def main():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Erreur : la clé API GOOGLE_API_KEY n'est pas définie.")
        return

    print("Clé API chargée :", True)

    finance_memory = Memory()

    tools = [
        DuckDuckGoTools(),
        ShellTools(),
    ]

    finance_agent = Agent(
        model=Gemini(id="gemini-1.5-flash", api_key=api_key),
        instructions=(
            "Tu es un expert en Finance et Banque. "
            "Tes missions : analyser des données financières et produire des rapports clairs."
        ),
        memory=finance_memory,
        tools=tools,
        reasoning=True,
    )

    # Transactions prédéfinies (plus besoin de saisir au clavier)
    transactions = [
        {"transaction": "achat", "montant": 1000, "type": "dépense"},
        {"transaction": "vente", "montant": 1500, "type": "revenu"}
    ]

    # 1. Explication concept financier
    response1 = finance_agent.run(
        "Explique-moi simplement la différence entre liquidité et solvabilité en finance."
    )
    print("\n--- Explication concept ---\n")
    print(response1.content if hasattr(response1, "content") else response1)

    # 2. Analyse des transactions
    response2 = finance_agent.run(f"Analyse ces transactions : {transactions}")
    print("\n--- Analyse des transactions ---\n")
    print(response2.content if hasattr(response2, "content") else response2)

    # 3. Rapport pédagogique
    response3 = finance_agent.run(
        "Rédige un rapport synthétique en Markdown sur les principaux risques bancaires "
        "(crédit, liquidité, marché, opérationnel) et propose des solutions."
    )
    print("\n--- Rapport pédagogique ---\n")
    print(response3.content if hasattr(response3, "content") else response3)

if __name__ == "__main__":
    main()
