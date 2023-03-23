import logging
from fastapi import FastAPI

from src.app.data_transfer import AskRequest, AskResponse
from src.app.assistant import GPTAssistant

app = FastAPI()
logger = logging.getLogger("uvicorn.error")

assistant_handler = {}

@app.post("/dump", status_code=200)
async def post_dump(ask_request: AskRequest):
    return {}


@app.post("/ask", response_model=AskResponse, status_code=200)
async def post_ask(ask_request: AskRequest):
    id = ask_request.id
    ask_text = ask_request.text
    if id in assistant_handler:
        assistant = assistant_handler[id]
    else:
        assistant = GPTAssistant()
        assistant_handler[id] = assistant
    answer_text = await assistant.ask(ask_text)
    return AskResponse(id=id, text=answer_text)
