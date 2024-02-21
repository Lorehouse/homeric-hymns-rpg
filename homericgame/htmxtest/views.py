
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms

def test(request):
    if "HP" not in request.session:
        request.session["HP"] = 10
    if "XP" not in request.session:
        request.session["XP"] = 0
    if "weapon" not in request.session:
        request.session["XP"] = "none"
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "1":
            request.session["weapon"] = "sword"
        elif action == "2":
            request.session["XP"] = "spear"
    return render(request, "test.html")

def weapon(request):
    return render(request, "weapon.html")