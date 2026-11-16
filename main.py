import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Find the folder where this file is saved and load the .env file
folder = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(folder, ".env"))

API_KEY = os.getenv("YELP_API_KEY")
YELP_URL = "https://api.yelp.com/v3/businesses/search"

app = Flask(__name__, template_folder="homepage")

CATEGORY_OPTIONS = {
    "hospitals": "Hospitals",
    "urgent_care": "Urgent Care",
    "medcenters": "Medical Centers",
    "physicians": "Doctors / Physicians",
    "alternativemedicine": "Alternative Medicine",
    "psychiatrists": "Psychiatrists",
    "acupuncture": "Acupuncture",
    "chiropractors": "Chiropractors",
    "c_and_mh": "Counseling & Mental Health",
    "psychologists": "Psychologists",
    "tcm": "Traditional Chinese Medicine",
    "physicaltherapy": "Physical Therapy",
    "pediatricians": "Pediatricians",
    "dentists": "Dentists",
    "cardiology": "Cardiologists",
    "dermatology": "Dermatologists"
}

# Create a short description from the clinic's categories
def get_business_description(business):
    categories = business.get("categories", [])
    category_names = []

    for category in categories:
        if "title" in category:
            category_names.append(category["title"])

    if len(category_names) > 0:
        return business["name"] + " is listed in: " + ", ".join(category_names)
    else:
        return "Healthcare provider. Contact details below."

# Search Yelp for clinics matching the location and categories
def search_clinics(location, selected_categories):
    headers = {
        "Authorization": "Bearer " + API_KEY
    }
    
    parameters = {
        "location": location,
        "categories": ",".join(selected_categories),
        "limit": 20,
        "sort_by": "distance"
    }

    response = requests.get(YELP_URL, headers=headers, params=parameters, timeout=10)
    response.raise_for_status()
    data = response.json()
    
    clinics = data.get("businesses", [])
    for clinic in clinics:
        clinic["description"] = get_business_description(clinic)
        
    return clinics

@app.route("/", methods=["GET", "POST"])
def home():
    clinics = []
    location = ""
    error = None
    selected_categories = []

    if request.method == "POST":
        location = request.form.get("location", "").strip()
        submitted_categories = request.form.getlist("categories")

        # Only keep categories that exist in our dictionary
        for category in submitted_categories:
            if category in CATEGORY_OPTIONS:
                selected_categories.append(category)

        # Check for empty inputs before searching
        if location == "":
            error = "Please enter a city or ZIP code."
        elif len(selected_categories) == 0:
            error = "Please select at least one healthcare category."
        elif not API_KEY:
            error = "Yelp API configuration error."
        else:
            try:
                clinics = search_clinics(location, selected_categories)
                if len(clinics) == 0:
                    error = "No results found for your search. Try adjusting your filters."
            except Exception as e:
                print("Yelp API error:", e)
                error = "Could not connect to the search service. Please try again."

    return render_template(
        "index.html",
        clinics=clinics,
        location=location,
        error=error,
        category_options=CATEGORY_OPTIONS,
        selected_categories=selected_categories
    )

if __name__ == "__main__":
    # Start the website on port 8082
    app.run(host="127.0.0.1", port=8082, debug=False)
