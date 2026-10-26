# database.py - Base de Datos Clínica Ampliada para NutriLife API

RECETAS_CLINICAS = {
    "diabetes": {
        "restricciones_perfil": {
            "preferir": [
                "fibra alta", 
                "proteínas magras", 
                "granos integrales", 
                "bajo índice glucémico",
                "vegetales de hoja verde"
            ],
            "evitar_ingredientes": [
                "azúcar refinada", 
                "harina blanca", 
                "miel / jarabes", 
                "arroz blanco", 
                "jugo de frutas industrializado"
            ]
        },
        "recetas_recomendadas": [
            # DESAYUNOS (5)
            {"id": 101, "nombre": "Avena Nocturna con Chía y Arándanos", "calorias": 290, "tipo": "Desayuno", "ingredientes": ["avena integral", "leche descremada", "semillas de chía", "arándanos frescos", "canela"]},
            {"id": 102, "nombre": "Omelette de Claras con Espinaca y Champiñones", "calorias": 220, "tipo": "Desayuno", "ingredientes": ["claras de huevo", "espinaca fresca", "champiñones picados", "aceite de oliva extra virgen"]},
            {"id": 103, "nombre": "Tostada Integral con Palta y Semillas de Lino", "calorias": 260, "tipo": "Desayuno", "ingredientes": ["pan 100% integral", "palta molida", "semillas de lino", "tomate cherry"]},
            {"id": 104, "nombre": "Yogur Griego Natural con Frambuesas y Almendras", "calorias": 210, "tipo": "Desayuno", "ingredientes": ["yogur griego 0% grasa sin azúcar", "frambuesas", "almendras laminadas"]},
            {"id": 105, "nombre": "Pancakes de Avena, Clara de Huevo y Manzana", "calorias": 280, "tipo": "Desayuno", "ingredientes": ["harina de avena", "claras de huevo", "manzana verde rallada", "canela en polvo"]},
            
            # ALMUERZOS (5)
            {"id": 106, "nombre": "Pechuga de Pollo a la Plancha con Quinoa y Brócoli", "calorias": 410, "tipo": "Almuerzo", "ingredientes": ["pechuga de pollo", "quinoa cocida", "brócoli al vapor", "aceite de oliva", "limón"]},
            {"id": 107, "nombre": "Filete de Reineta al Horno con Verduras Salteadas", "calorias": 360, "tipo": "Almuerzo", "ingredientes": ["filete de reineta", "zapallo italiano", "pimentón verde", "cebolla", "ajo"]},
            {"id": 108, "nombre": "Ensalada de Lentejas con Pavo Desmenuzado y Tomate", "calorias": 390, "tipo": "Almuerzo", "ingredientes": ["lentejas cocidas", "pechuga de pavo", "tomate fresco", "pepino", "perejil"]},
            {"id": 109, "nombre": "Salmón a la Parrilla con Espárragos y Ensalada Verde", "calorias": 440, "tipo": "Almuerzo", "ingredientes": ["filete de salmón", "espárragos frescos", "lechuga hidropónica", "palta"]},
            {"id": 110, "nombre": "Guiso de Garbanzos con Acelga y Tofu Firme", "calorias": 380, "tipo": "Almuerzo", "ingredientes": ["garbanzos", "acelga fresca", "tofu firme en cubos", "comino", "cebolla"]},
            
            # CENAS (5)
            {"id": 111, "nombre": "Crema de Zapallo e Hinojo sin Crema", "calorias": 190, "tipo": "Cena", "ingredientes": ["zapallo camote", "hinojo fresco", "caldo de verduras casero", "semillas de calabaza"]},
            {"id": 112, "nombre": "Tacos de Hojas de Lechuga con Pavo y Palta", "calorias": 270, "tipo": "Cena", "ingredientes": ["hojas de lechuga costina", "carne molida de pavo magra", "palta en cubos", "cilantro"]},
            {"id": 113, "nombre": "Sopa Clara de Verduras con Filete de Merluza", "calorias": 230, "tipo": "Cena", "ingredientes": ["filete de merluza", "apio", "zanahoria", "zapallo italiano", "cilantro"]},
            {"id": 114, "nombre": "Tortilla de Acelga y Claras al Horno", "calorias": 210, "tipo": "Cena", "ingredientes": ["acelga al vapor", "claras de huevo", "cebollín", "aceite de oliva"]},
            {"id": 115, "nombre": "Ceviche de Pescado Blanco con Cítricos y Pepino", "calorias": 240, "tipo": "Cena", "ingredientes": ["pescado blanco fresco", "jugo de limón", "pepino", "cebolla morada", "cilantro"]},
            
            # SNACKS (2)
            {"id": 116, "nombre": "Bastones de Celery con Hummus de Garbanzo", "calorias": 140, "tipo": "Snack", "ingredientes": ["bastones de apio", "hummus casero", "pimentón en polvo"]},
            {"id": 117, "nombre": "Nueces e Higos Secos Controlados", "calorias": 160, "tipo": "Snack", "ingredientes": ["nueces mariposa", "semillas de girasol"]}
        ]
    },

    "resistencia_insulina": {
        "restricciones_perfil": {
            "preferir": [
                "altas proteínas magras", 
                "grasas saludables (Omega 3)", 
                "carbohidratos de digestión lenta", 
                "abundantes vegetales verdes"
            ],
            "evitar_ingredientes": [
                "azúcar", 
                "harinas de trigo refinadas", 
                "bebidas endulzadas", 
                "alimentos procesados", 
                "mermeladas tradicionales"
            ]
        },
        "recetas_recomendadas": [
            # DESAYUNOS (5)
            {"id": 201, "nombre": "Tostada Integral con Palta y Huevo Pochado", "calorias": 280, "tipo": "Desayuno", "ingredientes": ["pan 100% integral de grano entero", "palta", "huevo pochado", "semillas de sésamo"]},
            {"id": 202, "nombre": "Pudín de Chía con Leche de Almendras y Canela", "calorias": 210, "tipo": "Desayuno", "ingredientes": ["semillas de chía", "leche de almendras sin azúcar", "extracto de vainilla", "canela"]},
            {"id": 203, "nombre": "Scramble de Huevos con Pimentón y Ricotta", "calorias": 250, "tipo": "Desayuno", "ingredientes": ["huevos enteros", "pimentón rojo picado", "queso ricotta descremado", "ciboulette"]},
            {"id": 204, "nombre": "Yogur Griego con Semillas de Zapallo y Moras", "calorias": 220, "tipo": "Desayuno", "ingredientes": ["yogur griego natural sin azúcar", "semillas de zapallo", "moras frescas"]},
            {"id": 205, "nombre": "Batido Verde Proteico de Espinaca y Proteína Limpia", "calorias": 230, "tipo": "Desayuno", "ingredientes": ["espinaca baby", "proteína vegetal aislada", "leche de coco sin azúcar", "pepino"]},

            # ALMUERZOS (5)
            {"id": 206, "nombre": "Salmón al Horno con Espárragos y Ensalada de Rúcula", "calorias": 420, "tipo": "Almuerzo", "ingredientes": ["filete de salmón", "espárragos", "rúcula fresca", "aceite de oliva", "limón"]},
            {"id": 207, "nombre": "Pechuga de Pollo al Curry con Vegetales Salteados", "calorias": 380, "tipo": "Almuerzo", "ingredientes": ["pechuga de pollo", "curry suave", "brócoli", "pimentón", "cebolla morada"]},
            {"id": 208, "nombre": "Bistec Magro a la Plancha con Puré de Coliflor", "calorias": 390, "tipo": "Almuerzo", "ingredientes": ["posta negra o lomo liso magro", "coliflor al vapor en puré", "aceite de oliva", "ajo"]},
            {"id": 209, "nombre": "Ensalada de Atún al Agua con Arroz Integral y Palta", "calorias": 410, "tipo": "Almuerzo", "ingredientes": ["atún al agua", "arroz integral cocido", "palta", "tomate", "lechuga"]},
            {"id": 210, "nombre": "Tofu Marinado a la Plancha con Quinoa y Zapallo", "calorias": 350, "tipo": "Almuerzo", "ingredientes": ["tofu firme", "salsa de soya baja en sodio", "quinoa", "zapallo italiano"]},

            # CENAS (5)
            {"id": 211, "nombre": "Sopa de Verduras Mixtas y Tofu Firme", "calorias": 220, "tipo": "Cena", "ingredientes": ["tofu en cubos", "apio", "zanahoria", "espinaca", "caldo de verduras"]},
            {"id": 212, "nombre": "Pechuga de Pavo al Horno con Ensalada de Pepino y Huevo", "calorias": 290, "tipo": "Cena", "ingredientes": ["pechuga de pavo", "pepino en rodajas", "huevo duro", "limón"]},
            {"id": 213, "nombre": "Salteado de Mariscos con Brócoli y Dientes de Dragón", "calorias": 270, "tipo": "Cena", "ingredientes": ["camarones o calamares", "brócoli", "dientes de dragón", "aceite de sésamo"]},
            {"id": 214, "nombre": "Crema de Espárragos Ligera con Semillas de Girasol", "calorias": 180, "tipo": "Cena", "ingredientes": ["espárragos verdes", "caldo claro", "semillas de girasol tostadas"]},
            {"id": 215, "nombre": "Pescado Blanco a la Vasca con Tomate y Pimentón", "calorias": 260, "tipo": "Cena", "ingredientes": ["filete de pescado blanco", "tomate picado", "pimentón rojo", "cebolla", "ajo"]},

            # SNACKS (2)
            {"id": 216, "nombre": "Mix de Nueces y Almendras Tostadas", "calorias": 170, "tipo": "Snack", "ingredientes": ["nueces", "almendras sin sal"]},
            {"id": 217, "nombre": "Rollitos de Jamón de Pavo con Queso Fresco Light", "calorias": 130, "tipo": "Snack", "ingredientes": ["jamón de pavo bajo en grasa", "queso fresco sin sal"]}
        ]
    },

    "hipertension": {
        "restricciones_perfil": {
            "preferir": [
                "alimentos frescos sin procesar", 
                "especias e hierbas aromáticas", 
                "potasio y magnesio natural", 
                "bajo en sodio"
            ],
            "evitar_ingredientes": [
                "sal de mesa añadida", 
                "embutidos y conservas", 
                "caldos concentrados en cubo", 
                "salsas industriales", 
                "snacks salados"
            ]
        },
        "recetas_recomendadas": [
            # DESAYUNOS (5)
            {"id": 301, "nombre": "Bowl de Frutas Frescas con Plátano y Arándanos", "calorias": 220, "tipo": "Desayuno", "ingredientes": ["plátano (rico en potasio)", "arándanos frescos", "semillas de lino molidas"]},
            {"id": 302, "nombre": "Avena Cocida con Manzana Verde y Canela", "calorias": 250, "tipo": "Desayuno", "ingredientes": ["avena en hojuelas", "manzana verde picada", "canela en polvo", "agua o leche vegetal"]},
            {"id": 303, "nombre": "Smoothie Potenciador de Magnesio de Espinaca y Pera", "calorias": 190, "tipo": "Desayuno", "ingredientes": ["espinaca fresca", "pera madura", "agua de coco natural", "semillas de chía"]},
            {"id": 304, "nombre": "Pan Integral sin Sal con Ricotta y Mermelada Casera sin Azúcar", "calorias": 230, "tipo": "Desayuno", "ingredientes": ["pan 100% integral preparado sin sal", "queso ricotta", "frutillas cocidas"]},
            {"id": 305, "nombre": "Tostada con Puré de Palta y Cilantro Fresco", "calorias": 240, "tipo": "Desayuno", "ingredientes": ["pan pita integral sin sal", "palta", "cilantro picado", "jugo de limón"]},

            # ALMUERZOS (5)
            {"id": 306, "nombre": "Pechuga de Pollo a las Hierbas Finas con Camote al Horno", "calorias": 390, "tipo": "Almuerzo", "ingredientes": ["pechuga de pollo", "camote (batata) al horno", "romero", "orégano", "limón"]},
            {"id": 307, "nombre": "Merluza al Vapor con Ensalada de Espinacas y Nueces", "calorias": 330, "tipo": "Almuerzo", "ingredientes": ["filete de merluza", "espinaca baby", "nueces picadas", "aceite de oliva extra virgen"]},
            {"id": 308, "nombre": "Guiso de Lentejas Cortas con Tomate Natural y Cúrcuma", "calorias": 360, "tipo": "Almuerzo", "ingredientes": ["lentejas cocidas", "tomate natural triturado", "zanahoria", "cúrcuma", "laurel"]},
            {"id": 309, "nombre": "Pavita al Horno con Quinoa y Salteado de Pimentones", "calorias": 380, "tipo": "Almuerzo", "ingredientes": ["pechuga de pavo", "quinoa", "pimentón rojo y amarillo", "cebollín"]},
            {"id": 310, "nombre": "Tazón Nutritivo de Garbanzos, Betarraga y Palta", "calorias": 400, "tipo": "Almuerzo", "ingredientes": ["garbanzos cocidos sin sal", "betarraga rallada", "palta", "semillas de sésamo"]},

            # CENAS (5)
            {"id": 311, "nombre": "Crema de Zapallo Camote y Jengibre sin Sal", "calorias": 180, "tipo": "Cena", "ingredientes": ["zapallo camote", "jengibre rallado", "cebolla", "aceite de oliva"]},
            {"id": 312, "nombre": "Pescado a la Planche con Ensalada de Pepino y Eneldo", "calorias": 250, "tipo": "Cena", "ingredientes": ["filete de pescado fresco", "pepino", "eneldo fresco", "jugo de limón"]},
            {"id": 313, "nombre": "Sopa Ligera de Zanahoria y Cilantro", "calorias": 160, "tipo": "Cena", "ingredientes": ["zanahoria", "cilantro fresco", "caldo vegetal casero sin sal", "aceite de oliva"]},
            {"id": 314, "nombre": "Omelette de Claras con Champiñones al Tomillo", "calorias": 200, "tipo": "Cena", "ingredientes": ["claras de huevo", "champiñones laminados", "tomillo fresco", "aceite de oliva"]},
            {"id": 315, "nombre": "Salteado de Zapallito Italiano, Tomate y Albahaca", "calorias": 170, "tipo": "Cena", "ingredientes": ["zapallo italiano en cubos", "tomate cherry", "albahaca fresca", "ajo"]},

            # SNACKS (2)
            {"id": 316, "nombre": "Bastones de Pepino y Zanahoria con Limón y Oregano", "calorias": 90, "tipo": "Snack", "ingredientes": ["pepino", "zanahoria", "jugo de limón", "orégano"]},
            {"id": 317, "nombre": "Manzana Horneada con Canela", "calorias": 110, "tipo": "Snack", "ingredientes": ["manzana roja", "canela en polvo"]}
        ]
    },

    "hipotension": {
        "restricciones_perfil": {
            "preferir": [
                "hidratación constante", 
                "sodio moderado en las comidas", 
                "electrolitos naturales", 
                "comidas fraccionadas"
            ],
            "evitar_ingredientes": [
                "ayunos prolongados", 
                "comidas excesivamente copiosas", 
                "dietas restrictivas extremas en sal"
            ]
        },
        "recetas_recomendadas": [
            # DESAYUNOS (5)
            {"id": 401, "nombre": "Tostadas Integrales con Queso Fresco y Tomate", "calorias": 310, "tipo": "Desayuno", "ingredientes": ["pan integral", "queso fresco moderadamente salado", "tomate", "aceite de oliva"]},
            {"id": 402, "nombre": "Omelette Completo con Pimentón y Jamón de Pavo", "calorias": 290, "tipo": "Desayuno", "ingredientes": ["huevos enteros", "jamón de pavo", "pimentón picado", "pizca de sal marina"]},
            {"id": 403, "nombre": "Sandwich en Pan Pita con Hummus, Aceitunas y Espinaca", "calorias": 320, "tipo": "Desayuno", "ingredientes": ["pan pita integral", "hummus", "aceitunas negras picadas", "espinaca"]},
            {"id": 404, "nombre": "Yogur Natural con Granola, Almendras Saladas y Miel", "calorias": 300, "tipo": "Desayuno", "ingredientes": ["yogur natural", "granola casera", "almendras tostadas con sal", "miel de abeja"]},
            {"id": 405, "nombre": "Batido de Plátano, Leche de Cereal y Sal de Mar", "calorias": 270, "tipo": "Desayuno", "ingredientes": ["plátano maduro", "leche descremada o vegetal", "pizca de sal marina", "mantequilla de maní"]},

            # ALMUERZOS (5)
            {"id": 406, "nombre": "Arroz Integral con Pollo al Jugo y Verduras", "calorias": 440, "tipo": "Almuerzo", "ingredientes": ["arroz integral", "muslo o pechuga de pollo", "zanahoria", "caldo con sazón casera"]},
            {"id": 407, "nombre": "Carne de Vacuno Magra con Ensalada Rusa Ligera", "calorias": 460, "tipo": "Almuerzo", "ingredientes": ["posta negra o rosada", "papas cocidas", "zanahoria", "mayonesa casera ligera"]},
            {"id": 408, "nombre": "Pastel de Papas Ligero con Carne de Pavo", "calorias": 430, "tipo": "Almuerzo", "ingredientes": ["papa en puré", "pavo molido", "cebolla", "huevo duro", "aceitunas"]},
            {"id": 409, "nombre": "Garbanzos Salteados con Espinaca, Ajo y Bacalao", "calorias": 420, "tipo": "Almuerzo", "ingredientes": ["garbanzos cocidos", "espinaca", "trozos de bacalao o pescado salado", "ajo"]},
            {"id": 410, "nombre": "Pasta Integral con Salsa de Tomate Casera y Queso Parmesano", "calorias": 450, "tipo": "Almuerzo", "ingredientes": ["pasta 100% integral", "salsa de tomate natural sazonada", "queso parmesano rallado"]},

            # CENAS (5)
            {"id": 411, "nombre": "Caldo Claro de Pollo e Hortalizas Frescas", "calorias": 220, "tipo": "Cena", "ingredientes": ["pechuga de pollo", "apio", "zanahoria", "perejil", "pizca de sal mineral"]},
            {"id": 412, "nombre": "Consomé de Verduras con Huevo Hilado", "calorias": 190, "tipo": "Cena", "ingredientes": ["caldo de verduras sazonado", "huevo batido", "cebollín", "espinacas"]},
            {"id": 413, "nombre": "Sopa de Fideos Integrales con Pollo y Verduras", "calorias": 280, "tipo": "Cena", "ingredientes": ["fideos integrales cortos", "pollo desmenuzado", "zapallo italiano", "caldo casero"]},
            {"id": 414, "nombre": "Tortilla de Papas y Cebolla con Ensalada Verde", "calorias": 310, "tipo": "Cena", "ingredientes": ["papas en láminas", "huevos", "cebolla salteada", "lechuga y tomate"]},
            {"id": 415, "nombre": "Crema de Verduras Mixtas con Crutones Integrales", "calorias": 240, "tipo": "Cena", "ingredientes": ["zapallo, zanahoria y apio", "crutones de pan integral", "pizca de sal y pimienta"]},

            # SNACKS (2)
            {"id": 416, "nombre": "Aceitunas Verdes y Almendras Tostadas", "calorias": 160, "tipo": "Snack", "ingredientes": ["aceitunas verdes", "almendras tostadas con sal"]},
            {"id": 417, "nombre": "Queso Crotin o Queso Fresco con Galletas Integrales", "calorias": 180, "tipo": "Snack", "ingredientes": ["queso fresco", "galletas de agua integrales"]}
        ]
    }
}
