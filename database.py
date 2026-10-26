# database.py

# Reglas de restricción por condición médica
HEALTH_RESTRICTIONS = {
    "diabetes_resistencia_insulina": {
        "evitar_ingredientes": ["azúcar", "harina refinada", "miel", "arroz blanco", "jugo de fruta"],
        "preferir": ["fibra", "proteínas", "granos integrales", "bajo índice glucémico"]
    },
    "hipertension": {
        "evitar_ingredientes": ["sal añadida", "sodio", "embutidos", "caldos industriales", "salsa de soya"],
        "preferir": ["potasio", "especias naturales", "alimentos frescos"]
    },
    "hipotension": {
        "evitar_ingredientes": ["comidas hipercalóricas pesadas que bajen la presión drásticamente"],
        "preferir": ["moderado aporte de sodio", "hidratación constante", "comidas frecuentes"]
    },
    "saludable": {
        "evitar_ingredientes": [],
        "preferir": ["balanceado"]
    }
}

# Catálogo de recetas
RECIPES_DATABASE = [
    {
        "id": 1,
        "nombre": "Ensalada de Quinoa con Pollo y Paltas",
        "perfiles_aptos": ["diabetes_resistencia_insulina", "hipertension", "saludable"],
        "ingredientes": ["quinoa", "pechuga de pollo", "palta", "tomate", "aceite de oliva", "limón"],
        "calorias": 420,
        "tipo": "Almuerzo"
    },
    {
        "id": 2,
        "nombre": "Salmón al Horno con Espárragos",
        "perfiles_aptos": ["diabetes_resistencia_insulina", "hipertension", "hipotension", "saludable"],
        "ingredientes": ["salmón", "espárragos", "aceite de oliva", "pimienta negra", "limón", "romero"],
        "calorias": 380,
        "tipo": "Almuerzo/Cena"
    },
    {
        "id": 3,
        "nombre": "Sopa Crema de Zapallo con Jengibre (Baja en Sodio)",
        "perfiles_aptos": ["diabetes_resistencia_insulina", "hipertension", "saludable"],
        "ingredientes": ["zapallo camote", "jengibre", "caldo de verduras casero sin sal", "cebolla"],
        "calorias": 210,
        "tipo": "Entrada"
    },
    {
        "id": 4,
        "nombre": "Caldo Concentrado de Huesos y Verduras (Apto Hipotensión)",
        "perfiles_aptos": ["hipotension", "saludable"],
        "ingredientes": ["huesos de res", "apio", "zanahoria", "sal marina moderada", "ajo"],
        "calorias": 180,
        "tipo": "Sopa/Recuperación"
    },
    {
        "id": 5,
        "nombre": "Avena Nocturna con Chía y Frutos Rojos",
        "perfiles_aptos": ["diabetes_resistencia_insulina", "saludable"],
        "ingredientes": ["avena integral", "leche descremada o vegetal sin azúcar", "semillas de chía", "arándanos"],
        "calorias": 310,
        "tipo": "Desayuno"
    }
]