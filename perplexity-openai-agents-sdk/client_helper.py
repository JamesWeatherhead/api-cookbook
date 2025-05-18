import os
from openai import AsyncOpenAI

DEFAULT_BASE_URL = os.getenv("EXAMPLE_BASE_URL") or "https://api.perplexity.ai"
DEFAULT_API_KEY = os.getenv("EXAMPLE_API_KEY")
API_VERSION = os.getenv("EXAMPLE_API_VERSION") or "v1"

def get_async_client(
    base_url: str | None = None,
    api_key: str | None = None,
    api_version: str | None = None,
) -> AsyncOpenAI:
    """Return a shared AsyncOpenAI client configured for the Sonar API."""
    base_url = base_url or DEFAULT_BASE_URL
    api_key = api_key or DEFAULT_API_KEY
    api_version = api_version or API_VERSION
    if not api_key:
        raise ValueError("EXAMPLE_API_KEY must be set via environment or argument")
    if api_version and not base_url.rstrip("/").endswith(api_version):
        base_url = base_url.rstrip("/") + f"/{api_version}"
    return AsyncOpenAI(base_url=base_url, api_key=api_key)
