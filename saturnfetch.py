import psutil
import os
from datetime import datetime

def obtener_info_sistema():
    """Obtiene la información del sistema: batería, RAM y memoria"""
    try:
        # Porcentaje de batería
        try:
            bateria = psutil.sensors_battery()
            porcentaje_bateria = f"{bateria.percent:.1f}%" if bateria else "N/A"
        except:
            porcentaje_bateria = "N/A"
        
        # Porcentaje de RAM usada
        memoria_ram = psutil.virtual_memory()
        porcentaje_ram = f"{memoria_ram.percent:.1f}%"
        
        # Porcentaje de memoria del disco
        disco = psutil.disk_usage('/')
        porcentaje_disco = f"{disco.percent:.1f}%"
        
        return porcentaje_bateria, porcentaje_ram, porcentaje_disco
        
    except Exception as e:
        return "Error", "Error", "Error"

def mostrar_archivo_con_info(archivo_path):
    """Muestra el archivo con la información del sistema abajo a la derecha"""
    try:
        # Verificar si el archivo existe
        if not os.path.exists(archivo_path):
            print(f"Error: El archivo '{archivo_path}' no existe.")
            return
        
        # Obtener información del sistema
        bateria, ram, disco = obtener_info_sistema()
        
        # Leer el contenido del archivo
        with open(archivo_path, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        
        # Encabezado con información del sistema
        print("=" * 80)
        print(f"ARCHIVO: {os.path.basename(archivo_path)}")
        print(f"FECHA: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
        print()
        
        # Calcular el ancho máximo de las líneas del archivo
        ancho_maximo = max(len(linea.rstrip()) for linea in lineas) if lineas else 0
        
        # Información del sistema en formato de lista
        info_sistema = [
            "╔═══════════════════════╗",
            "║   SISTEMA INFO        ║",
            "╠═══════════════════════╣",
            f"║ 🔋 Batería: {bateria:<8}  ║",
            f"║ 🎯 RAM: {ram:<11}   ║",
            f"║ 💾 Disco: {disco:<11} ║",
            "╚═══════════════════════╝"
        ]
        
        # Determinar cuántas líneas de espacio necesitamos
        lineas_archivo = len(lineas)
        lineas_info = len(info_sistema)
        
        # Mostrar todas las líneas del archivo
        for i, linea in enumerate(lineas):
            linea_limpia = linea.rstrip()
            
            # Si estamos en las últimas líneas donde va la información
            if i >= lineas_archivo - lineas_info:
                # Calcular el índice correspondiente en la información del sistema
                info_index = i - (lineas_archivo - lineas_info)
                if info_index >= 0 and info_index < lineas_info:
                    print(f"{linea_limpia:<{ancho_maximo}}  {info_sistema[info_index]}")
                else:
                    print(linea_limpia)
            else:
                print(linea_limpia)
                
        # Si el archivo tiene menos líneas que la información del sistema
        if lineas_archivo < lineas_info:
            for i in range(lineas_archivo, lineas_info):
                espacios = " " * ancho_maximo
                print(f"{espacios}  {info_sistema[i]}")
                
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

# Verificar e instalar psutil si es necesario
try:
    import psutil
except ImportError:
    print("La librería 'psutil' no está instalada.")
    respuesta = input("¿Deseas instalarla ahora? (s/n): ")
    if respuesta.lower() == 's':
        print("Instalando psutil...")
        os.system("pip install psutil --break-system-packages")
        print("Por favor, ejecuta el script nuevamente.")
    exit()

# Ejemplo de uso
if __name__ == "__main__":
    # Cambia esta ruta por la de tu archivo .txt
    archivo_txt = "/home/nicolas/saturno.txt"
    
    # Crear un archivo de ejemplo si no existe
    if not os.path.exists(archivo_txt):
        with open(archivo_txt, 'w') as f:
            f.write("Línea 1: Contenido del archivo de ejemplo\n")
            f.write("Línea 2: Información importante sobre el tema\n")
            f.write("Línea 3: Más detalles y especificaciones\n")
            f.write("Línea 4: Características adicionales\n")
            f.write("Línea 5: Última línea del archivo\n")
            f.write("Línea 6: Otra línea de contenido\n")
            f.write("Línea 7: Más información relevante\n")
            f.write("Línea 8: Finalizando el contenido\n")
    
    # Mostrar el archivo con la información del sistema
    mostrar_archivo_con_info(archivo_txt)