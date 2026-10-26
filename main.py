# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "mensaje": "Bienvenido a la API de Recetas Saludables",
        "estado": "Servidor activo y funcionando correctamente"
    }
# --------------------------------------
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from recommender import get_recommendations_for_profile
from database import HEALTH_RESTRICTIONS, RECIPES_DATABASE

app = FastAPI(
    title="API de Recomendación de Recetas Clínicas",
    description="Sistema backend para recomendar recetas según condiciones de salud crónicas.",
    version="1.0.0"
)

# Endpoint raíz para solucionar el error de Not Found en "/"
@app.get("/")
def read_root():
    return {
        "mensaje": "Bienvenido a la API de Recetas Saludables",
        "perfiles_disponibles": list(HEALTH_RESTRICTIONS.keys())
    }

@app.get("/recetas/{profile}")
def get_recetas(profile: str):
    result = get_recommendations_for_profile(profile)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

class CustomRecipe(BaseModel):
    nombre: str
    perfiles_aptos: list[str]
    ingredientes: list[str]
    calorias: int
    tipo: str

@app.post("/recetas/agregar")
def add_recipe(recipe: CustomRecipe):
    new_recipe = recipe.dict()
    new_recipe["id"] = len(RECIPES_DATABASE) + 1
    RECIPES_DATABASE.append(new_recipe)
    return {"mensaje": "Receta agregada exitosamente", "receta": new_recipe}

# Add CORSMiddleware in main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],
)
