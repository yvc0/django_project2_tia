from django.http import HttpResponse

def add_numbers(request):
    a = 10
    b = 5
    result = a + b
    return HttpResponse(f"Addition: {a} + {b} = {result}")

def subtract_numbers(request):
    a = 10
    b = 5
    result = a - b
    return HttpResponse(f"Subtraction: {a} - {b} = {result}")

def multiply_numbers(request):
    a = 10
    b = 5
    result = a * b
    return HttpResponse(f"Multiplication: {a} × {b} = {result}")

def student_info(request):
    name = "Tanmay"
    age = 21
    course = "B.Tech in ECE"
    return HttpResponse(f"Student Info:<br>Name: {name}<br>Age: {age}<br>Course: {course}")
