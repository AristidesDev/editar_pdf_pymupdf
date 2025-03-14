import fitz  # PyMuPDF

letra = "J"
num1 = "31552665"
num2 = "7"
rif = f"{letra}-{num1}-{num2}"

def insertar_varios_textos(input_pdf, output_pdf, textos):
    doc = fitz.open(input_pdf)
    
    for config in textos:
        pagina = doc[config["pagina"]]
        
        # Configuración básica
        texto = config["texto"]
        x = config["x"]
        y = config["y"]
        font_size = config.get("font_size", 12)
        font_name = config.get("font_name", "helv")
        color_text = config.get("color_text", (0, 0, 0))

        # Insertar texto directamente en la posición especificada
        pagina.insert_text(
            point=(x, y),
            text=texto,
            fontname=font_name,
            fontsize=font_size,
            color=color_text
        )
    
    doc.save(output_pdf)
    doc.close()

# Configuración simplificada
textos = [
# REGISTRO DE INFORMACION FISCAL
    # RIF
    {
        "pagina": 0, # numero de pagina a editar
        "texto": rif, # Texto a introducir
        "font_name": "hebo", # nombre de la fuente
        "font_size": 11, # Tamano de la fuente
        "color_text" : (0, 0, 0), # Color del texto (RGB)
        "x": 315, # posicion inical en X
        "y": 77, # posicion inical en Y
    },

# FOOTER
    # NUMERO DE CONTROL
    # Numero de control inicio
    {
        "pagina": 0,  
        "texto": "000000",  
        "font_name": "hebo",  
        "font_size": 5,  
        "color_text" : (0, 0, 0),   
        "x": 97.50,  
        "y": 561.50,  
    },

    # Numero de control final
    {
        "pagina": 0,  
        "texto": "000000",  
        "font_name": "hebo",  
        "font_size": 5,  
        "color_text" : (0, 0, 0),   
        "x": 133.00,  
        "y": 561.50,  
    },

    # NUMERO DE FACTURA
    # Numero de factura inicio
    {
        "pagina": 0,  
        "texto": "000000",  
        "font_name": "hebo",  
        "font_size": 5,  
        "color_text" : (0, 0, 0),   
        "x": 206.00,  
        "y": 561.50,  
    },

    # Numero de factura final
    {
        "pagina": 0,  
        "texto": "000000",  
        "font_name": "hebo",  
        "font_size": 5,  
        "color_text" : (0, 0, 0),   
        "x": 241.00,  
        "y": 561.50,  
    },

    #FECHA DE ELABORACION
    # Numero 1 del Dia 
    {
        "pagina": 0,  
        "texto": "0",  
        "font_name": "hebo",  
        "font_size": 5,  
        "color_text" : (0, 0, 0),   
        "x": 272.85,  
        "y": 561.50,  
    },

    # Numero 2 del Dia 
    {
        "pagina": 0,  
        "texto": "0",  
        "font_name": "hebo",  
        "font_size": 5,  
        "color_text" : (0, 0, 0),   
        "x": 286.60,  
        "y": 561.50,  
    },

    # Numero 1 del Mes 
    {
        "pagina": 0,  
        "texto": "0",  
        "font_name": "hebo",  
        "font_size": 5,  
        "color_text" : (0, 0, 0),   
        "x": 300.40,  
        "y": 561.50,  
    },

   # Numero 2 del Mes 
    {
        "pagina": 0,  
        "texto": "0",  
        "font_name": "hebo",  
        "font_size": 5,  
        "color_text" : (0, 0, 0),   
        "x": 314.00,  
        "y": 561.50,  
    },

    # Numero 1 del Año 
    {
        "pagina": 0,  
        "texto": "0",  
        "font_name": "hebo",  
        "font_size": 5,  
        "color_text" : (0, 0, 0),   
        "x": 328.00,  
        "y": 561.50,  
    },

    # Numero 2 del Año 
    {
        "pagina": 0,  
        "texto": "0",  
        "font_name": "hebo",  
        "font_size": 5,  
        "color_text" : (0, 0, 0),   
        "x": 341.70,  
        "y": 561.50,  
    },

    # Numero 3 del Año 
    {
        "pagina": 0,  
        "texto": "0",  
        "font_name": "hebo",  
        "font_size": 5,  
        "color_text" : (0, 0, 0),   
        "x": 355.50,  
        "y": 561.50,  
    },

    # Numero 4 del Año 
    {
        "pagina": 0,  
        "texto": "0",  
        "font_name": "hebo",  
        "font_size": 5,  
        "color_text" : (0, 0, 0),   
        "x": 369.30,  
        "y": 561.50, 
    },
]

insertar_varios_textos(
    input_pdf="static/Template_Factura_Vertical_SVG.pdf", 
    output_pdf="new_document/documento_con_texto.pdf",
    textos=textos
)