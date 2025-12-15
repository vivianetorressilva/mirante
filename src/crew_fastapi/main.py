import sys, os
from fastapi import FastAPI
from crew import Mirante
import db_postgresql

os.environ["HF_TOKEN"] = "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"
os.environ["OPENAI_MODEL_NAME"] = "huggingface/meta-llama/Llama-3.1-8B-Instruct"

app = FastAPI()

@app.get("/health/")
async def health():
    return {"status": "up and running"}

@app.post("/analyze-code/")
async def kickoff_crew_endpoint(inputs:dict):
    result_llm = Mirante().crew().kickoff(inputs)
    code_snippet = inputs["python_code"]
    suggestion = result_llm.raw
    conn = db_postgresql.create_table() 
    db_postgresql.insert_table(conn,code_snippet,suggestion)
    return {"Python code original": code_snippet, "Python code improved/corrected": suggestion}

