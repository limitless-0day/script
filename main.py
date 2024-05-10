from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# 模拟数据库中的数据
scripts_db = [
    {"id": 1, "name": "安装nginx", "command": "sudo apt-get install nginx"},
    {"id": 2, "name": "安装MySQL", "command": "sudo apt-get install mysql-server"},
]


class Script(BaseModel):
    id: int
    name: str
    command: str


class ScriptIn(BaseModel):
    name: str
    command: str


def get_script(script_id: int) -> Script:
    for script in scripts_db:
        if script["id"] == script_id:
            return Script(**script)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Script not found")


@app.get("/v1/scripts", response_model=List[Script])
def get_scripts():
    return [Script(**script) for script in scripts_db]


@app.post("/v1/scripts", response_model=Script, status_code=status.HTTP_201_CREATED)
def create_script(script: ScriptIn):
    new_script = {"id": len(scripts_db) + 1, "name": script.name, "command": script.command}
    scripts_db.append(new_script)
    return Script(**new_script)


@app.put("/v1/scripts/{script_id}", response_model=Script)
def update_script(script_id: int, script: ScriptIn):
    existing_script = get_script(script_id)
    updated_script = {"id": script_id, "name": script.name or existing_script.name, "command": script.command or existing_script.command}
    scripts_db[scripts_db.index(existing_script)] = updated_script
    return Script(**updated_script)


@app.delete("/v1/scripts/{script_id}", response_model=Script)
def delete_script(script_id: int):
    existing_script = get_script(script_id)
    scripts_db.remove(existing_script)
    return existing_script


@app.get("/v1/scripts/{script_id}", response_model=Script)
def get_script_by_id(script_id: int):
    return get_script(script_id)


@app.get("/v1/scripts/search", response_model=List[Script])
def search_scripts(q: str):
    return [Script(**script) for script in scripts_db if q.lower() in script["name"].lower() or q.lower() in script["command"].lower()]