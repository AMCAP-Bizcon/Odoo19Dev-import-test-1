# Wrapper image so Codespaces can use the odoo service as the devcontainer
FROM odoo:19

USER root

# Handy tools; keep it slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    nano less git curl procps iproute2 \
 && rm -rf /var/lib/apt/lists/*

# Make sure the common mount point is present
RUN mkdir -p /workspaces && chown -R root:root /workspaces

# Stay root as remote user for fewer permission surprises in Codespaces
USER root
