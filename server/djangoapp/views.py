from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json


# ------------------------------------------------
# HOME PAGE
# ------------------------------------------------
def index(request):
    dealers = [
        {"name": "Best Cars", "city": "Hyderabad", "state": "Telangana"},
        {"name": "Auto World", "city": "Bangalore", "state": "Karnataka"},
    ]

    return render(request, "djangoapp/index.html", {
        "dealers": dealers,
        "user": request.user
    })


# ------------------------------------------------
# LOGIN API
# ------------------------------------------------
@csrf_exempt
def login_user(request):

    if request.method == "GET":
        return HttpResponse("Login endpoint — use POST")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return JsonResponse({
                "status": "Authenticated",
                "user": username
            })

        return JsonResponse({
            "status": "Failed"
        }, status=401)


# ------------------------------------------------
# LOGOUT API
# ------------------------------------------------
def logout_user(request):
    logout(request)
    return JsonResponse({
        "status": "Logged out",
        "userName": ""
    })


# ------------------------------------------------
# MOCK DEALER DATABASE (50 dealers)
# ------------------------------------------------
def generate_dealers():
    dealers = []

    for i in range(1, 51):
        dealers.append({
            "id": i,
            "name": f"Dealer {i}",
            "short_name": f"D{i}",
            "address": f"{100+i} Main Street",
            "city": "Kansas City",
            "state": "Kansas",
            "zip": "66101",
            "lat": 39.0997 + i * 0.001,
            "long": -94.5786 - i * 0.001
        })

    return dealers


DEALERS = generate_dealers()


# ------------------------------------------------
# Q9 — FETCH ALL DEALERS
# ------------------------------------------------
def fetchDealers(request):
    return JsonResponse({
        "status": 200,
        "dealers": DEALERS
    })


# ------------------------------------------------
# Q10 — FETCH SINGLE DEALER
# ------------------------------------------------
def fetchDealer(request, dealer_id):

    dealer = next((d for d in DEALERS if d["id"] == dealer_id), None)

    if dealer:
        return JsonResponse({
            "status": 200,
            "dealer": dealer
        })

    return JsonResponse({"status": 404})


# ------------------------------------------------
# Q11 — FETCH DEALERS BY STATE
# ------------------------------------------------
def fetchDealersState(request, state):

    filtered = [d for d in DEALERS if d["state"].lower() == state.lower()]

    return JsonResponse({
        "status": 200,
        "dealers": filtered
    })


# ------------------------------------------------
# Q8 — REVIEWS
# ------------------------------------------------
def fetchReviews(request, dealer_id):

    reviews = [{
        "dealer_id": dealer_id,
        "review": "Excellent service and friendly staff!",
        "purchase": True,
        "purchase_date": "2024-01-10",
        "car_make": "Toyota",
        "car_model": "Camry",
        "sentiment": "positive"
    }]

    return JsonResponse({"reviews": reviews})


# ------------------------------------------------
# Q14 — CAR MAKES / MODELS
# ------------------------------------------------
def get_cars(request):

    return JsonResponse({
        "CarModels": [
            {"make": "Toyota", "model": "Corolla", "year": 2021},
            {"make": "Toyota", "model": "Camry", "year": 2022},
            {"make": "Honda", "model": "Civic", "year": 2020},
            {"make": "Honda", "model": "Accord", "year": 2021}
        ]
    })


# ------------------------------------------------
# Q15 — SENTIMENT ANALYSIS (GET)
# ------------------------------------------------
def analyze(request, text):

    text = text.lower()

    if "fantastic" in text or "excellent" in text:
        sentiment = "positive"
    else:
        sentiment = "neutral"

    return JsonResponse({"sentiment": sentiment})


# ------------------------------------------------
# DEALER PAGE (UI)
# ------------------------------------------------
def dealer_page(request, dealer_id):

    dealer = next((d for d in DEALERS if d["id"] == dealer_id), None)
    reviews = fetchReviews(request, dealer_id).json()["reviews"]

    return render(request, "djangoapp/dealer_details.html", {
        "dealer": dealer,
        "reviews": reviews
    })


# ------------------------------------------------
# ADD REVIEW PAGE
# ------------------------------------------------
@login_required
def add_review(request, dealer_id):

    return render(request, "djangoapp/add_review.html", {
        "dealer_id": dealer_id
    })
