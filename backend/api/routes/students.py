from fastapi import APIRouter
from api.services.supabase_service import create_student, list_students

router = APIRouter()

@router.post("/students")
def add_student(department: str, student_count: int, uploaded_by: str):
    result = create_student(department, student_count, uploaded_by)
    return {"message": "Student record created ✅", "data": result.data}

@router.get("/students")
def get_students():
    result = list_students()
    return {"students": result.data}
