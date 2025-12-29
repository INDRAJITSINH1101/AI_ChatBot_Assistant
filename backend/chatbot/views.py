from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .llm import ask_qwen
from .retriever import search
from .trainer import train
from .crawl_train import crawl_and_train
from .status import STATUS

@api_view(['POST'])
def train_api(request):
    train(request.data["text"])
    return Response({"status": "trained"})

@api_view(['POST'])
def chat(request):
    q = request.data["question"]
    docs = search(q)

    prompt = f"""Answer only from this data:{docs}If not found say "I don't know".
        Question: {q}"""
    answer = ask_qwen(prompt)
    return Response({"answer": answer})

@api_view(["POST"])
def crawl_api(request):
    url = request.data["url"]
    crawl_and_train(url)
    return Response({"status":"website trained"})


@api_view(["GET"])
def crawl_status(request):
    return Response(STATUS)
