# 🔐 Password Strength Checker API

A modern, fast, and scalable REST API built with **FastAPI** that analyzes password strength based on multiple criteria.  
It gives you a score, strength level, and suggestions for improvement.

---

## 🚀 Features

- ✅ Score system (0 to 5)
- ✅ Password strength level (Very Weak → Very Strong)
- ✅ Regex-based rules: length, uppercase, lowercase, digits, special chars
- ✅ Real-time API response
- ✅ Dockerized
- ✅ CI with GitHub Actions

---

## 📦 Tech Stack

- **Python 3.10**
- **FastAPI**
- **Uvicorn**
- **Pytest**
- **Docker**
- **GitHub Actions**

---

## 🛠️ API Endpoints

### `POST /check-password`

Check the strength of a password.

#### Request:
```json
{
  "password": "Abcd1234!"
}
Response:
json
{
  "score": 5,
  "strength": "Very Strong",
  "issues": []
}
🐳 Run with Docker

docker build -t password-checker .
docker run -d -p 8000:8000 password-checker
Open in browser: http://localhost:8000/docs

📂 Project Structure

password-strength-checker/
│
├── app/
│   ├── main.py
│   └── checker.py
├── tests/
├── Dockerfile
├── requirements.txt
└── .github/workflows/ci.yml

👤 Author
Made with ❤️ by eldarmeta
