def recommend_products(user_data):
    products = [
        {"name": "Organic Cotton T-Shirt", "category": "Clothing", "sustainability": 8},
        {"name": "Reusable Bamboo Cup", "category": "Homeware", "sustainability": 9},
        {"name": "Electric Car", "category": "Automobile", "sustainability": 7},
    ]
    
    category_preference = user_data.get('category')
    filtered_products = [p for p in products if p['category'] == category_preference]
    
    return filtered_products
