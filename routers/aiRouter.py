from fastapi import APIRouter
from openai import OpenAI
from interfaces.chatinterfaces import InputMessage

router = APIRouter()

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

@router.post("/ai-chat")
def ai_chat(data: InputMessage):
    user_message = data.message
    model_name = data.model

    print(f"Mensaje recibido: {user_message}")
    print(f"Modelo seleccionado: {model_name}")

    system_message = "Eres un asistente que siempre responde en Español de Colombia de forma clara y breve."
    prompt = f"Por favor, responde de manera concreta, clara y siempre en español. Responde a esta pregunta: {user_message}"

    try:
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        )
        return {
            "status": "OK",
            "response": completion.choices[0].message.content
        }

    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
