from fastapi import APIRouter, HTTPException

from app.models.chat import ChatRequest, ChatResponse
from app.services.huggingface_service import generate_huggingface_response
from app.services.openai_service import generate_response as generate_openai_response


router = APIRouter(
    prefix="/api/v1",
    tags=["Generative AI"],
)


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        if request.provider == "openai":
            response_text, model = generate_openai_response(request.message)

        else:
            response_text, model = generate_huggingface_response(
                request.message
            )

        return ChatResponse(
            response=response_text,
            model=model,
            provider=request.provider,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate AI response: {str(exc)}",
        )