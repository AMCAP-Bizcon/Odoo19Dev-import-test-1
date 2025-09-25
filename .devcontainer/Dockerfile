FROM odoo:19

# Optional: add tools you like inside the dev container
RUN apt-get update && apt-get install -y --no-install-recommends \
    nano less git make curl \
 && rm -rf /var/lib/apt/lists/*

# (If you use private Enterprise repos, you can later add SSH keys via VS Code)

