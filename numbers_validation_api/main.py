from fastapi import FastAPI, Path
from functions import valida_cpf

app = FastAPI()

@app.get("/valida/cpf/{cpf}")
async def validar_cpf(cpf: str = Path(..., max_length=14, min_length=11)):
    return {"result": valida_cpf(cpf)}
