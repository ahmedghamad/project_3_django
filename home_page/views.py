from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from services import get_books  # Assuming you have a function to get books
from .models import Portfolio




@login_required(login_url='account_login')
def home_view(request):
        if request.method == "GET":
            return render(request, 'home_page/search.html')
        
        if request.method == "POST":
            genre = request.POST.get("Categories")  # Use request.POST to access form data
            recommendations = get_books(genre)
            if recommendations is None:
                messages.add_message(
            request, messages.ERROR,
            'Nothing matching'
    )
                return render(request, 'home_page/apology.html')
            else:
                for recommendation in recommendations:
                    book_title = recommendation['title']
                    description = recommendation['description']
                    Portfolio.objects.create(user=request.user, book_title=book_title, description= description)  # Create and save Portfolio instance
                messages.add_message(
            request, messages.SUCCESS,
            'The results will be added to your recommendations'
    )
            return render(
            request,
            "home_page/results.html",
            {
            "recommendations":recommendations,
            },
        )

@login_required(login_url='account_login')
def Recomended(request):
    if request.method == "GET":
        recommendations =Portfolio.objects.filter(user=request.user).order_by("-created_on")
        messages.add_message(
            request, messages.SUCCESS,
            'Loading your recommendations'
    )
        
        return render(
        request,
        "home_page/portfolio.html",
        {
        "recommendations":recommendations,
        },
    )

def Welcome_view(request):
        return render(
            request,
            "home_page/welcome.html",
        )