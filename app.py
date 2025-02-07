from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math
import os

app = Flask(_name_)
CORS(app)  # Enable CORS

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    if n < 1:
        return False
    return sum([i for i in range(1, n) if n % i == 0]) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(abs(n))]  # Handle negative numbers correctly
    power = len(digits)
    return sum(d**power for d in digits) == abs(n)

def get_fun_fact(n):
    """Fetch a fun fact from the Numbers API."""
    url = f"http://numbersapi.com/{abs(n)}/math?json"  # Use absolute value for fun fact
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("text", "No fun fact found.")
    except requests.exceptions.RequestException:
        return "Could not fetch fun fact."
    return "No fun fact available."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """Classify a number based on various properties."""
    number = request.args.get("number")

    # *Input validation*
    try:
        num = int(number)  # Convert to integer (Handles negative numbers too)
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Please enter a valid integer."}), 400

    # Determine properties
    properties = ["even" if num % 2 == 0 else "odd"]
    if is_armstrong(num):
        properties.insert(0, "armstrong")

    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(num))),  # Handle negatives correctly
        "fun_fact": get_fun_fact(num)
    }

    return jsonify(response), 200

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))  # Use dynamic PORT for Render
    app.run(debug=True, host="0.0.0.0", port=port)
