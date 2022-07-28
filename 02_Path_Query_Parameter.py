from fastapi import FastAPI
from typing import Optional

app = FastAPI()
@app.get('/component/{component_id}') # path parameter
async def get_component(component_id: int):
    return {"component_id": component_id}

@app.get('/component/') # query parameter
async def read_component(id: int, name: Optional[str]):
    return {"id": id, "name": name}
