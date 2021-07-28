# Server 
This is the server, implemented using FastAPI and is the web framework that serves our initial website, handles the web crawler, etc.  

A website consists of multiple parts, but the most important ones are:
1. The *client/frontend*   
   Everything that is visual and interactive is made here. Traditionally, only HTLM, CSS and javascript could be used. HTML controls what components and structure will be seen on your page, CSS controls the UI and layout of the page and Javscript allows for reactivity, logic and manipulation of components on your website.
2. The *server/backend*   
   Takes care of most logic on the website. Can be written in any language. The server defines which end-points (paths) you can visit on a website and serves the files that should be seen when visiting those links. It also handles account verification, database access, scraping of websites, etc.

1. Svelte as our frontend framework along with javascript (Ecmascript 6)
  2. CSS to style our website   
2. FastAPI as our web framework  
  3. Uvicorn as the ASGI server that serves as a interface layer  
4. NGINX as a web server (we will come to that much later)  


# Setup 
Make sure that you have git, python, node, npm and a python virtual environment manager installed   

    git clone PROJECT
    cd PROJECT && pip install -r requirements.txt
    cd client && npm install && cd ..


# Develop 
The easiest setup is to always have the server running in one terminal window and another terminal open for interacting or changing things on the frontend 

To launch the app:    


    cd PROJECT 
    uvicorn server:app --reload 
    # go to http://localhost:8000
    
To develop and test out new things on the frontend only, that does not need the server   

    cd PROJECT/client 
    npm run dev 
    # go to http://localhost:5000
    
To add the new version of the frontend to the server:   

    cd PROJECT/client
    npm run build 
    # and if the server is not running, start it
    cd ..
    uvicorn server:app --reload


# Deep Dive 
## What is a frontend, Svelte, Javascript, etc.?
TODO   

If you thing some languages are weird, wait until you see some of Javascript's quirks :smirk:   

## What is a web server, API and FastAPI?
<details>
  <summary>What is FastAPI and what is the Matrix?</summary>
  Congratulations Neo for asking that question! You are truly the One..!  
    
FastAPI is a high performance framework for writing web frameworks in Python.
It is on par with some Go and Node servers, but with the convenience of Python.
Integrates well with existing Machine Learning toolings and provides static typing for better type hints, fever bugs and generally faster development speed compared to other frameworks.  

Some killer features of FastAPI is the maintainer, automatic REST API documentation AND that the documentation has automatic testing!    

FastAPI is a web framework that allows for modern approaches, such as asynchronous execution of code (do something else while it waits for a response). It allows you to define an API for how applications should access your page. Example: when you type something into Google, you can do it from either the search box or from ulr directly:    

    https://www.google.com/search?q=google  
    
An API defines which paths are available for a program and user to access and what type of things you could get and interact with. APIs allows websites to interact with each other in an easy and standard way. APIs allows you as a developer to integrate existing APIs, such as a Google login on your own page or quickly test out different frontends to users.    

FastAPI is not a web-server, nor is express.js, Django, or Flask a web server, or similar; These are so called *web frameworks* - applications that where you define the web API and logic for what shall happen and be allowed for a user to interact with. All your logic, serving files, processing user requests, fetching and verifying things from a database is usually done from here.   

A **web server** is what processes and forwards incoming requests to and from a website. These web servers are almost always written in C/C++ and needs to be really fast and efficient (hence why C/C++). Web server operate and communicate using the HTTP protocol and is on a very low level. To simplify life, several modern language, implements abstraction layers that can connect to raw socket connections and translate that to a format that is easier to work with. This is similar to how USB or bluetooth is an unifying interface between multiple different applications and hardware.   
  
In python, there are multiple standards for serving as the interface/bridge between Python web frameworks and a web server. The one we are interested in is called [ASGI](https://www.encode.io/articles/hello-asgi#:~:text=In%2Dprocess%20background%20tasks,a%20full%2Dblown%20task%20queue). This interface allows Python applications to interpret and interact asynchronously with a web server. Here, again, there are multiple options, but the most popular and common ASGI server is 
[uvicorn](https://www.uvicorn.org/), and the one we will be using.  

Unfortunately Neo, no one can be told what The Matrix is...  
...Follow the white rabbit.  
</details>

