from __future__ import annotations

from typing import Any, Dict, List


def moroccan_law_42_25() -> Dict[str, Any]:
    return {
        "law": "Loi 42.25",
        "title": "Protection of personal data",
        "requirements": [
            "Data processing must be lawful and transparent.",
            "Collection must be limited to specified purposes.",
            "Individuals have rights to access, correct, and delete their data.",
            "Retention periods must be defined and enforced.",
            "Data processors must be clearly designated.",
            "Security incidents should be notified within 72 hours where required.",
        ],
        "status": "requires-implementation",
    }


def islamic_compliance() -> Dict[str, Any]:
    return {
        "principles": [
            "Avoid riba (interest-based finance).",
            "Avoid gharar (excessive uncertainty).",
            "Avoid maysir (gambling-like risk).",
            "Prefer halal revenue streams.",
            "Maintain transparency and fairness.",
        ],
        "forbidden_sectors": [
            "Alcohol and tobacco",
            "Gambling and casinos",
            "Pork-related supply chains",
            "Prohibited weapons operations",
            "Conventional interest-based banking",
        ],
    }


def cloud_configuration_summary() -> Dict[str, Any]:
    import os

    provider = os.getenv("CLOUD_PROVIDER", "local").strip().lower()

    summary: Dict[str, Any] = {
        "provider": provider,
        "valid": True,
        "issues": [],
    }

    if provider == "aws":
        if not os.getenv("AWS_ACCESS_KEY_ID") or not os.getenv("AWS_SECRET_ACCESS_KEY"):
            summary["valid"] = False
            summary["issues"].append("AWS credentials are missing.")
        if not os.getenv("AWS_S3_BUCKET"):
            summary["valid"] = False
            summary["issues"].append("AWS S3 bucket is missing.")
    elif provider == "azure":
        if not os.getenv("AZURE_STORAGE_CONNECTION_STRING"):
            summary["valid"] = False
            summary["issues"].append("Azure connection string is missing.")
    elif provider == "gcp":
        if not os.getenv("GCP_PROJECT_ID"):
            summary["valid"] = False
            summary["issues"].append("GCP project ID is missing.")

    return summary
