# Secure Python App w/ DevSecOps Pipeline

A Flask app demonstrating shift-left security: Dockerized, scanned for vulns, and automated via GitHub Actions.

## Features
- Python/Flask backend
- Secure Docker build (non-root)
- Automated scans: Bandit (code) + Trivy (containers)

## Quick Start
docker build -t secure-app .
docker run -p 5000:5000 secure-app
