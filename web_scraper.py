from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import random

# ----------------- CONFIGURACIÓN -----------------
print("🔧 Iniciando Web Scraper Avanzado...\n")

# ===== PERSONALIZA AQUÍ =====
# Para Amazon:
# url = "https://www.amazon.com/s?k=laptop"
# selectores_items = ["div[data-component-type='s-search-result']", ".s-result-item", "div.sg-col-inner"]

# Para Shein:
# url = "https://www.shein.com/search?q=dress"
# selectores_items = [".product-card", ".S-product-item", "article"]

# Para eBay (ejemplo):
url = ""
selectores_items = ["li.s-item", ".s-item"]

nombre_archivo = "productos_extraidos"
tiempo_espera_inicial = 15  # Aumentar para sitios lentos
tiempo_scroll = 2  # Tiempo entre scrolls
# ==========================

# Configurar opciones de Edge (ANTI-DETECCIÓN)
edge_options = Options()
edge_options.add_argument('--disable-blink-features=AutomationControlled')
edge_options.add_argument('--disable-dev-shm-usage')
edge_options.add_argument('--no-sandbox')
edge_options.add_argument('--start-maximized')
edge_options.add_argument('--disable-infobars')
edge_options.add_argument('--disable-notifications')

# User-Agent realista y actualizado
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
]
edge_options.add_argument(f'user-agent={random.choice(user_agents)}')

# Ocultar señales de automatización
edge_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
edge_options.add_experimental_option('useAutomationExtension', False)

# Preferencias adicionales
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.default_content_setting_values.notifications": 2
}
edge_options.add_experimental_option("prefs", prefs)

