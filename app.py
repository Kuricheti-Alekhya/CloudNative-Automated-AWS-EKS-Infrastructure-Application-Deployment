from flask import Flask, jsonify, render_template, request
from datetime import datetime
import uuid

app = Flask(__name__)

MENU = [
    {"id": 1, "name": "Chicken Biryani", "category": "Main Course", "price": 220, "emoji": "🍛"},
    {"id": 2, "name": "Paneer Butter Masala", "category": "Main Course", "price": 180, "emoji": "🥘"},
    {"id": 3, "name": "Masala Dosa", "category": "Breakfast", "price": 90, "emoji": "🥞"},
    {"id": 4, "name": "Veg Fried Rice", "category": "Main Course", "price": 150, "emoji": "🍚"},
    {"id": 5, "name": "Gulab Jamun", "category": "Dessert", "price": 70, "emoji": "🍮"},
    {"id": 6, "name": "Fresh Lime Soda", "category": "Drinks", "price": 60, "emoji": "🥤"}
]

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api/menu")
def menu():
    return jsonify(MENU)

@app.get("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "quickbite",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

@app.post("/api/orders")
def create_order():
    data = request.get_json(silent=True) or {}
    items = data.get("items", [])
    if not items:
        return jsonify({"error": "Cart is empty"}), 400

    total = sum(float(i.get("price", 0)) * int(i.get("quantity", 1)) for i in items)
    order_id = "ORD-" + uuid.uuid4().hex[:8].upper()

    return jsonify({
        "order_id": order_id,
        "status": "Confirmed",
        "total": round(total, 2),
        "message": "Your food order has been placed successfully."
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
