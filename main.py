"""
FastAPI main application entry point
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Keyword Generation AI API",
    description="AI-powered keyword and word suggestion generator using CrewAI",
    version="1.0.0"
)

# Get frontend URL from environment or use default
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        FRONTEND_URL,
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router, prefix="/api", tags=["Keyword Generation"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Keyword Generation AI API",
        "docs": "/docs",
        "health": "/api/health",
        "endpoints": {
            "generate_keywords": "/api/generate-keywords",
            "creative_suggestions": "/api/creative-suggestions"
        }
    }


if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("HOST", "localhost")
    port = int(os.getenv("PORT", 8000))
    
    print(f"Starting server at http://{host}:{port}")
    print(f"API documentation available at http://{host}:{port}/docs")
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True
    )
