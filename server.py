from mcp.server.fastmcp import FastMCP
from openai import OpenAI
import tempfile
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

VECTOR_STORE_NAME = "memories"

mcp = FastMCP("Memories")


def get_or_create_vector_store():
    stores = client.vector_stores.list()
    for store in stores:
        if store.name == VECTOR_STORE_NAME:
            return store
    return client.vector_stores.create(name=VECTOR_STORE_NAME)


@mcp.tool()
def save_memory(memory: str):
    """Save a memory to the vector store."""
    vector_store = get_or_create_vector_store()
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".txt") as f:
        f.write(memory)
        f.flush()
        client.vector_stores.files.upload_and_poll(

            vector_store_id=vector_store.id,
            file=open(f.name, "rb"),
        )
    return {"status": "saved", "vector store id": vector_store.id}


@mcp.tool()
def search_memories(query: str):
    """Search the vector store for memories that match the query."""
    vector_store = get_or_create_vector_store()
    print(vector_store.id)
    results = client.vector_stores.search(
        vector_store_id=vector_store.id,
        query=query,     
    )
    print(results)
    
    # Handle SyncPage response - iterate through the data
    content_text = []
    for item in results.data:
        if hasattr(item, 'content'):
            for content in item.content:
                if content.type == "text":
                    content_text.append(content.text)
    
    return {"status": "success", "results": content_text}




if __name__ == "__main__":
    mcp.run(transport="stdio")