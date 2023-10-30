from fastapi import FastAPI
import wikipedia
app = FastAPI(
    title='Wikipedia'
)
@app.get("/name/{name}", description="Все статьи по запросу")
def get_name(name):
    return wikipedia.search(name)
@app.get("/name2", description="Определенные статьи по запросу")
def get_name2(name2: str, amount: int):
    return wikipedia.search(name2, results=amount)
from pydantic import BaseModel
class text(BaseModel):
    language: str
    name3: str
    sentences_amount: int
@app.post("/text", description="Нужная статья")
def get_name3(text: text):
    wikipedia.set_lang(text.language)
    return wikipedia.summary(text.name3, sentences=text.sentences_amount)
