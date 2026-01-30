import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    app_env: str = os.getenv("APP_ENV", "dev")
    llm_provider: str = os.getenv("LLM_PROVIDER", "stub").lower()
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    max_context_chunks: int = int(os.getenv("MAX_CONTEXT_CHUNKS", "5"))
    request_timeout_seconds: int = int(os.getenv("REQUEST_TIMEOUT_SECONDS", "20"))
    rate_limit_rpm: int = int(os.getenv("RATE_LIMIT_RPM", "120"))
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()
