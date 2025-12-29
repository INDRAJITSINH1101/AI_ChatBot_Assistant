import requests

def ask_qwen(prompt):
  url = "http://localhost:11434/api/generate"

  payload = {
        "model": "qwen2.5:7b",
        "prompt": prompt,
        "stream": False
    }
  
  r = requests.post(url, json=payload)
  
  if r.status_code != 200:
        raise Exception(f"Ollama error: {r.text}")

  data = r.json()  
  return data["response"]