from typing import Dict, Any, List, Optional
import uuid

class CrudStore:
    def __init__(self):
        self._records: Dict[str, Dict[str, Any]] = {}
        
    def create(self, item: Dict[str, Any]) -> Dict[str, Any]:
        rec = dict(item)
        item_id = str(rec.get("id") or uuid.uuid4())
        rec["id"] = item_id
        self._records[item_id] = rec
        return rec
        
    def get(self, item_id: str) -> Optional[Dict[str, Any]]:
        return self._records.get(item_id)
        
    def update(self, item_id: str, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if item_id not in self._records:
            return None
        self._records[item_id].update(updates)
        return self._records[item_id]
        
    def delete(self, item_id: str) -> bool:
        return self._records.pop(item_id, None) is not None
        
    def list_all(self) -> List[Dict[str, Any]]:
        return list(self._records.values())