# Inicializar driver
driver = None
try:
    service = Service()
    driver = webdriver.Edge(service=service, options=edge_options)
    
    # Eliminar propiedades de webdriver
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en']
            });
        """
    })
    
    driver.set_page_load_timeout(45)
    print(f"🌐 Accediendo a: {url}\n")
    driver.get(url)
    
except Exception as e:
    print(f"❌ Error al iniciar el navegador: {e}")
    if driver:
        driver.quit()
    exit()

# Espera inicial LARGA para JavaScript
print(f"⏳ Esperando {tiempo_espera_inicial} segundos para renderizado JavaScript...")
time.sleep(tiempo_espera_inicial)

print(f"📄 Título: {driver.title}")
print(f"🔗 URL: {driver.current_url}\n")

# Detectar si hay CAPTCHA o bloqueo
if "captcha" in driver.current_url.lower() or "robot" in driver.page_source.lower()[:500]:
    print("🚨 ALERTA: Posible CAPTCHA o bloqueo detectado")
    print("   Resuelve manualmente en la ventana y presiona ENTER aquí...")
    input()

# Captura inicial
try:
    driver.save_screenshot("captura_inicial.png")
    print("📸 Captura inicial guardada\n")
except:
    pass

# Scroll REALISTA (imitar comportamiento humano)
print("📜 Simulando scroll humano...")
total_height = driver.execute_script("return document.body.scrollHeight")
viewport_height = driver.execute_script("return window.innerHeight")
current_position = 0

while current_position < total_height:
    # Scroll aleatorio (no uniforme)
    scroll_amount = random.randint(300, 600)
    current_position += scroll_amount
    
    driver.execute_script(f"window.scrollTo(0, {current_position});")
    
    # Espera aleatoria (humano)
    time.sleep(random.uniform(1.5, tiempo_scroll))
    
    # Recalcular altura (contenido dinámico)
    total_height = driver.execute_script("return document.body.scrollHeight")
    
    if current_position > 3000:  # Limitar scroll
        break

print("✅ Scroll completado\n")

# Espera adicional después del scroll
time.sleep(5)

# Intentar encontrar elementos
print("🔍 Buscando elementos en la página...\n")
items_selenium = []
selector_usado = None

for selector in selectores_items:
    try:
        print(f"   Probando: {selector}")
        elements = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
        )
        if len(elements) > 0:
            items_selenium = elements
            selector_usado = selector
            print(f"   ✅ {len(elements)} elementos encontrados\n")
            break
    except TimeoutException:
        print(f"   ❌ Timeout con '{selector}'")
    except Exception as e:
        print(f"   ❌ Error: {str(e)[:50]}")

# Guardar HTML
html_content = driver.page_source
with open("page_full.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("💾 HTML guardado en 'page_full.html'\n")

# Captura final
try:
    driver.save_screenshot("captura_final.png")
    print("📸 Captura final guardada\n")
except:
    pass

driver.quit()

# ----------------- ANÁLISIS -----------------
print("🔬 Analizando HTML...\n")
soup = BeautifulSoup(html_content, "html.parser")

productos, precios, links = [], [], []

# Usar selector que funcionó
if selector_usado:
    items = soup.select(selector_usado)
else:
    # Fallback: buscar por atributos comunes
    items = soup.find_all(attrs={"data-component-type": True})
    if not items:
        items = soup.find_all("article")
    if not items:
        items = soup.find_all("li", class_=lambda x: x and any(k in x.lower() for k in ["item", "product", "result"]) if x else False)

print(f"📦 Total de elementos: {len(items)}\n")

# Extraer datos (flexible)
for idx, item in enumerate(items):
    # Títulos (múltiples estrategias)
    titulo = None
    for tag in ['h2', 'h3', 'h4', 'span', 'div', 'a']:
        titulo = item.find(tag, class_=lambda x: x and any(k in x.lower() for k in ['title', 'name', 'product']) if x else False)
        if titulo and len(titulo.get_text(strip=True)) > 5:
            break
    
    # Si no encuentra por clase, buscar por posición
    if not titulo:
        titulo = item.find('h2') or item.find('h3') or item.find('a')
    
    # Precios
    precio = None
    for tag in ['span', 'div', 'p']:
        precio = item.find(tag, class_=lambda x: x and any(k in x.lower() for k in ['price', 'cost', 'amount']) if x else False)
        if precio:
            break
    
    # Links
    link = item.find('a', href=True)
    
    # Debug primeros 3
    if idx < 3:
        print(f"--- Item {idx + 1} ---")
        print(f"Título: {titulo is not None}")
        print(f"Precio: {precio is not None}")
        if titulo:
            print(f"  → {titulo.get_text(strip=True)[:60]}")
        if precio:
            print(f"  💰 {precio.get_text(strip=True)[:30]}")
        print()
    
    # Guardar datos
    if titulo:
        titulo_texto = titulo.get_text(strip=True)
        
        # Filtros
        if len(titulo_texto) > 5 and not any(x in titulo_texto.lower() for x in ['shop on', 'sponsored', 'ad']):
            productos.append(titulo_texto)
            precios.append(precio.get_text(strip=True) if precio else "No disponible")
            
            if link:
                href = link.get("href", "")
                if href.startswith("/"):
                    from urllib.parse import urljoin
                    href = urljoin(url, href)
                links.append(href)
            else:
                links.append("No disponible")

# ----------------- GUARDAR -----------------
print("="*60)
if not productos:
    print("\n❌ NO SE ENCONTRARON PRODUCTOS\n")
    print("🔍 PASOS PARA RESOLVER:")
    print("   1. Abre 'page_full.html' y busca un producto")
    print("   2. Click derecho → Inspeccionar")
    print("   3. Encuentra la clase CSS del contenedor del producto")
    print("   4. Actualiza 'selectores_items' en el código")
    print("\n💡 Para Amazon/Shein puede necesitar:")
    print("   - VPN o Proxy")
    print("   - Cookies de sesión válidas")
    print("   - Resolver CAPTCHAs manualmente")
    print("   - Usar sus APIs oficiales")
else:
    print(f"\n✅ {len(productos)} PRODUCTOS EXTRAÍDOS\n")
    
    df = pd.DataFrame({
        "Producto": productos,
        "Precio": precios,
        "Enlace": links
    })
    
    print("📊 PRIMEROS 5 RESULTADOS:")
    print(df.head(5).to_string(index=False))
    print()
    
    ruta_excel = os.path.join(os.getcwd(), f"{nombre_archivo}.xlsx")
    try:
        df.to_excel(ruta_excel, index=False, engine='openpyxl')
        print(f"📂 Excel: {ruta_excel}")
    except:
        ruta_csv = os.path.join(os.getcwd(), f"{nombre_archivo}.csv")
        df.to_csv(ruta_csv, index=False, encoding='utf-8-sig')
        print(f"📂 CSV: {ruta_csv}")

print("\n" + "="*60)
print("🎉 PROCESO FINALIZADO")
print("="*60)
