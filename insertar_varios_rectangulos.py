import fitz  # PyMuPDF

def insertar_varios_rectangulos_con_texto(
    input_pdf,
    output_pdf,
    config_rectangulos  # Lista de diccionarios con configuraciones
):
    """
    Inserta múltiples rectángulos con texto en un PDF.
    
    Parámetros:
        config_rectangulos (list): Lista de diccionarios con:
            {
                "pagina": 0,                # Página (0 = primera)
                "texto": "Texto aquí",      # Texto a insertar
                "rect_x": 123.7,            # Coordenada X
                "rect_y": 38.10,            # Coordenada Y
                "rect_width": 154,          # Ancho del rectángulo
                "rect_height": 73.7,        # Alto del rectángulo
                "color_rect": (0.25, 0.75, 0.75),  # Color del rectángulo
                "color_texto": (0, 0, 0),   # Color del texto
                "font_size": 7,             # Tamaño de fuente
                "font_name": "helv",        # Fuente
                "padding": 0,               # Espacio interno
                "align": 1                  # Alineación (0=izq,1=centro,2=der)
            }
    """
    doc = fitz.open(input_pdf)
    
    for config in config_rectangulos:
        pagina = doc[config["pagina"]]
        
        # Dibujar el rectángulo
        rect = fitz.Rect(
            config["rect_x"],
            config["rect_y"],
            config["rect_x"] + config["rect_width"],
            config["rect_y"] + config["rect_height"]
        )
        
        pagina.draw_rect(
            rect,
            color=config.get("color_rect", (0.25, 0.75, 0.75)),
            fill=config.get("color_rect", (0.25, 0.75, 0.75)),
            width=1.5  # Grosor del borde
        )
        
        # Área de texto con padding
        padding = config.get("padding", 0)
        text_rect = fitz.Rect(
            rect.x0 + padding,
            rect.y0 + padding,
            rect.x1 - padding,
            rect.y1 - padding
        )
        
        # Insertar texto
        pagina.insert_textbox(
            text_rect,
            config["texto"],
            fontname=config.get("font_name", "helv"),
            fontsize=config.get("font_size", 7),
            color=config.get("color_texto", (0, 0, 0)),
            align=config.get("align", 1)
        )
    
    doc.save(output_pdf)
    doc.close()

# Ejemplo de uso con múltiples rectángulos
configuraciones = [
    # LOGO DE LA EMPRESA
    {
        "pagina": 0,
        "texto": "LOGO DE LA EMPRESA",
        "rect_x": 47.5,
        "rect_y": 38.5,  # Ajusta la posición Y
        "rect_width": 73.5,
        "rect_height": 73.5,
        "color_rect": (0.8, 0.8, 0.8),  # Gris claro
        "font_size": 8,
        "align": 0
    },

    # NOMBRE DE LA EMPRESA
    {
        "pagina": 0,
        "texto": "NOMBRE DE LA EMPRESA",
        "rect_x": 123.7,
        "rect_y": 38.5,
        "rect_width": 153,
        "rect_height": 26,
        "color_rect": (0.55, 0.55, 0.55),  # Turquesa
        "color_texto": (0, 0, 0),
        "font_size": 7,
        "align": 1
    },

    # DIRECION DE LA EMPRESA
    {
        "pagina": 0,
        "texto": "DIRECCION DE LA EMPRESA",
        "rect_x": 123.7,
        "rect_y": 64.5,
        "rect_width": 153,
        "rect_height": 22,
        "color_rect": (0.25, 0.75, 0.75),  # Turquesa
        "color_texto": (0, 0, 0),
        "font_size": 7,
        "align": 1
    },
    
    # TELEFONO DE LA EMPRESA
    {
        "pagina": 0,
        "texto": "TEL 0412 - 555 5555",
        "rect_x": 123.7,
        "rect_y": 86,
        "rect_width": 153,
        "rect_height": 13,
        "color_rect": (0.3, 0.3, 0.3),  # Turquesa
        "color_texto": (0, 0, 0),
        "font_size": 7,
        "align": 1
    },
        # DIRECION DE LA EMPRESA
    {
        "pagina": 0,
        "texto": "DIRECCION DE LA EMPRESA",
        "rect_x": 123.7,
        "rect_y": 99,
        "rect_width": 153,
        "rect_height": 13,
        "color_rect": (0.75, 0.75, 0.75),  # Turquesa
        "color_texto": (0, 0, 0),
        "font_size": 7,
        "align": 1
    },
]

insertar_varios_rectangulos_con_texto(
    input_pdf="static/Template_Factura_Vertical_SVG.pdf",
    output_pdf="new_document/documento_con_texto.pdf",
    config_rectangulos=configuraciones
)