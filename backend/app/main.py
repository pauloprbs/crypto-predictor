from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "API de Previsão de Criptomoedas."}