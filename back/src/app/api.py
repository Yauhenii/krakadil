import logging
from fastapi import FastAPI

from src.app.data_transfer import AnswerRequest, AnswerResponse

app = FastAPI()
logger = logging.getLogger("uvicorn.error")


@app.post("/request_answer", response_model=AnswerResponse, status_code=200)
async def post_request_answer(answer_request: AnswerRequest):
    return AnswerResponse(id=f'milena_{answer_request.id}')
