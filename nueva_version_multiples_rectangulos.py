import fitz  # PyMuPDF

def insertar_varios_rectangulos_con_texto(input_pdf, output_pdf, config_rectangulos):
    doc = fitz.open(input_pdf)
    
    for config in config_rectangulos:
        pagina = doc[config["pagina"]]
        
        # Crear rectángulo
        rect = fitz.Rect(
            config["rect_x"],
            config["rect_y"],
            config["rect_x"] + config["rect_width"],
            config["rect_y"] + config["rect_height"]
        )
        
        # Dibujar fondo del rectángulo
        pagina.draw_rect(
            rect,
            fill=config.get("color_rect", (0.8, 0.8, 0.8)),
            color=config.get("color_rect", (0.8, 0.8, 0.8)),
        )
        
        # Configuración de texto
        texto = config["texto"]
        font_size = config.get("font_size", 7)
        font_name = config.get("font_name", "helv")
        color_texto = config.get("color_texto", (0, 0, 0))
        align = config.get("align", 1)  # 0=izq, 1=centro, 2=der
        padding = 2  # Espacio mínimo entre texto y borde

        # ----- Corrección clave aquí -----
        # Crear un objeto Font para calcular el ancho del texto
        font = fitz.Font(fontname=font_name)
        text_width = font.text_length(texto, fontsize=font_size)
        # --------------------------------

        # Calcular posición horizontal
        if align == 1:  # Centrado
            x = rect.x0 + (rect.width - text_width) / 2
        elif align == 2:  # Derecha
            x = rect.x1 - text_width - padding
        else:  # Izquierda
            x = rect.x0 + padding

        # Calcular posición vertical
        y = rect.y0 + (rect.height - font_size) / 2 + font_size * 0.8

        # Insertar texto
        pagina.insert_text(
            point=(x, y),
            text=texto,
            fontname=font_name,
            fontsize=font_size,
            color=color_texto
        )
    
    doc.save(output_pdf)
    doc.close()

# Ejemplo de uso
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
    
    # CORREO DE LA EMPRESA
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
        "align": 0
    },
]

insertar_varios_rectangulos_con_texto(
    input_pdf="static/Template_Factura_Vertical_SVG.pdf",
    output_pdf="new_document/documento_con_texto.pdf",
    config_rectangulos=configuraciones
)