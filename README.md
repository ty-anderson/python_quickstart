# Tech Notes

A comprehensive collection of technical documentation and guides covering software development, infrastructure, and system administration topics.

## About

This repository contains detailed technical notes and tutorials on various technology topics, organized as a static documentation site built with MkDocs Material. The content is designed to serve as both a learning resource and a quick reference for developers and system administrators.

## Topics Covered

### Python
- Complete introduction from basics to advanced topics
- Important libraries and standard library gems
- Testing, deployment, and publishing projects
- Tools like `uv` and documentation libraries

### DevOps & Infrastructure
- **Docker**: Containers, Compose, and creating images
- **Git & GitHub**: Version control fundamentals, branching, and remotes
- **Linux**: Command line, SSH, and backup strategies
- **Networking**: General networking concepts, servers, DNS, and Caddy reverse proxy

### Self-Hosting
Guides for hosting your own services including:
- NAS and storage solutions (Samba, Syncthing)
- Media servers (Plex/Jellyfin)
- Security cameras (Frigate)
- VPN (WireGuard)
- AI models (Ollama)

### Additional Topics
- **AI**: Local LLM hosting and Model Context Protocol (MCP)
- **Databases**: DuckDB and other database systems
- **Video Processing**: FFmpeg and streaming
- **Low-Level Programming**: Drivers and foundations
- **Rust**: Getting started with Rust
- **Windows Administration**: Password policies and system management

## Viewing the Documentation

The documentation is published at: [https://ty-anderson.github.io/python_quickstart/](https://ty-anderson.github.io/python_quickstart/)

Alternatively, hosted at: [https://healthfin.solutions/notes/](https://healthfin.solutions/notes/)

## Local Development

### Prerequisites
- Python 3.x
- pip

### Setup and Run

1. Clone the repository:
```bash
git clone https://github.com/ty-anderson/python_quickstart.git
cd python_quickstart
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Serve the documentation locally:
```bash
mkdocs serve
```

4. Open your browser to `http://127.0.0.1:8000`

### Building the Site

To build the static site:
```bash
mkdocs build
```

The built site will be available in the `site/` directory.

## Project Structure

```
.
├── docs/              # Markdown documentation files
│   ├── Python/        # Python tutorials and guides
│   ├── Git/           # Git and version control
│   ├── Docker/        # Container documentation
│   ├── self_host/     # Self-hosting guides
│   ├── Networking/    # Network configuration
│   ├── AI/            # AI and ML topics
│   └── ...
├── mkdocs.yml         # MkDocs configuration
└── README.md          # This file
```

## Contributing

This is a personal knowledge base, but suggestions and corrections are welcome via issues or pull requests.

## License

Content is provided as-is for educational purposes.