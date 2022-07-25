FASTAPI-MongoDB-CRUD App


The application uses fastAPI and MongoDB as backend servers to implement a simple REST API.
I have used asynchronous functions in most places.
FastAPI provides amazing support for asynchronous programming.
For Database Asynchronous operations, I have used Motor python package for MongoDB.
The API provides a simple API for a student database. The API is capable of performing

1)Retrieve all students (GET)
2)Retrieve single student using student-id (GET)
3)Add a student (POST)
4)Update a student info (PUT)
5)Delete a student from Database

*RUN

To run the application follow these instruction. if you are inside the root folder, then move into the app folder. then execute the following command.
python main.py
This will start the server in localhost:8000
To access the api endpoints, we have used the FastAPI built-in interface. go to this url for that purpose. localhost:8000/docs
test the API endpoints as much as you like!