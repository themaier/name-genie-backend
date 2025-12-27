"""
FastAPI routes for CrewAI backend
"""
from fastapi import APIRouter, HTTPException
from api.models import (
    KeywordRequest,
    KeywordResponse,
    CreativityRequest,
    CreativityResponse,
    HealthResponse
)
from crew import CrewManager
from tools import memory_store, creativity_tool

router = APIRouter()
crew_manager = CrewManager()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="ok",
        message="Keyword Generation AI is running"
    )


@router.post("/generate-keywords", response_model=KeywordResponse)
async def generate_keywords(request: KeywordRequest):
    """Generate keyword and word suggestions for a topic"""
    try:
        result = crew_manager.generate_keywords(
            topic_description=request.topic_description,
            use_search=request.use_search,
            creativity_level=request.creativity_level
        )
        
        # Save to memory
        memory_store.save("keyword_generation", {
            "topic": request.topic_description,
            "creativity_level": request.creativity_level,
            "result": result.get("keywords", "")
        })
        
        return KeywordResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/creative-suggestions", response_model=CreativityResponse)
async def get_creative_suggestions(request: CreativityRequest):
    """Get creative word suggestions using the creativity tool"""
    try:
        suggestions = creativity_tool.get_creative_suggestions(
            topic=request.topic,
            count=request.count
        )
        
        return CreativityResponse(
            success=True,
            suggestions=suggestions
        )
    
    except Exception as e:
        return CreativityResponse(
            success=False,
            error=str(e)
        )


@router.get("/memory/{session_id}")
async def get_memory(session_id: str):
    """Retrieve memory for a session"""
    try:
        entries = memory_store.retrieve(session_id)
        return {
            "success": True,
            "session_id": session_id,
            "entries": entries
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/memory/{session_id}")
async def clear_memory(session_id: str):
    """Clear memory for a session"""
    try:
        memory_store.clear(session_id)
        return {
            "success": True,
            "message": f"Memory cleared for session: {session_id}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
