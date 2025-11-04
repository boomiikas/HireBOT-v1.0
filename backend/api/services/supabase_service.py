from core.db import supabase

# -------------------------------
# 📘 Placement Team (User Table)
# -------------------------------
def create_placement_team_member(name, email, organization, password):
    data = {
        "name": name,
        "email": email,
        "organization": organization,
        "password": password
    }
    return supabase.table("placement_team").insert(data).execute()

def list_placement_team_members():
    return supabase.table("placement_team").select("*").execute()


# -------------------------------
# 🎓 Students Table
# -------------------------------
def create_student(department, student_count, uploaded_by):
    data = {
        "department": department,
        "student_count": student_count,
        "uploaded_by": uploaded_by
    }
    return supabase.table("students").insert(data).execute()

def list_students():
    return supabase.table("students").select("*").execute()


# -------------------------------
# 💼 HR Contacts Table
# -------------------------------
def create_hr_contact(hr_name, hr_email, company_name, added_by):
    data = {
        "hr_name": hr_name,
        "hr_email": hr_email,
        "company_name": company_name,
        "added_by": added_by
    }
    return supabase.table("hr_contacts").insert(data).execute()

def list_hr_contacts():
    return supabase.table("hr_contacts").select("*").execute()
