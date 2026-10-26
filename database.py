# database.py

HEALTH_RESTRICTIONS = {
    "diabetes": {
        "evitar_ingredientes": ["azúcar", "harina refinada", "miel", "arroz blanco", "jugo de fruta", "jarabe"],
        "preferir": ["fibra alta", "proteínas magras", "granos integrales", "bajo índice glucémico estricto"]
    },
    "resistencia_insulina": {
        "evitar_ingredientes": ["azúcar refinada", "harinas blancas", "miel", "dulces procesados"],
        "preferir": ["fibra", "proteínas", "grasas saludables", "carbohidratos complejos"]
    },
    "hipertension": {
        "evitar_ingredientes": ["sal añadida", "sodio alto", "embutidos", "caldos industriales en cubo", "enlatados con sodio"],
        "preferir": ["alimentos frescos", "especias naturales", "potasio", "bajo en sodio"]
    },
    "hipotension": {
        "evitar_ingredientes": ["comidas muy escasas en sal (si requiere ajuste médico)", "alcohol excesivo"],
        "preferir": ["buena hidratación", "sodio moderado", "electrolitos", "comidas fraccionadas"]
    }
}

RECIPES_DATABASE = [
    # --- DESAYUNOS Y MERIENDAS ---
    {
        "id": 1,
        "nombre": "Avena Nocturna con Chía y Frutos Rojos",
        "perfiles_aptos": ["diabetes", "resistencia_insulina", "hipertension", "hipotension"],
        "ingredientes": ["avena integral", "leche descremada o vegetal sin azúcar", "semillas de chía", "arándanos"],
        "calorias": 310,
        "tipo": "Desayuno"
    },
    {
        "id": 2,
        "nombre": "Tostada Integral con Palta y Huevo Pochado",
        "perfiles_aptos": ["diabetes", "resistencia_insulina", "hipertension", "hipotension"],
        "ingredientes": ["pan 100% integral", "palta", "huevo", "pimienta negra", "semillas de sésamo"],
        "calorias": 280,
        "tipo": "Desayuno"
    },
    {
        "id": 3,
        "nombre": "Omelette de Claras con Espinacas y Champiñones",
        "perfiles_aptos": ["diabetes", "resistencia_insulina", "hipertension"],
        "ingredientes": ["claras de huevo", "espinacas frescas", "champiñones", "aceite de oliva"],
        "calorias": 190,
        "tipo": "Desayuno/Cena"
    },
    {
        "id": 4,
        "nombre": "Yogur Griego Sin Azúcar con Almendras y Canela",
        "perfiles_aptos": ["diabetes", "resistencia_insulina", "hipertension", "hipotension"],
        "ingredientes": ["yogur griego natural sin azúcar", "almendras laminadas", "canela en polvo"],
        "calorias": 220,
        "tipo": "Snack/Desayuno"
    },

    # --- ALMUERZOS Y CENAS ---
    {
        "id": 5,
        "nombre": "Ensalada de Quinoa con Pollo y Paltas",
        "perfiles_aptos": ["diabetes", "resistencia_insulina", "hipertension", "hipotension"],
        "ingredientes": ["quinoa", "pechuga de pollo", "palta", "tomate", "aceite de oliva", "limón"],
        "calorias": 420,
        "tipo": "Almuerzo"
    },
    {
        "id": 6,
        "nombre": "Salmón al Horno con Espárragos y Eneldo",
        "perfiles_aptos": ["diabetes", "resistencia_insulina", "hipertension", "hipotension"],
        "ingredientes": ["salmón", "espárragos", "aceite de oliva", "pimienta negra", "limón", "eneldo"],
        "calorias": 380,
        "tipo": "Almuerzo/Cena"
    },
    {
        "id": 7,
        "nombre": "Pavo a la Plancha con Salteado de Brócoli y Pimentón",
        "perfiles_aptos": ["diabetes", "resistencia_insulina", "hipertension"],
        "ingredientes": ["filete de pavo", "brócoli", "pimentón rojo", "ajo", "aceite de oliva"],
        "calorias": 330,
        "tipo": "Almuerzo/Cena"
    },
    {
        "id": 8,
        "nombre": "Bowl de Garbanzos Rostizados con Verduras y Tahini",
        "perfiles_aptos": ["diabetes", "resistencia_insulina", "hipertension", "hipotension"],
        "ingredientes": ["garbanzos cocidos", "pepino", "tomate cherry", "aceitunas", "pasta de tahini", "limón"],
        "calorias": 410,
        "tipo": "Almuerzo"
    },
    {
        "id": 9,
        "nombre": "Pescado a la Reineta con Cilantro y Ensalada de Lentejas",
        "perfiles_aptos": ["diabetes", "resistencia_insulina", "hipertension", "hipotension"],
        "ingredientes": ["reineta fresca", "lentejas cocidas", "cilantro", "cebolla morada", "aceite de oliva", "limón"],
        "calorias": 360,
        "tipo": "Almuerzo"
    },

    # --- SOPAS Y ENTRADAS ---
    {
        "id": 10,
        "nombre": "Sopa Crema de Zapallo con Jengibre (Baja en Sodio)",
        "perfiles_aptos": ["hipertension"],
        "ingredientes": ["zapallo camote", "jengibre", "caldo de verduras casero sin sal", "cebolla"],
        "calorias": 210,
        "tipo": "Entrada/Cena"
    },
    {
        "id": 11,
        "nombre": "Caldo Claro de Pollo e Hortalizas con Romero",
        "perfiles_aptos": ["hipotension", "hipertension"],
        "ingredientes": ["pechuga de pollo con hueso", "apio", "zanahoria", "romero fresco", "pizca de sal mineral"],
        "calorias": 180,
        "tipo": "Entrada/Cena"
    },

    # --- SNACKS Y ACOMPAÑAMIENTOS ---
    {
        "id": 12,
        "nombre": "Hummus Casero con Bastones de Zanahoria y Pepino",
        "perfiles_aptos": ["diabetes", "resistencia_insulina", "hipertension", "hipotension"],
        "ingredientes": ["garbanzos", "tahini", "ajo", "jugo de limón", "zanahoria", "pepino"],
        "calorias": 190,
        "tipo": "Snack"
    },
    {
        "id": 13,
        "nombre": "Mix de Frutos Secos Naturales (Nueces y Caju)",
        "perfiles_aptos": ["diabetes", "resistencia_insulina", "hipertension", "hipotension"],
        "ingredientes": ["nueces de mariposa", "castañas de cajú sin sal", "semillas de zapallo"],
        "calorias": 200,
        "tipo": "Snack"
    }
]
