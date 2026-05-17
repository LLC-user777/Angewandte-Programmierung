from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.get("/status")
def get_status():
    return {
        "status": "online",
        "version": "0.1.0",
        "day": 1
    }

@app.get("/about")
def get_about():
    return {
        "project": "First API from an idiot",
        "author": "LIUBOMYR MEDVEDCHUK",
        "course": "Applied Programming"
    }

#!!! HAUSARBEIT !!!

@app.get("/square/{number}")
def calculate_square(number: int):
    result = number * number
    return {
        "number": number,
        "square": result,
        "calculation": f"{number} × {number} = {result}"
    }

@app.get("/student")
def get_student():
    return {
        "name": "Liubomyr Medvedchuk",  
        "semester": 2,              
        "course": "Wirtschaftsinformatik 2.0",
        "university": "HS Coburg (Campus Kronach)"    
    }

@app.get("/double/{number}")
def calculate_double(number: int):
    result = number * 2
    return {
        "number": number,
        "double": result,
        "calculation": f"{number} × 2 = {result}"
    }