from flask import Blueprint, request, render_template
from app.recommender import recommend_products
from app.sustainability import calculate_footprint

app_routes = Blueprint('app_routes', __name__)

# Home Page
@app_routes.route('/')
def index():
    return render_template('index.html')

# Product Recommendation Endpoint
@app_routes.route('/recommend', methods=['POST'])
def recommend():
    user_data = request.form
    recommendations = recommend_products(user_data)
    footprint = calculate_footprint(recommendations)
    return render_template('results.html', products=recommendations, footprint=footprint)

