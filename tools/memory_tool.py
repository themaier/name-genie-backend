"""
Memory tool for CrewAI agents to maintain context across interactions
"""
from typing import Dict, List, Any
import json
from datetime import datetime


class MemoryStore:
    """Simple in-memory storage for agent context"""
    
    def __init__(self):
        self._storage: Dict[str, List[Dict[str, Any]]] = {}
    
    def save(self, key: str, data: Dict[str, Any]) -> None:
        """Save data to memory with timestamp"""
        if key not in self._storage:
            self._storage[key] = []
        
        entry = {
            'timestamp': datetime.now().isoformat(),
            'data': data
        }
        self._storage[key].append(entry)
    
    def retrieve(self, key: str) -> List[Dict[str, Any]]:
        """Retrieve all entries for a given key"""
        return self._storage.get(key, [])
    
    def retrieve_latest(self, key: str) -> Dict[str, Any] | None:
        """Retrieve the most recent entry for a given key"""
        entries = self.retrieve(key)
        return entries[-1] if entries else None
    
    def clear(self, key: str = None) -> None:
        """Clear memory for a specific key or all keys"""
        if key:
            self._storage.pop(key, None)
        else:
            self._storage.clear()
    
    def get_all_keys(self) -> List[str]:
        """Get all keys in memory"""
        return list(self._storage.keys())
    
    def to_dict(self) -> Dict[str, List[Dict[str, Any]]]:
        """Export memory as dictionary"""
        return self._storage.copy()
    
    def to_json(self) -> str:
        """Export memory as JSON string"""
        return json.dumps(self._storage, indent=2)


# Global memory instance
memory_store = MemoryStore()


class MemoryTool:
    """Tool wrapper for memory operations"""
    
    def __init__(self, store: MemoryStore = None):
        self.store = store or memory_store
    
    def save_context(self, session_id: str, context: Dict[str, Any]) -> str:
        """Save context for a session"""
        self.store.save(session_id, context)
        return f"Context saved for session: {session_id}"
    
    def get_context(self, session_id: str) -> str:
        """Retrieve context for a session"""
        entries = self.store.retrieve(session_id)
        if not entries:
            return f"No context found for session: {session_id}"
        
        latest = entries[-1]
        return f"Latest context: {json.dumps(latest['data'], indent=2)}"
    
    def get_all_context(self, session_id: str) -> str:
        """Retrieve all context history for a session"""
        entries = self.store.retrieve(session_id)
        if not entries:
            return f"No context found for session: {session_id}"
        
        return f"Full context history: {json.dumps(entries, indent=2)}"


# Pre-configured memory tool instance
memory_tool = MemoryTool()
