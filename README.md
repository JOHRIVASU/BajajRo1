
# BFHL – VIT Full Stack API (FastAPI)

REST API for the VIT Full-Stack assignment.  
Implements POST **/bfhl** exactly as specified: separates odd/even numbers, alphabets (uppercased), special characters, returns sum (as string), and concatenation of all alphabetical characters in **reverse with alternating caps**.

## ✅ Endpoint
```
POST /bfhl
Content-Type: application/json
```

### Request Body
```json
{ "data": ["a", "1", "334", "4", "R", "$"] }
```

### Success Response (200)
```json
{
  "is_success": true,
  "user_id": "tanmay_mishra_22072002",
  "email": "tanmay.mishra2022@vitstudent.ac.in",
  "roll_number": "22BEC0978",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

> Numbers are returned as **strings**.  
> `user_id` format: `full_name_ddmmyyyy` (full name lowercase).

## 🧪 Local Run
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Test:
```bash
curl -X POST http://127.0.0.1:8000/bfhl   -H "Content-Type: application/json"   -d '{"data": ["2","a","y","4","&","-","*","5","92","b"]}'
```

## 🚀 Deploy (Render / Railway / Heroku)
1. Push these files to a **public GitHub repo**.
2. **Render**: New Web Service → Build from repo → Start command auto (from `Procfile`), or set to:
   ```
   uvicorn main:app --host=0.0.0.0 --port=$PORT
   ```
3. **Railway**/**Heroku**: Just use the `Procfile`.

Your final URL will look like:
```
https://<your-app>.onrender.com/bfhl
```

## ⚙️ Config
Edit the constants at the top of `main.py`:
```python
FULL_NAME = "tanmay_mishra"
DOB = "22072002"  # ddmmyyyy
EMAIL = "tanmay.mishra2022@vitstudent.ac.in"
ROLL_NUMBER = "22BEC0978"
```

## 🧩 Notes
- Only **strictly numeric** strings are treated as numbers (as in the examples).
- Alphabet items can be multi-letter words; they are uppercased in the `alphabets` array, but the `concat_string` uses original letters (joined), then reversed with alternating caps.
- Errors are returned with `"is_success": false` and an `"error"` message.


---

## ✅ Postman & REST Client
- Import `postman_collection.json` into Postman and hit **Send**.
- Or install the VS Code **REST Client** extension and open `request.http`.

## 🧪 CI (GitHub Actions)
This repo includes `.github/workflows/ci.yml` which runs **flake8** and **pytest** on every push/PR.

## ☁️ One‑click Render Deploy
- Connect your GitHub repo on Render → New **Blueprint** → select this repo.
- Render detects `render.yaml` and sets everything up automatically.

## 📄 OpenAPI Docs
Once running, visit:
- Swagger UI: `http://<your-app>/docs`
- ReDoc: `http://<your-app>/redoc`

## 🧷 Notes for Submission
- Ensure your live URL ends with `/bfhl`.
- Verify **status code 200** on success.
- Confirm data types in arrays are **strings** for numbers.
- `user_id` must be lowercase full name + DOB in `ddmmyyyy` format.
