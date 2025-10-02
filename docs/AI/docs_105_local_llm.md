# Ollama

Ollama is an open-source LLM runtime environment.

Here is a docker compose that runs it all. 
Save this to a file called ``docker-compose.yaml``.

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

Run the docker compose file with ``docker compose up -d``.

You can go to [https://localhost:3000](https://localhost:3000) to use the web ui or you can use the API.

API call:

```http
### Generate text with llama3
POST http://localhost:11434/api/generate
Content-Type: application/json

{
  "model": "llama3",
  "prompt": "Write a haiku about data pipelines"
}
```

```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama3", "prompt": "Hello from PyCharm!"}
)

for line in response.iter_lines():
    if line:
        print(line.decode())
```

Available models can be found here:
https://registry.ollama.ai/search

To download other models:
```http
POST http://localhost:11434/api/pull
Content-Type: application/json

{
  "name": "mistral"
}
```

or download a model with the docker command: 
```bash
# download mistral model
docker exec -it ollama ollama pull mistral
# download llama3 model
docker exec -it ollama ollama pull llama3
```

For more info on the REST API definition: https://github.com/ollama/ollama/blob/main/docs/api.md

