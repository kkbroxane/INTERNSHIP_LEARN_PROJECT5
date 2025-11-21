from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain.agents.factory import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from .tools import get_tools
from AI_Chatbot.settings import SYSTEM_PROMPT, LLAMA_GENERATION_MODEL, LLAMA_EMBEDDING_MODEL

memory = InMemorySaver()

def build_agent():

    llm = ChatOllama(
        model=LLAMA_GENERATION_MODEL,
        temperature=0.2,
        base_url="http://localhost:11434",
        keep_alive=0,          # 
        # num_ctx=8192,          # 
    )

    embeddings = OllamaEmbeddings(
        model=LLAMA_EMBEDDING_MODEL,
        base_url="http://localhost:11434",
    )

    tools = get_tools()

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
        checkpointer=memory,
        name='my_agent'
    )

    return agent


def debug_memory(thread_id):
    print("\n=== MEMORY DEBUG ===")

    try:
        checkpoints = memory.list({
            "namespace": "my_agent",
            "thread_id": thread_id
        })
    except Exception as e:
        print("Error calling list():", e)
        return

    if not checkpoints:
        print(f"\nNo memory found for thread_id={thread_id}\n")
        return

    print("\n=== CHECKPOINTS FOUND ===")
    print(checkpoints)

    for cp in checkpoints:
        try:
            data = memory.get({
                "namespace": cp["namespace"],
                "thread_id": cp["thread_id"],
                "checkpoint_id": cp["checkpoint_id"],
            })
        except Exception as e:
            print("Error calling get():", e)
            continue

        print("\n=== CHECKPOINT CONTENT ===")
        print(data)
        print("\n=========================")
