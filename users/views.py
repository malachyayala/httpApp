import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from users.models import teamMember
from django.core import serializers 
 # Create your views here.

"""
Adds a user to the SQL model database and saves it.
Return: None
"""
def addUser(request):
    data = json.loads(request.body)
    u = teamMember(
    firstName = data.get("firstName"),
    lastName = data.get("lastName"),
    phone = data.get("phone"),
    emailId = data.get("emailId"),
    role = data.get("role")
    )
    u.save()

"""
Deletes an existing user from the SQL model database.
Return: None
"""
def deleteUsers(request):
    data = json.loads(request.body)
    teamMember.objects.filter(pk = data.get("userId")).delete()

"""
Updates an existing user in the current SQL model database.
Return: None
"""
def updateUsers(request):
    data = json.loads(request.body)
    new = teamMember.objects.filter(pk = data.get("userId")).first()
    if "firstName" in data:
        new.firstName = data.get("firstName")

    if "lastName" in data:
        new.lastName = data.get("lastName")

    if "phone" in data:
        new.phone = data.get("phone")
        
    if "emailId" in data:
        new.emailId = data.get("emailId")

    if "role" in data:
        new.role = data.get("role")
        
    new.save()

"""
Handles all HTTP requests and deploys helper function according to which input is given.
Return: JsonResponse/HttpResponse
"""
@csrf_exempt
def users(request):
    if request.method == "POST":
        addUser(request)
        sd = serializers.serialize("json", [teamMember.objects.last()])
        sd = json.loads(sd)
        return JsonResponse(sd, safe = False)

    if request.method == "GET":
        members = teamMember.objects.all()
        serializedData = serializers.serialize("json", members)
        serializedData = json.loads(serializedData)
        return JsonResponse(serializedData, safe = False)

    if request.method == "DELETE":
        deleteUsers(request)
        return HttpResponse("")

    if request.method == "PUT":
        data = json.loads(request.body)
        updateUsers(request)
        return JsonResponse(data)