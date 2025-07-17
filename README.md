# MCP Memory Tracker

A Model Context Protocol (MCP) server that provides persistent memory capabilities using OpenAI's vector stores. This allows AI assistants to save and search through memories across conversations.

## Features

- **Save Memories**: Store text-based memories in OpenAI vector stores
- **Search Memories**: Semantic search through saved memories using natural language queries
- **Persistent Storage**: Memories are stored in OpenAI's cloud infrastructure
- **MCP Compatible**: Works with any MCP-compatible client (like Claude Desktop)

## Prerequisites

- Python 3.8+
- OpenAI API key
- UV package manager (recommended) or pip

## Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd mcp-memory-tracker
```

2. **Install dependencies**:
```bash
# Using UV (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

3. **Set up environment variables**:
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Running the MCP Server

```bash
# Using UV
uv run server.py

# Or using Python directly
python server.py
```

### Available Tools

#### `save_memory(memory: str)`
Saves a text memory to the vector store.

**Parameters:**
- `memory` (string): The text content to save

**Returns:**
```json
{
  "status": "saved",
  "vector store id": "vs_xxxxx"
}
```

**Example:**
```python
save_memory("I met John at the coffee shop on Main Street. He's a software engineer who loves hiking.")
```

#### `search_memories(query: str)`
Searches through saved memories using semantic search.

**Parameters:**
- `query` (string): Natural language search query

**Returns:**
```json
{
  "status": "success",
  "results": ["matching memory content..."]
}
```

**Example:**
```python
search_memories("Who did I meet at the coffee shop?")
```

## Integration with MCP Clients

### Claude Desktop

Add this server to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "memory-tracker": {
      "command": "uv",
      "args": ["run", "/path/to/mcp-memory-tracker/server.py"],
      "env": {
        "OPENAI_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### Other MCP Clients

This server implements the standard MCP protocol and should work with any compatible client. Refer to your client's documentation for configuration details.

## How It Works

1. **Vector Store Management**: The server automatically creates and manages an OpenAI vector store named "memories"
2. **Memory Storage**: When you save a memory, it's uploaded as a text file to the vector store
3. **Semantic Search**: The search functionality uses OpenAI's vector search capabilities to find relevant memories based on meaning, not just keywords

## Configuration

The server uses the following constants that can be modified in `server.py`:

- `VECTOR_STORE_NAME`: Name of the OpenAI vector store (default: "memories")

## Dependencies

- `fastmcp`: MCP server framework
- `openai`: OpenAI Python SDK
- `python-dotenv`: Environment variable management

## Troubleshooting

### Common Issues

1. **"OPENAI_API_KEY not found"**: Make sure your `.env` file is properly configured
2. **"'SyncPage' object has no attribute..."**: This indicates an API response structure issue - check your OpenAI SDK version
3. **File upload errors**: Ensure your OpenAI API key has vector store permissions

### Debug Mode

Add print statements to see detailed responses:
```python
print(f"Vector store ID: {vector_store.id}")
print(f"Search results: {results}")
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

[Add your license here]

## Support

For issues and questions:
- Check the [troubleshooting section](#troubleshooting)
- Review OpenAI API documentation
- Check MCP protocol documentation
