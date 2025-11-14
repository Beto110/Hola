"""
Web Scraper Avanzado - Versión con WebDriver Manager
Gestión automática de ChromeDriver
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import random
import sys

# ----------------- CONFIGURACIÓN -----------------
print("🔧 Iniciando Web Scraper Avanzado (Auto)...\n")

# ===== PERSONALIZA AQUÍ =====
url = "https://books.toscrape.com/"
selectores_items = ["article.product_pod", ".product_pod"]

nombre_archivo = "productos_extraidos"
tiempo_espera_inicial = 10
tiempo_scroll = 2
modo_headless = True
# ==========================

def configurar_driver(headless=True):
    """Configura el driver de Chrome con opciones anti-detección"""
    chrome_options = Options()
    
    if headless:
        chrome_options.add_argument('--headless=new')
    
    # Opciones esenciales
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--window-size=1920,1080')
    
    # User-Agent
    user_agents = [
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    ]
    chrome_options.add_argument(f'user-agent={random.choice(user_agents)}')
    
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
    }
    chrome_options.add_experimental_option("prefs", prefs)
    
    return chrome_options

def main():
    if not url:
        print("❌ ERROR: Debes configurar la variable 'url' antes de ejecutar")
        sys.exit(1)
    
    driver = None
    try:
        # Configurar driver con WebDriver Manager
        print("📥 Descargando/verificando ChromeDriver...")
        chrome_options = configurar_driver(headless=modo_headless)
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Anti-detección
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                });
            """
        })
        
        driver.set_page_load_timeout(45)
        print(f"🌐 Accediendo a: {url}\n")
        driver.get(url)
        
        # Espera inicial
        print(f"⏳ Esperando {tiempo_espera_inicial} segundos...")
        time.sleep(tiempo_espera_inicial)
        
        print(f"📄 Título: {driver.title}")
        print(f"🔗 URL: {driver.current_url}\n")
        
        # Scroll
        print("📜 Simulando scroll...")
        total_height = driver.execute_script("return document.body.scrollHeight")
        current_position = 0
        
        while current_position < total_height:
            scroll_amount = random.randint(300, 600)
            current_position += scroll_amount
            driver.execute_script(f"window.scrollTo(0, {current_position});")
            time.sleep(random.uniform(1.5, tiempo_scroll))
            total_height = driver.execute_script("return document.body.scrollHeight")
            if current_position > 3000:
                break
        
        print("✅ Scroll completado\n")
        time.sleep(5)
        
        # Buscar elementos
        print("🔍 Buscando elementos...\n")
        selector_usado = None
        
        for selector in selectores_items:
            try:
                print(f"   Probando: {selector}")
                elements = WebDriverWait(driver, 15).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
                )
                if len(elements) > 0:
                    selector_usado = selector
                    print(f"   ✅ {len(elements)} elementos encontrados\n")
                    break
            except TimeoutException:
                print(f"   ❌ Timeout con '{selector}'")
        
        # Guardar HTML
        html_content = driver.page_source
        with open("page_full.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print("💾 HTML guardado\n")
        
        driver.quit()
        
        # Análisis
        print("🔬 Analizando HTML...\n")
        soup = BeautifulSoup(html_content, "html.parser")
        
        productos, precios, links = [], [], []
        
        if selector_usado:
            items = soup.select(selector_usado)
        else:
            items = soup.find_all("article")
        
        print(f"📦 Total de elementos: {len(items)}\n")
        
        for idx, item in enumerate(items):
            # Títulos
            titulo = None
            for tag in ['h2', 'h3', 'h4', 'a']:
                titulo = item.find(tag)
                if titulo and len(titulo.get_text(strip=True)) > 5:
                    break
            
            # Precios
            precio = None
            for tag in ['span', 'div', 'p']:
                precio = item.find(tag, class_=lambda x: x and 'price' in x.lower() if x else False)
                if precio:
                    break
            
            # Links
            link = item.find('a', href=True)
            
            if idx < 3:
                print(f"--- Item {idx + 1} ---")
                if titulo:
                    print(f"  → {titulo.get_text(strip=True)[:60]}")
                if precio:
                    print(f"  💰 {precio.get_text(strip=True)[:30]}")
                print()
            
            if titulo:
                titulo_texto = titulo.get_text(strip=True)
                if len(titulo_texto) > 5:
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
        
        # Guardar resultados
        print("="*60)
        if not productos:
            print("\n❌ NO SE ENCONTRARON PRODUCTOS\n")
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
            
            try:
                ruta_excel = os.path.join(os.getcwd(), f"{nombre_archivo}.xlsx")
                df.to_excel(ruta_excel, index=False, engine='openpyxl')
                print(f"📂 Excel: {ruta_excel}")
            except:
                ruta_csv = os.path.join(os.getcwd(), f"{nombre_archivo}.csv")
                df.to_csv(ruta_csv, index=False, encoding='utf-8-sig')
                print(f"📂 CSV: {ruta_csv}")
        
        print("\n" + "="*60)
        print("🎉 PROCESO FINALIZADO")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass

if __name__ == "__main__":
    main()
