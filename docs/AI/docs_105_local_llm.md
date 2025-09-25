# Ollama

Ollama is an open-source LLM runtime environment. 

Simply put:

1. Rum Ollama
2. Download the model you'd like to use (mistral, llama3, etc.)
3. Go to the WebUI
4. Select the model you want to use.
5. Chat away!

Download a model: ``docker exec -it ollama ollama pull mistral`` or ``docker exec -it ollama ollama pull llama3``

Here is a docker compose file that runs it:

```yaml
services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    restart: unless-stopped
    ports:
      - "11434:11434"   # Ollama API exposed
    volumes:
      - ollama_data:/root/.ollama  # Persist models

  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    restart: unless-stopped
    ports:
      - "3000:8080"   # WebUI runs here
    environment:
      - OLLAMA_API_BASE_URL=http://ollama:11434
    depends_on:
      - ollama

volumes:
  ollama_data:

```