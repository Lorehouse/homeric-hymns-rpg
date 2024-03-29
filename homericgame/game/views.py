from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms

def index(request):
    if "HP" not in request.session:
        request.session["HP"] = 10
    if "XP" not in request.session:
        request.session["XP"] = 0
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "1":
            request.session["HP"] += 1
        elif action == "2":
            request.session["XP"] += 1
        return redirect("index")
    return render(request, "game/index.html", {
        "HP": request.session["HP"],
        "XP": request.session["XP"],
    })

