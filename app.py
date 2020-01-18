import uvicorn
from fastapi import FastAPI

# init app
app = FastAPI()

# Routes
@app.get('/')
async def index():
    return {"test": "U kno da fkn VIBES"}

@app.get('/items/{name}')
async def get_items(name:str):
    return {"name": f"sup {name}"}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
