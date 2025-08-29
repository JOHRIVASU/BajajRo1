
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
import re

app = FastAPI(
    title="BFHL – VIT Full Stack API",
    version="1.0.0",
    description="POST /bfhl to process the input as per problem statement."
)

# ---------- CONFIG (edit if needed) ----------
FULL_NAME = "Vasu Johri"   # full name in lowercase with underscore
DOB = "04102004"              # ddmmyyyy
EMAIL = "vasu.johri2022@vitstudent.ac.in"
ROLL_NUMBER = "22BEC0978"
USER_ID = f"{FULL_NAME.lower()}_{DOB}"
# --------------------------------------------

class InputData(BaseModel):
    data: List[str] = Field(..., description="Array of strings containing numbers/alphabets/special chars")

def alternating_caps_reverse(s: str) -> str:
    # Reverse string then apply alternating caps starting with UPPER
    s = s[::-1]
    out = []
    toggle_upper = True
    for ch in s:
        if ch.isalpha():
            out.append(ch.upper() if toggle_upper else ch.lower())
            toggle_upper = not toggle_upper
        else:
            # Shouldn't occur because s is built from only alpha chars,
            # but keep behavior consistent
            out.append(ch)
    return "".join(out)

@app.post("/bfhl")
async def bfhl(payload: InputData):
    try:
        data = payload.data

        odd_numbers: List[str] = []
        even_numbers: List[str] = []
        alphabets: List[str] = []
        special_characters: List[str] = []
        total_sum = 0

        alpha_concat_builder = []

        for item in data:
            # Treat strictly numeric strings as numbers (no +/- or decimals per examples)
            if item.isdigit():
                n = int(item)
                (even_numbers if n % 2 == 0 else odd_numbers).append(item)
                total_sum += n
            elif item.isalpha():
                alphabets.append(item.upper())
                alpha_concat_builder.append(item)  # preserve original letters for concat rule
            else:
                special_characters.append(item)

        # Build concat string from all alphabetical characters (joined), reverse + alternating caps
        concat_input = "".join(alpha_concat_builder)
        concat_string = alternating_caps_reverse(concat_input)

        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),  # sum as string
            "concat_string": concat_string,
        }
        return response
    except Exception as e:
        return {
            "is_success": False,
            "error": str(e)
        }
