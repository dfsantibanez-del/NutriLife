# recommender.py
from database import RECIPES_DATABASE, HEALTH_RESTRICTIONS

def get_recommendations_for_profile(profile_name: str):
    """
    Filtra las recetas basándose estrictamente en el perfil de salud crónico ingresado.
    """
    profile_key = profile_name.lower().strip().replace(" ", "_")
    
    if profile_key not in HEALTH_RESTRICTIONS:
        return {
            "error": "Perfil no encontrado. Los perfiles válidos son: diabetes_resistencia_insulina, hipertension, hipotension, saludable"
        }
    
    # Filtrar recetas que incluyan el perfil en su lista de aptos
    matched_recipes = [
        recipe for recipe in RECIPES_DATABASE 
        if profile_key in recipe["perfiles_aptos"]
    ]
    
    return {
        "perfil": profile_key,
        "recomendaciones_nutricionales": HEALTH_RESTRICTIONS[profile_key],
        "total_recetas": len(matched_recipes),
        "recetas": matched_recipes
    }