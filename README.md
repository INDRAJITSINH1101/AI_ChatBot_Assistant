🔥 Key Features

  🌐 Website Auto-Crawling

    Crawls all pages of a website
    
    Extracts clean text
    
    Automatically trains the AI

  🧠 RAG (Retrieval-Augmented Generation)

    Uses E5 embeddings to convert text into vectors
    
    Stores them in ChromaDB
    
    Retrieves only relevant data for each question

  🤖 LLM Integration
  
    Powered by Qwen-3 (via Ollama)
    
    Generates answers strictly from retrieved website data
    
    No hallucinations (says “I don’t know” if data is missing)

  📊 Real-Time Training Progress

    Terminal progress bar with 0–100% percentage
    
    Shows pages and chunks being trained live

  🔗 Django REST API

    /api/train → Add manual knowledge
    
    /api/crawl → Crawl & train a website
    
    /api/chat → Ask questions
    
    /api/status → View training progress

  🧪 Postman Ready

    Fully testable via REST APIs
    
    No frontend required
