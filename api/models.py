"""
Pydantic models for API requests and responses
"""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class KeywordRequest(BaseModel):
    """Request model for keyword generation"""
    topic_description: str = Field(..., description="Description of the topic/concept")
    use_search: bool = Field(default=True, description="Enable web search for trending keywords")
    creativity_level: str = Field(default="high", description="Creativity level: low, medium, or high")
    
    class Config:
        json_schema_extra = {
            "example": {
                "topic_description": "A modern AI-powered productivity app for remote teams",
                "use_search": True,
                "creativity_level": "high"
            }
        }


class KeywordResponse(BaseModel):
    """Response model for keyword generation"""
    success: bool
    keywords: Optional[str] = None
    creative_suggestions: Optional[Dict[str, List[str]]] = None
    topic: Optional[str] = None
    creativity_level: Optional[str] = None
    search_enabled: Optional[bool] = None
    error: Optional[str] = None


class CreativityRequest(BaseModel):
    """Request model for creativity tool suggestions"""
    topic: str = Field(..., description="Topic or phrase to generate suggestions for")
    count: int = Field(default=20, description="Number of suggestions per category")
    
    class Config:
        json_schema_extra = {
            "example": {
                "topic": "cloud storage solution",
                "count": 15
            }
        }


class CreativityResponse(BaseModel):
    """Response model for creativity suggestions"""
    success: bool
    suggestions: Optional[Dict[str, List[str]]] = None
    error: Optional[str] = None


class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    message: str
