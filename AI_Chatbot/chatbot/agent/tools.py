from langchain.tools import tool
from chatbot.views_ai import search_properties
from chatbot.utils import answer_from_db

@tool
def search_properties_tool(user_query: str, property_type: str, top_k: int = 3):
    """Cherche des propriétés en fonction du type et de la requête. Utile uniquement lorsque la demande concerne des propriétés immobilières."""
    return search_properties(user_query, property_type, top_k=top_k)

@tool
def answer_from_db_tool(user_query: str, results):
    """Génère la réponse finale en utilisant les résultats trouvés. Utile uniquement pour les questions liées à l'immobilier."""
    return answer_from_db(user_query, results)

def get_tools():
    return [
        search_properties_tool,
        answer_from_db_tool,
    ]
