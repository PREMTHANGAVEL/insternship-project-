from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import json

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]




# GET all users / POST a new user
def user_list(request):
    if request.method == "GET":
        return JsonResponse(users, safe=False)  # safe=False allows list
    elif request.method == "POST":
        data = json.loads(request.body)
        new_id = max([u["id"] for u in users]) + 1 if users else 1
        data["id"] = new_id
        users.append(data)
        return JsonResponse(data, status=201)

# GET, PUT, DELETE a user by id
def user_detail(request, user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return JsonResponse({"error": "User not found"}, status=404)
    
    if request.method == "GET":
        return JsonResponse(user)
    elif request.method == "PUT":
        data = json.loads(request.body)
        user.update(data)
        return JsonResponse(user)
    elif request.method == "DELETE":
        users.remove(user)
        return JsonResponse({"message": "User deleted"})
