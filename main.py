from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="BFHL – VIT Full Stack API", version="1.1.0")

# CORS so you can test from browser/Swagger
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- YOUR DETAILS ----
FULL_NAME = "vasu_johri"                 # lowercase + underscore
DOB = "04102004"                         # ddmmyyyy
EMAIL = "vasu.johri2022@vitstudent.ac.in"
ROLL_NUMBER = "22BEC0978"
USER_ID = f"{FULL_NAME.lower()}_{DOB}"
# -----------------------

class InputData(BaseModel):
    data: List[str] = Field(..., description="Array of strings (numbers/alphabets/special chars)")

def alternating_caps_reverse(s: str) -> str:
    s = s[::-1]
    out, upper = [], True
    for ch in s:
        if ch.isalpha():
            out.append(ch.upper() if upper else ch.lower())
            upper = not upper
        else:
            out.append(ch)
    return "".join(out)

# Friendly GET endpoints (so browser doesn't 404)
@app.get("/")
def root():
    return {"message": "Service is up. Use POST /bfhl. See /docs for Swagger."}

@app.get("/health")
def health():
    return {"status": "up"}

@app.get("/bfhl")
def bfhl_get_info():
    return {"message": "Use POST /bfhl with body: {\"data\": [\"a\",\"1\",\"$\", ...]} (POST-only as per spec)"}

# MAIN ASSIGNMENT ENDPOINT
@app.post("/bfhl")
async def bfhl(payload: InputData):
    try:
        data = payload.data
        odd_numbers, even_numbers, alphabets, special_characters = [], [], [], []
        total_sum = 0
        alpha_concat_src = []

        for item in data:
            if item.isdigit():
                n = int(item)
                (even_numbers if n % 2 == 0 else odd_numbers).append(item)
                total_sum += n
            elif item.isalpha():
                alphabets.append(item.upper())
                alpha_concat_src.append(item)
            else:
                special_characters.append(item)

        concat_string = alternating_caps_reverse("".join(alpha_concat_src))

        return {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string,
        }
    except Exception as e:
        return {"is_success": False, "error": str(e)}
