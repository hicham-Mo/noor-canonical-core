# Noor Canonical Core

🌟 نور الاستخلاف - نظام متكامل للمعرفة والإنتاج والاستثمار الشرعي

A FastAPI-based foundation for a lawful, compliant, and technically reliable project stack. This repository provides a solid base for building AI-assisted, data-aware applications with checks for:

- Moroccan data protection compliance (Loi 42.25)
- Islamic-friendly business constraints
- Cloud configuration validation
- Secure environment configuration
- Health and compliance API endpoints

## Project status

This repository now includes:

- FastAPI application scaffold
- Environment configuration with `.env.example`
- Basic health and compliance routes
- Validation helpers for legal and cloud requirements
- Initial test setup

## Quick start

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy environment variables:
   ```bash
   cp .env.example .env
   ```

4. Run the app:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

5. Open the docs:
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## Included endpoints

- `GET /`
- `GET /health`
- `GET /ready`
- `GET /compliance/law-42-25`
- `GET /compliance/islamic`
- `GET /compliance/cloud`

## Compliance notes

This code is structured as a lawful technical foundation and uses a conservative, transparent approach for handling sensitive data and operational rules. It does not replace legal advice; it provides implementation scaffolding aligned with the project’s stated compliance goals.

## License

MIT
