# src/services/llm.py
import os
from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Good default (usually ungated & fast enough on free tier)
DEFAULT_HF_MODEL = "HuggingFaceH4/zephyr-7b-beta"
# Other options if needed:
#   "mistralai/Mistral-7B-Instruct-v0.2"     (may be slower / sometimes gated)
#   "google/flan-t5-large"                   (lighter, not chat-tuned but works)

def _get_hf_token() -> str:
    token = os.getenv("HUGGINGFACEHUB_API_TOKEN") or os.getenv("HUGGINGFACE_API_KEY")
    if not token:
        raise RuntimeError(
            "Hugging Face token not found. Set HUGGINGFACEHUB_API_TOKEN in your .env"
        )
    return token

def build_itinerary_chain(
    system_msg: str,
    user_template: str,
    model_name: str = DEFAULT_HF_MODEL,
    temperature: float = 0.3,
):
    """
    Builds a LangChain pipeline:
      Prompt (system + user) → HF Endpoint (chat-wrapped) → String output
    """
    # Prompt
    system = SystemMessagePromptTemplate.from_template(system_msg)
    human = HumanMessagePromptTemplate.from_template(user_template)
    prompt = ChatPromptTemplate.from_messages([system, human])

    # Base HF endpoint (text generation)
    base_llm = HuggingFaceEndpoint(
        repo_id=model_name,
        huggingfacehub_api_token=_get_hf_token(),
        temperature=temperature,
        max_new_tokens=700,       # adjust if you want longer/shorter outputs
        do_sample=True,
        repetition_penalty=1.1,
        timeout=120,              # seconds
    )

    # Wrap as a chat model so ChatPromptTemplate works smoothly
    chat_llm = ChatHuggingFace(llm=base_llm)

    # Compose the runnable chain
    return prompt | chat_llm | StrOutputParser()

def generate_itinerary(params: dict, system_msg: str, template: str) -> str:
    chain = build_itinerary_chain(system_msg, template)
    return chain.invoke(params)
