from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(
     docs_url="/docs" # This is the URL for your Swagger UI documentation
)


@app.get("/health" , tags=["Health CheckUp"])
def health_check():
    return {
        "msg" : "Health of the server is Ok" 
    }
