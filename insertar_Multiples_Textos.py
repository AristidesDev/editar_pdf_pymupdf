import fitz  # PyMuPDF

def insertar_varios_textos(input_pdf, output_pdf, textos):
    doc = fitz.open(input_pdf)
    
    for config in textos:
        pagina = doc[config["pagina"]]
        
        # Parámetros básicos
        texto = config["texto"]
        x = config["x"]
        y = config["y"]
        padding = config.get("padding", 0)
        font_size = config.get("font_size", 12)
        font_name = config.get("font_name", "helv")
        color_text = config.get("color_text", (0, 0, 0))
        # color_rect_backgraound = config.get("color_background")
        # width_border = config.get("width_border")
        # color_rect_border = config.get("color_border")
        
        # Si se usa alineación, definir el rectángulo del textbox
        if "align" in config:
            # Ancho y alto del cuadro de texto (obligatorios si hay alineación)
            width_box = config.get("width", 200)  # Ancho predeterminado: 200 puntos
            height_box = config.get("height", 100)  # Alto predeterminado: 100 puntos

            # Definir el rectángulo (x1, y1, x2, y2)
            rect = fitz.Rect(
                x + padding,                  # Esquina superior izquierda (x)
                y + padding,                  # Esquina superior izquierda (y)
                x + width_box - padding,          # Esquina inferior derecha (x + ancho)
                y + height_box - padding           # Esquina inferior derecha (y + alto)
            )
            # # Dibujar el rectángulo en la pagina
            # pagina.draw_rect(
            #     rect,
            #     fill = None,   # Relleno del rectángulo
            #     width = 1,   
            #     color = None,  # Color del border
            # )
            
            # Insertar texto en el rectángulo

            pagina.insert_textbox(
                rect,
                texto,
                fontname=font_name,
                fontsize=font_size,
                align=config["align"],
                color=color_text,
            )

        else:
            # Insertar texto en una posición específica (sin cuadro)
            pagina.insert_text(
                point=(x, y),
                text=texto,
                fontname=font_name,
                fontsize=font_size,
                color=color_text
            )
    
    doc.save(output_pdf)
    doc.close()

# Ejemplo de uso con rectángulos definidos
textos = [
    {
        "pagina": 0, # numero de pagina a editar
        "texto": "INFORME FINAL", # Texto a introducir 
        "font_size": 12, # Tamano de la fuente
        "font_name": "tiro", # nombre de la fuente
        "color_text" : (0.25, 0.75, 0.75), # Color del texto (RGB)
        "align": 1,  # Alineacion 0=izquierda, 1=centro, 2=derecha
        "padding" : 0, # Separacion de texto respecto al border de rectángulo 
        "x": 75, # posicion inical en X
        "y": 75, # posicion inical en Y
        "width": 100,  # Ancho del cuadro
        "height": 150,   # Alto del cuadro
        # "color_background" : (0, 0, 0),  # Color del fondo del rectángulo (RGB)
        # "width_border" : 0 # Grosor del border del rectángulo
        # "color_border" : (0.25, 0.75, 0.75), # Color del border del rectángulo (RGB)
    },
    {
        # Ejemplo de insertar texto sin rectangulo
        "pagina": 0, # numero de pagina a editar
        "texto": "31552665", # Texto a introducir
        "font_name": "hebo", # nombre de la fuente
        "font_size": 11, # Tamano de la fuente
        "color_text" : (0, 0, 0), # Color del texto (RGB)
        "x": 315, # posicion inical en X
        "y": 77, # posicion inical en Y
    },

    #FECHA DE ELABORACION
    # Numero 1 del Dia 
    {
        "pagina": 0, # numero de pagina a editar
        "texto": "0", # Texto a introducir
        "font_name": "hebo", # nombre de la fuente
        "font_size": 5, # Tamano de la fuente
        "color_text" : (0, 0, 0), # Color del texto (RGB)
        "x": 272.85, # posicion inical en X
        "y": 561.50, # posicion inical en Y
    },

    # Numero 2 del Dia 
    {
        "pagina": 0, # numero de pagina a editar
        "texto": "0", # Texto a introducir
        "font_name": "hebo", # nombre de la fuente
        "font_size": 5, # Tamano de la fuente
        "color_text" : (0, 0, 0), # Color del texto (RGB)
        "x": 286.60, # posicion inical en X
        "y": 561.50, # posicion inical en Y
    },

    # Numero 1 del Mes 
    {
        "pagina": 0, # numero de pagina a editar
        "texto": "0", # Texto a introducir
        "font_name": "hebo", # nombre de la fuente
        "font_size": 5, # Tamano de la fuente
        "color_text" : (0, 0, 0), # Color del texto (RGB)
        "x": 300.40, # posicion inical en X
        "y": 561.50, # posicion inical en Y
    },

   # Numero 2 del Mes 
    {
        "pagina": 0, # numero de pagina a editar
        "texto": "0", # Texto a introducir
        "font_name": "hebo", # nombre de la fuente
        "font_size": 5, # Tamano de la fuente
        "color_text" : (0, 0, 0), # Color del texto (RGB)
        "x": 314.00, # posicion inical en X
        "y": 561.50, # posicion inical en Y
    },

    # Numero 1 del Año 
    {
        "pagina": 0, # numero de pagina a editar
        "texto": "0", # Texto a introducir
        "font_name": "hebo", # nombre de la fuente
        "font_size": 5, # Tamano de la fuente
        "color_text" : (0, 0, 0), # Color del texto (RGB)
        "x": 328.00, # posicion inical en X
        "y": 561.50, # posicion inical en Y
    },

    # Numero 2 del Año 
    {
        "pagina": 0, # numero de pagina a editar
        "texto": "0", # Texto a introducir
        "font_name": "hebo", # nombre de la fuente
        "font_size": 5, # Tamano de la fuente
        "color_text" : (0, 0, 0), # Color del texto (RGB)
        "x": 341.70, # posicion inical en X
        "y": 561.50, # posicion inical en Y
    },

    # Numero 3 del Año 
    {
        "pagina": 0, # numero de pagina a editar
        "texto": "0", # Texto a introducir
        "font_name": "hebo", # nombre de la fuente
        "font_size": 5, # Tamano de la fuente
        "color_text" : (0, 0, 0), # Color del texto (RGB)
        "x": 355.50, # posicion inical en X
        "y": 561.50, # posicion inical en Y
    },

    # Numero 4 del Año 
    {
        "pagina": 0, # numero de pagina a editar
        "texto": "0", # Texto a introducir
        "font_name": "hebo", # nombre de la fuente
        "font_size": 5, # Tamano de la fuente
        "color_text" : (0, 0, 0), # Color del texto (RGB)
        "x": 369.30, # posicion inical en X
        "y": 561.50, # posicion inical en Y
    },
]

insertar_varios_textos(
    input_pdf="static/Template_Factura_Vertical_SVG.pdf", 
    output_pdf="new_document/documento_con_texto.pdf",
    textos=textos
)