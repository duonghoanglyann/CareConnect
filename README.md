# CareConnect

CareConnect is a web app that helps people find local healthcare providers quickly and easily. Users can enter their city or ZIP code, pick specific healthcare categories (like hospitals, urgent care, or dentists), and see nearby clinics sorted by distance.

## How It Works
* **Frontend (HTML, CSS, JavaScript):** The webpage lets users type in a location and select multiple healthcare categories using quick-select checkboxes or a dropdown menu. JavaScript updates the category counter and opens or closes the dropdown menu.
* **Backend (Python & Flask):** When the user clicks Search, Flask sends the location and chosen categories to the Yelp Fusion API. Python processes the results, converts distances into miles, and displays each clinic's name, rating, address, phone number, and Yelp link.

## Project Files
* `main.py` - The Python Flask server that handles form submissions and connects to the Yelp API.
* `homepage/index.html` - The main webpage template that displays the search form and clinic results.
* `static/style.css` - Controls the colors, fonts, spacing, and card layout of the webpage.
* `static/script.js` - Makes the dropdown menu interactive and counts how many categories are selected.
* `.env` - Stores the secret Yelp API key safely outside the main code.

## How to Run the Project
1. Install the required Python libraries:
   ```bash
   pip install flask requests python-dotenv
   ```
2. Add your Yelp API key inside a `.env` file:
   ```env
   YELP_API_KEY=your_api_key_here
   ```
3. Run the Python server:
   ```bash
   python main.py
   ```
4. Open your browser and go to `http://127.0.0.1:8082`.

## DEMO ##
https://careconnect-z942.onrender.com/
