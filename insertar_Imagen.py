import fitz  # PyMuPDF

def insertar_imagen_en_pdf(pdf_original, pdf_modificado, ruta_imagen, pagina=0, x=50, y=50, ancho=100, alto=100):
    """
    Inserta una imagen en un PDF existente y guarda el resultado en un nuevo archivo.

    Parámetros:
        pdf_original (str): Ruta del PDF original.
        pdf_modificado (str): Ruta del nuevo PDF con la imagen.
        ruta_imagen (str): Ruta de la imagen a insertar.
        pagina (int): Número de página donde se insertará la imagen (0 = primera página).
        x (int): Posición horizontal inicial (en puntos).
        y (int): Posición vertical inicial (en puntos).
        ancho (int): Ancho de la imagen (en puntos).
        alto (int): Alto de la imagen (en puntos).
    """
    # Abrir el PDF original
    documento = fitz.open(pdf_original)
    
    # Seleccionar la página deseada
    pagina = 0
    pagina_pdf = documento[pagina]

    # Obtener el tamano del documento a editar
    #
   
    
    # Definir la posición y tamaño de la imagen (rectángulo)

    rectangulo = fitz.Rect(x, y, x + ancho, y + alto)
    
    # Insertar la imagen en la página
    pagina_pdf.insert_image(rectangulo, filename=ruta_imagen)
    
    # Guardar el PDF modificado
    documento.save(pdf_modificado)
    documento.close()

# Ejemplo de uso
insertar_imagen_en_pdf(
    pdf_original="static/Factura_Vertical_Template.pdf",
    pdf_modificado="new_document/Factura_Vertical_Logo.pdf",
    ruta_imagen="static/Logo_PNG.png",
    pagina=0,
    x=47,
    y=47,
    ancho=69,
    alto=86
)