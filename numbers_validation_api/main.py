from fastapi import FastAPI, Path
from functions import valida_cpf, valida_cnpj, valida_data

app = FastAPI()

@app.get("/valida/cpf/{cpf}")
async def validar_cpf(cpf: str = Path(..., max_length=14, min_length=11)):
    """
    Check if a CPF, is a valid CPF.
    """
    return {"result": valida_cpf(cpf)}

@app.get("/valida/cnpj/{cnpj}")
async def validar_cnpj(cnpj: str = Path(..., max_length=14, min_length=11)):
    """
    Check if a CNPJ, is a valid CNPJ.
    """
    return {"result": valida_cnpj(cnpj)}

@app.get("/valida/data/{ano}/{mes}/{dia}")
async def validar_data(ano: int = Path(..., gt=0),
    mes: int = Path(..., gt=0, le=12),
    dia: int = Path(..., gt=0, le=31)):
    """
    Check if a Data, is a valid Data.
    """
    return {"result": valida_data(ano, mes, dia)}