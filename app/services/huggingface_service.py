import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


MODEL_NAME = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

model.eval()


def generate_huggingface_response(message: str) -> tuple[str, str]:

    inputs = tokenizer(
        message,
        return_tensors="pt",
        truncation=True,
        max_length=512,
    )

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=128,
        )

    generated_text = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True,
    )

    return generated_text, MODEL_NAME