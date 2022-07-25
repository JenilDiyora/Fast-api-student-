from server.database import student_collection, faculty_collection
from server.models.student import StudentSchema

def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "rollno" : str(student["rollno"]),
        "fullname": student["fullname"],
        "gender" :student["gender"],
        "language" : student["language"]
    }

async def retrieve_student():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


async def add_student(student_data: dict) -> dict:
    try :
            student = await student_collection.insert_one(student_data)
            new_student = await student_collection.find_one({"_id": student.inserted_id})
            return student_helper(new_student)
    except Exception as e:
        return {"msg": e.args}
    
async def update_student(rollno: int, data: dict):
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"rollno": int(rollno)})
    if student:
        updated_student = await student_collection.update_one(
            {"rollno": int(rollno)}, {"$set": data}
        )
        print(updated_student)
        if updated_student:
            return True
        return False
    
async def retrieve_student(rollno: int) -> dict:
    student = await student_collection.find_one({"rollno": int(rollno)})
    if student:
        return student_helper(student)
    return "id not present"


async def delete_student(rollno: int):
    student = await student_collection.find_one({"rollno": int(rollno)})
    if student:
        await student_collection.delete_one({"rollno": int(rollno)})
        return True
    return False