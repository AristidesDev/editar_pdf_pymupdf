import fitz  # PyMuPDF

def insertar_rectangulo_con_texto(
    input_pdf,
    output_pdf,
    texto,
    rect_x,
    rect_y,
    rect_width,
    rect_height,
    pagina=0,
    color_rect=(0.25, 0.75, 0.75),  # Color del rectángulo (RGB)
    color_texto=(0, 0, 0),        # Color del texto (RGB)
    font_size=14,
    font_name="helv",
    padding=0,                   # Espacio entre el borde y el texto
    align=1                       # 0=izquierda, 1=centro, 2=derecha
):
    """
    Inserta un rectángulo con texto dentro en un PDF.
    
    Parámetros:
        rect_x, rect_y: Coordenadas de la esquina superior izquierda del rectángulo.
        rect_width, rect_height: Ancho y alto del rectángulo.
        padding: Espacio entre el texto y los bordes del rectángulo.
    """
    doc = fitz.open(input_pdf)
    page = doc[pagina]
    
    # Dibujar el rectángulo
    rect = fitz.Rect(rect_x, rect_y, rect_x + rect_width, rect_y + rect_height)
    page.draw_rect(
        rect,
        color=color_rect,  # Color de relleno (opcional)
        fill=color_rect,   # Relleno del rectángulo (mismo color)
        # width=1.5,         # Grosor del borde
    )
    
    # Ajustar el área de texto dentro del rectángulo (con padding)
    text_rect = fitz.Rect(
        rect_x + padding,
        rect_y + padding,
        rect_x + rect_width - padding,
        rect_y + rect_height - padding
    )
    
    # Insertar texto dentro del área ajustada
    page.insert_textbox(
        text_rect,
        texto,
        fontname=font_name,
        fontsize=font_size,
        color=color_texto,
        align=align
    )
    
    doc.save(output_pdf)
    doc.close()

# Ejemplo de uso
insertar_rectangulo_con_texto(
    input_pdf="static/Template_Factura_Vertical_SVG.pdf",
    output_pdf="new_document/documento_con_texto.pdf",
    texto="J-15265067-0",
    rect_x=305.5,          # Posición X del rectángulo
    rect_y=67.6,         # Posición Y del rectángulo
    rect_width=107,     # Ancho del rectángulo
    rect_height=12,     # Alto del rectángulo
    color_rect=(1, 1, 1),  # Blanco
    color_texto=(0, 0, 0),     # Negro
    font_size=7,
    align=1            # Texto centrado
)