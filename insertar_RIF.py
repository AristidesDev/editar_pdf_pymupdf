import fitz  # PyMuPDF

def insertar_texto_en_pdf(input_pdf, output_pdf, texto, pagina=0, x=50, y=50):
    """
    Inserta texto en un PDF y guarda una copia modificada.
    
    Parámetros:
        input_pdf (str): Ruta del PDF original.
        output_pdf (str): Ruta del nuevo PDF.
        texto (str): Texto a insertar.
        pagina (int): Número de página (0 = primera página).
        x (float): Posición horizontal (puntos).
        y (float): Posición vertical (puntos).
    """
    doc = fitz.open(input_pdf)
    page = doc[pagina]
    
    # Configurar fuente y tamaño
    font_size = 11
    font = fitz.Font("hebo")  # Fuente predeterminada (helvetica)
    
    # Insertar texto
    page.insert_text(
        point=(x, y),  # Posición (x, y) en puntos
        text=texto,
        fontname=font.name,
        fontsize=font_size,
        color=(0, 0, 0)  # Color en RGB (negro)
    )
    
    doc.save(output_pdf)
    doc.close()

# Ejemplo de uso
letra = "J"
num1 = "31552665"
num2 = "0"
rif = f"{letra}-{num1}-{num2}"

insertar_texto_en_pdf(
    input_pdf="static/Template_Factura_Vertical_SVG.pdf",
    output_pdf="new_document/documento_con_texto.pdf",
    texto=rif,
    pagina=0,
    x=315,
    y=77  # En un docuemnto de (614 pt de alto), 100 está cerca de la parte superior
)