# pip install supabase
# pip install uvicorn fastapi
# python -m pip install uvicorn fastapi
# py -m pip install uvicorn fastapi

from fastapi import FastAPI # importing FastAPI class
from supabase import create_client

SUPABASE_URL = "https://huqwzjiocksduifelooy.supabase.co"
SUPABASE_KEY = "sb_publishable_sos2mHQ7LxpRjFeReqXYvA_S0a_fIsL"

fastapi_obj=FastAPI() # creating fastapi object
supabase_obj=create_client(SUPABASE_URL,SUPABASE_KEY)



@fastapi_obj.post("/login")
def login_validation(login_cred_details:dict):
    print(login_cred_details)

    incoming_login_email=login_cred_details["email"]
    incoming_login_password=login_cred_details["password"]
    incoming_login_role=login_cred_details["role"]

    response = supabase_obj.table("users") \
    .select("id,name,email,role") \
    .eq("email", incoming_login_email) \
    .eq("password", incoming_login_password) \
    .eq("role", incoming_login_role) \
    .execute()

    print(response.data,"res from supabase after login")
    if len(response.data) == 0:
        return { "msg":"invalid credentials"}
    return {
        "msg":"login successful",
        "status":True,
        "loggedIn_user":response.data[0]
        }



@fastapi_obj.post("/register")
def user_registration(new_user:dict): # type annotation
    print("reg function")
    print(new_user)
    res=supabase_obj.table("users").insert(new_user).execute()

    return{
        "msg":"reg done successfully",
        "data":res.data
    }




@fastapi_obj.post("/add_course")
def course_adding_function(new_course:dict):
    res_from_supabase = supabase_obj.table("courses").insert(new_course).execute()
    print(res_from_supabase)
    return {'msg':'Successfully added'}


@fastapi_obj.post("/get_my_courses")
def get_my_courses_function(t_id:str):
    res = supabase_obj.table("courses").select("*").eq('trainer_id',t_id).execute()
    return {"msg":"These are your courses details","data":res.data}


@fastapi_obj.delete("/delete_course")
def delete_course_function(c_id : str ):
    supabase_del_res = supabase_obj.table("courses").delete().eq("id",c_id).execute()
    return {"msg": "Course deleted successfully",
            "data": supabase_del_res.data}

# To start be server run in terminal "uvicorn main:fastapi_obj --reload