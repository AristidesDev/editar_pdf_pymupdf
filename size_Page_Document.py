import fitz  # PyMuPDF

def obtener_tamanos_pdf(ruta_pdf):
    # Abrir el documento
    documento = fitz.open(ruta_pdf)
    
    print(f"📄 Documento: {ruta_pdf}")
    print(f"📑 Número de páginas: {len(documento)}")
    
    # Iterar por cada página
    for num_pagina in range(len(documento)):
        pagina = documento[num_pagina]
        ancho = pagina.rect.width  # Ancho en puntos
        alto = pagina.rect.height  # Alto en puntos
        
        print(f"\n📄 Página {num_pagina + 1}:")
        print(f"- Ancho: {ancho:.2f} puntos | {puntos_a_cm(ancho):.2f} cm")
        print(f"- Alto: {alto:.2f} puntos | {puntos_a_cm(alto):.2f} cm")
    
    documento.close()

def puntos_a_cm(puntos):
    # Convertir puntos a centímetros (1 punto = 1/72 pulgadas, 1 pulgada = 2.54 cm)
    return puntos * 2.54 / 72

# ejecucion
ruta_documento = 'static\Factura_Vertical_Template.pdf'
obtener_tamanos_pdf(ruta_documento)