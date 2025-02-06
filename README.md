
# Number Classification API

## Overview

The **Number Classification API** is a simple RESTful API that takes a number as input and returns its mathematical properties, including whether it's prime, perfect, or an Armstrong number. It also provides a fun fact about the number using the [Numbers API](http://numbersapi.com/).

## Features

- Determines if a number is **prime**, **perfect**, or **an Armstrong number**.
- Identifies if the number is **odd** or **even**.
- Calculates the **sum of its digits**.
- Fetches a **fun fact** from the Numbers API.
- Returns data in **JSON format**.
- Handles **input validation** and **error handling**.
- Supports **CORS** for cross-origin requests.

## API Specification

### **Endpoint**

`GET /api/classify-number?number=371`

### **Request Parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| number | int | The number to classify |

### **Success Response (200 OK)**

```json
{
  "digit_sum": 5,
  "fun_fact": "5 is the second Sierpinski number of the first kind, and can be written as S2=(22)+1.",
  "is_perfect": false,
  "is_prime": true,
  "number": 5,
  "properties": [
    "armstrong",
    "odd"
  ]
}
```

### **Error Response (400 Bad Request)**

```json
{
  "number": "abc",
  "error": true
}

```

## Installation & Running Locally

### **Prerequisites**

- Python 3.8+
- Pip package manager

### **Setup**

1. Clone the repository:
    
    ```
    git clone https://github.com/Patogee5/NumberClassificationAPI
    cd NumberClassificationAPI
    
    ```
    
2. Create a virtual environment:
    
    ```
    python -m venv venv
    
    ```
    
3. Activate the virtual environment:
    - **Windows:** `venv\Scripts\activate`
    - **Mac/Linux:** `source venv/bin/activate`
4. Install dependencies:
    
    ```
    pip install -r requirements.txt
    
    ```
    
5. Run the API:
    
    ```
    python app.py
    
    ```
    

The API should now be running at [**http://127.0.0.1:5000**](http://127.0.0.1:5000/).

## Deployment

### **Deploying on Render**

1. Push the project to GitHub:
    
    ```
    git init
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin https://github.com/Patogee5/NumberClassificationAPI
    git push -u origin main
    
    ```
    
2. Go to [Render](https://render.com/) and create a **new web service**.
3. Connect your GitHub repository.
4. Set up the following:
    - **Runtime:** Python 3.x
    - **Build Command:** `pip install -r requirements.txt`
    - **Start Command:** `python app.py`
5. Deploy and copy the **public API URL**.

## Example Usage

### **Local Testing**

### **Using Curl**

```
curl "http://127.0.0.1:5000/api/classify-number?number=371"

```

### **Using Browser**

Visit:

```
http://127.0.0.1:5000/api/classify-number?number=371

```

### **Live API Test**

Replace `<your-api-url>` with your deployed API link:

```
https://numberclassificationapi-14rq.onrender.com/api/classify-number?number=5

```

## Technologies Used

- **Python** (Flask)
- **Flask-CORS** (Handles cross-origin requests)
- **Requests** (Fetches fun facts from Numbers API)
- **Render** (For deployment)

## License

This project is open-source and available under the MIT License.

---

**Author:** Ibegbunam Patrick

**GitHub Repository:** [https://github.com/Patogee5/NumberClassificationAPI](https://github.com/Patogee5/NumberClassificationAPI/blob/main/README.md)
