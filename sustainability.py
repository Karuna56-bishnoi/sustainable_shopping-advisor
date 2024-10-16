def calculate_footprint(products):
    footprint = sum(product["sustainability"] for product in products)
    return {"total_footprint": footprint}
