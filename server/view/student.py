from fastapi import APIRouter, Body 
from fastapi.encoders import jsonable_encoder
from server.database import student_collection


from server.controller.student import (
    add_student,
    update_student,
    retrieve_student,
    delete_student

)          
                                
from server.models.student import(
    StudentSchema,
    UpdateStudentModel
)
router = APIRouter()

@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    try:
        rollnodefine = await student_collection.find_one({'rollno':int(student.rollno)})
        if rollnodefine :
            return {"msf":"rollno already present"}
        else: 
           student = jsonable_encoder(student)
           new_student = await add_student(student)   
           return  { "data":new_student,"code":200,"msg":"inserted student data"}
    except Exception as e:
        return { "msg":e.args,"code":500}
    

@router.put("/{rollno}", response_description="get data update buy rollno")
async def update_data_buy(rollno:int,req: UpdateStudentModel=Body(...)):
    try:
        data = jsonable_encoder(req)
        newdata = {q: s for q,s in data.items() if len(str(s))!=0}
        updated_student = await update_student(rollno, newdata)
    
        if updated_student==True:
            return {"msg": "Student updated successfully."}
                
        return {"msg": "something went wrong"}
    except Exception as e:
        return {"msg": e.args, "code":500}

@router.get("/{rollno}", response_description="get data buy rollno")
async def get_data_buy(rollno):
    try:
        data=await retrieve_student(rollno)
        if data==True:
                return {"Data": data,"msg": "Student updated successfully"}
        return {"Data": "Data not present"}
    except Exception as e:
        return {"msg": e.args, "code":500}


@router.delete("/{rollno}", response_description="get data buy id")
async def get_data_buy(rollno):
    try:
        data=await delete_student(rollno)
        if data==True:
            return {"Data": "Data delete successful"}
        return {"Data": "Data not present"}
    except Exception as e:
        return {"msg": e.args, "code":500}


