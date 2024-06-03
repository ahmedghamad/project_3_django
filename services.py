import os
import requests
from django.conf import settings
if os.path.isfile('env.py'):
    import env



def get_books(genre):
    """Look up books."""

    # Contact API
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("API key not found. Make sure 'API_KEY' environment variable is set.")
        return None
    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {
        'q': genre,
        'subject': genre,
        'key': api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        results = []
        if "items" in data:
            books = data["items"]
            for book in books:
                book_info = book.get("volumeInfo", {})
                book1 = {
                    'title': book_info.get("title", "N/A"),
                    'author': book_info.get("authors", ["N/A"])[0],
                    'publisher': book_info.get("publisher", "N/A"),
                    'description': book_info.get("description", "N/A")
                }
                results.append(book1)

            return results
        else:
            print("No items found in API response.")
            return None
    except requests.RequestException as e:
        print('Error occurred during API request:', e)
        return None
