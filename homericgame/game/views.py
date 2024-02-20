from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms

def index(request):
    if "counter" not in request.session:
        request.session["counter"] = 0
    if "countertwo" not in request.session:
        request.session["countertwo"] = 0
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "1":
            request.session["counter"] += 1
        elif action == "2":
            request.session["countertwo"] += 1
        return redirect("index")
    return render(request, "game/index.html", {
        "counter": request.session["counter"],
        "countertwo": request.session["countertwo"],
    })

