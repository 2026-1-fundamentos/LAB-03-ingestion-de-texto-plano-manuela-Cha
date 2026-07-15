"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    import re
    
    # Leer el archivo
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Dividir por clusters (separados por "Cluster X")
    # Usar regex para extraer cada cluster
    pattern = r"(\d+)\s+(\d+)\s+([\d,]+\s*%)\s+(.+?)(?=\n\s*\d+\s+\d+|$)"
    matches = re.findall(pattern, content, re.DOTALL)
    
    data = []
    for match in matches:
        cluster_num = int(match[0])
        cantidad = int(match[1])
        porcentaje_str = match[2].replace(" %", "").replace(",", ".")
        porcentaje = float(porcentaje_str)
        
        # Procesar las palabras clave: eliminar espacios múltiples y punto final
        keywords = match[3].strip()
        # Reemplazar múltiples espacios con un solo espacio
        keywords = re.sub(r"\s+", " ", keywords)
        # Eliminar el punto final si existe
        keywords = keywords.rstrip(".")
        # Normalizar separadores: cambiar espacios seguidos de coma a solo coma + espacio
        keywords = re.sub(r"\s*,\s*", ", ", keywords)
        
        data.append({
            "cluster": cluster_num,
            "cantidad_de_palabras_clave": cantidad,
            "porcentaje_de_palabras_clave": float(porcentaje_str),
            "principales_palabras_clave": keywords
        })
    
    df = pd.DataFrame(data)
    return df
