import sys,os
from typing import Any

def createResponse(status: int, message: Any) -> dict:
    return {
        "status": status,
        "message": message
    }