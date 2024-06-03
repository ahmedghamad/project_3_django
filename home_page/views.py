from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from services import get_books  
from .models import Portfolio



@login_required(login_url='account_login')
def home_view(request):
    """
    View to handle the home page for searching books by genre and displaying recommendations.
    """

    # If the request method is GET, render the search page
    if request.method == "GET":
        return render(request, 'home_page/search.html')
    
    # If the request method is POST, handle the form submission
    if request.method == "POST":
        genre = request.POST.get("Categories")  # Get the genre from the form input
        
        # Fetch the book recommendations based on the genre
        recommendations = get_books(genre)
        
        # If no recommendations are found, show an apology message
        if recommendations is None:
            messages.add_message(
                request, messages.ERROR,
                'Nothing matching'  # Add an error message to be displayed
            )
            return render(request, 'home_page/apology.html')  # Render the apology page
        else:
            # If recommendations are found, save them to the Portfolio model
            for recommendation in recommendations:
                book_title = recommendation['title']
                description = recommendation['description']
                Portfolio.objects.create(
                    user=request.user, 
                    book_title=book_title, 
                    description=description
                )  # Create and save Portfolio instance for each recommendation
            
            # Add a success message to be displayed
            messages.add_message(
                request, messages.SUCCESS,
                'The results will be added to your recommendations'
            )
            
            # Render the results page with the recommendations
            return render(
                request,
                "home_page/results.html",
                {
                    "recommendations": recommendations,  # Pass the recommendations to the template
                },
            )
        


@login_required(login_url='account_login')
def Recomended(request):
    """
    View to display the recommended books for the logged-in user.
    """

    # If the request method is GET, fetch the user's recommendations
    if request.method == "GET":
        # Retrieve all Portfolio entries for the current user, ordered by creation date (most recent first)
        recommendations = Portfolio.objects.filter(user=request.user).order_by("-created_on")
        
        # If the user has no recommendations, add a message indicating so
        if len(recommendations) == 0:
            messages.add_message(
                request, messages.SUCCESS,
                'You have no recommendations'  # Message to be displayed if there are no recommendations
            )
        else:
            # If there are recommendations, add a message indicating they are being loaded
            messages.add_message(
                request, messages.SUCCESS,
                'Loading your recommendations'  # Message to be displayed if recommendations are being loaded
            )
        
        # Render the portfolio template with the user's recommendations
        return render(
            request,
            "home_page/portfolio.html",
            {
                "recommendations": recommendations,  # Pass the recommendations to the template
            },
        )

def Welcome_view(request):
    """
    View to render the welcome page.
    """
    return render(
            request,
            "home_page/welcome.html",
        )