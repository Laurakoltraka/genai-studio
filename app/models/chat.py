
from typing import Literal

from pydantic import BaseModel, Field

from app.services.openai_service import generate_response


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=4000,
        description="Message to send to the AI model",
    )

    provider: Literal["openai", "huggingface"] = "huggingface"


class ChatResponse(BaseModel):
    response: str
    model: str
    provider: str

   
from fastapi import APIRouter, HTTPException
from app.models.chat import ChatRequest, ChatResponse



router = APIRouter(
    prefix="/api/v1",
    tags=["Generative AI"],
)


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        response_text, model = generate_response(request.message)

        return ChatResponse(
            response=response_text,
            model=model,
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to generate AI response",
        )