from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# ---------- HOME PAGE ----------
def index(request):
    dealers = [
        {"name": "Best Cars", "city": "Hyderabad", "state": "Telangana"},
        {"name": "Auto World", "city": "Bangalore", "state": "Karnataka"},
    ]

    return render(request, "djangoapp/index.html", {
        "dealers": dealers,
        "user": request.user
    })


# ---------- API ENDPOINTS ----------
@csrf_exempt
def login_user(request):
    # 👉 HANDLE GET (browser access)
    if request.method == "GET":
        return HttpResponse(
            "Login endpoint. Use POST with username and password.",
            status=200
        )

    # 👉 HANDLE POST (curl / frontend)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"status": "Authenticated", "user": username})
        else:
            return JsonResponse(
                {"status": "Failed", "message": "Invalid credentials"},
                status=401
            )
def logout_user(request):
    logout(request)
    return JsonResponse({"status": "Logged out"})


def get_dealers(request):
    return JsonResponse({
        "dealers": [
            {"id": 1, "name": "Best Cars", "city": "Hyderabad", "state": "Telangana"},
            {"id": 2, "name": "Auto World", "city": "Bangalore", "state": "Karnataka"},
        ]
    })


def get_dealers_by_state(request, state):
    return JsonResponse({
        "dealers": [
            {"id": 3, "name": "Kansas Cars", "city": "Wichita", "state": state}
        ]
    })


def get_dealer_details(request, dealer_id):
    return JsonResponse({
        "id": dealer_id,
        "name": "Best Cars",
        "city": "Hyderabad",
        "state": "Telangana"
    })


def get_reviews(request, dealer_id):
    return JsonResponse({
        "dealer_id": dealer_id,
        "reviews": []
    })


def get_cars(request):
    return JsonResponse({
        "CarMakes": [
            {"id": 1, "name": "Toyota", "models": ["Corolla", "Camry"]},
            {"id": 2, "name": "Honda", "models": ["Civic", "Accord"]}
        ]
    })
from django.shortcuts import render
import requests

def dealer_page(request, dealer_id):
    dealer_url = f"http://127.0.0.1:8000/djangoapp/get_dealer/{dealer_id}/"
    reviews_url = f"http://127.0.0.1:8000/djangoapp/get_reviews/{dealer_id}"

    dealer = requests.get(dealer_url).json()
    reviews = requests.get(reviews_url).json().get("reviews", [])

    context = {
        "dealer": dealer,
        "reviews": reviews
    }

    return render(request, "djangoapp/dealer_details.html", context)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def add_review(request, dealer_id):
    return render(request, 'djangoapp/add_review.html', {
        'dealer_id': dealer_id
    })
