#!/usr/bin/env python3

import random

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from typing import Optional
from starlette.responses import RedirectResponse

app = FastAPI()

# When running the server it will start on `http://localhost:8000`.
# If we think of our launched application in terms of a folder structure
# Then in order for the server to find new files, we need to specify/add
# New paths/folders for where new files should be added from.
#
# To add the index.html page, we need to specify the folder where it is located.
# We specify that the folder contains the main HTML file  we want the users to see
# However, that file (index.html) tries to find, based on its current location,
# other files in the "/assets" folder. But since that folder isn't visible to
# the server, the index file, when served with FastAPI wont know about those
# either.
#
# In order for the HTML file to find them, we also need to mount the "assets"
# folder. This means that IF any files tries to access any files from "/assets",
# point them to the MOUNTED folder that we have called "/assets".
#
# Thinking of the route as file paths again.
# - The server is "/"
# - The first file served is in a new folder "/index"
# - The assets folder is also a new folder "/assets".
#
# If we from the front-end want to make requests from the server,
# EXAMPLE: get a random number by going to the "/rand" route
# That would then mean that we would need to go "UP" one directory to access
# the "/rand" route. That is the reason for why in `App.Svelte` we are calling
# on `fetch(../rand)`

app.mount("/index", StaticFiles(directory="client/dist", html=True), name="index")
app.mount("/assets", StaticFiles(directory="client/dist/assets"), name="assets")


@app.get("/")
async def front():
    return RedirectResponse(url="index")


@app.get("/rand")
async def hello():
    return random.randint(0, 100)


@app.get("/hello")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
