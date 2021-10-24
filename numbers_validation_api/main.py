from fastapi import FastAPI, Path
from functions import valida_cpf, valida_cnpj

app = FastAPI()

@app.get("/valida/cpf/{cpf}")
async def validar_cpf(cpf: str = Path(..., max_length=14, min_length=11)):
    return {"result": valida_cpf(cpf)}

@app.get("/valida/cnpj/{cnpj}")
async def validar_cnpj(cnpj: str = Path(..., max_length=14, min_length=11)):
    return {"result": valida_cnpj(cnpj)}