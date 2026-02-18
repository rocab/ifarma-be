from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1", tags=["agents"])

# generate synaps
class GenerateRequest(BaseModel):
    inn: str
    dosage_form: str
    dosage: str
    # regimen: str = ""  

# otvet - poka zagluwka
class GenerateResponse(BaseModel):
    task_id: str
    status: str

@router.post("/generate", response_model=GenerateResponse)
async def generate_synopsis(request: GenerateRequest):
    """
    Запускает всех агентов и возвращает ID задачи для отслеживания.
    """
    # orkestrator
    # test otvet
    return GenerateResponse(task_id="123", status="processing")

@router.get("/status/{task_id}")
async def get_status(task_id: str):
    """
    Возвращает статус обработки задачи.
    """
    # zagluwka
    return {"task_id": task_id, "status": "completed"}

@router.get("/download/{task_id}")
async def download_synopsis(task_id: str):
    """
    Скачивает готовый синопсис.
    """
    # zagluwka -> file ne gotov
    return {"message": "File not ready yet"}
