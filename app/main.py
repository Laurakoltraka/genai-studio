from fastapi import FastAPI

from app.api.chat import router as chat_router


app = FastAPI(
    title="GenAI Studio API",
    description="Multimodal Generative AI experimentation platform",
    version="0.2.0",
)


app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "application": "GenAI Studio",
        "version": "0.2.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }