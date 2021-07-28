#!/usr/bin/env python3

import random

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from typing import Optional
from starlette.responses import RedirectResponse

app = FastAPI()

app.mount("/client", StaticFiles(directory="client/public", html=True), name="client")
app.mount("/build", StaticFiles(directory="client/public/build"), name="build")


@app.get('/')
async def front():
   return RedirectResponse(url='client')

@app.get("/rand")
async def hello():
   return random.randint(0, 100)

@app.get('/hello')
def read_root():
    return {'Hello': 'World'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


