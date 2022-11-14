import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from users.models import teamMember
from django.core import serializers 
 # Create your views here.

def addUser(request):
    """
    Adds a user to the SQL model database and saves it.
    Return: None
    """
    data = json.loads(request.body)
    u = teamMember(
    firstName = data.get("firstName"),
    lastName = data.get("lastName"),
    phone = data.get("phone"),
    emailId = data.get("emailId"),
    role = data.get("role")
    )
    u.save()

def deleteUsers(request, userID):
    """
    Deletes an existing user from the SQL model database.
    Return: None
    """
    teamMember.objects.filter(pk = userID.get("userId")).delete()

def updateUsers(request):
    '''
    Updates an existing user in the current SQL model database.
    Return: None
    '''
    userData = json.loads(request.body)
    user = teamMember.objects.filter(pk = userData.get("userId")).first()
    if "firstName" in userData:
        user.firstName = userData.get("firstName")

    if "lastName" in userData:
        user.lastName = userData.get("lastName")

    if "phone" in userData:
        user.phone = userData.get("phone")
        
    if "emailId" in userData:
        user.emailId = userData.get("emailId")

    if "role" in userData:
        user.role = userData.get("role")
    user.save()

@csrf_exempt
def users(request):
    """
    Handles all HTTP requests and deploys helper function according to which input is given.
    Return: JsonResponse/HttpResponse
    """
    if request.method == "POST":
        addUser(request)
        sd = serializers.serialize("json", [teamMember.objects.last()])
        sd = json.loads(sd)
        return JsonResponse(sd, safe = False)

    if request.method == "GET":
        teamMembers = teamMember.objects.all()
        serializedTeam = serializers.serialize("json", teamMembers)
        serializedTeam = json.loads(serializedTeam)
        return JsonResponse(serializedTeam, safe = False)

    if request.method == "DELETE":
        data = json.loads(request.body)
        if teamMember.objects.filter(pk = data.get("userId")).exists():
            deleteUsers(request, data)
            return HttpResponse("")
        else:
            return JsonResponse({"error": "Post not found.\n"}, status=404)

    if request.method == "PUT":
        data = json.loads(request.body)
        if teamMember.objects.filter(pk = data.get("userId")).exists():
            updateUsers(request)
            return JsonResponse(data)
        else:
            return JsonResponse({"error": "Post not found.\n"}, status=404)