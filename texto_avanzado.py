import fitz

def insertar_texto_avanzado(input_pdf, output_pdf, texto, pagina=0, x=50, y=50, 
                            font_size=12, font_name="helv", color=(0, 0, 0), align=0):
    doc = fitz.open(input_pdf)
    page = doc[pagina]
    
    # Crear rectángulo si se usa alineación
    if align in (0, 1, 2):
        rect = fitz.Rect(x, y, page.rect.width - 50, y + font_size)
        page.insert_textbox(
            rect=rect,
            text=texto,
            fontname=font_name,
            fontsize=font_size,
            align=align,
            color=color
        )
    else:
        page.insert_text(
            point=(x, y),
            text=texto,
            fontname=font_name,
            fontsize=font_size,
            color=color
        )
    
    doc.save(output_pdf)
    doc.close()

# Ejemplo: Texto centrado en la parte superior
insertar_texto_avanzado(
    input_pdf="static/Factura_Vertical_Template.pdf",
    output_pdf="new_document/documento_con_imagen.pdf",
    texto="TITULO CENTRADO",
    pagina=0,
    y=600,  # Cerca del borde superior en un A4
    font_size=24,
    font_name="helv-bo",
    color=(0, 0, 0),
    align=1  # Centrado
)