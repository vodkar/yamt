#!/usr/bin/python
import uvicorn

from yamt.api import app

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)
