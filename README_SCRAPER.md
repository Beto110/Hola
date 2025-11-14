# 🕷️ Web Scraper Avanzado

Web scraper robusto con Selenium y BeautifulSoup para extraer datos de sitios web de e-commerce.

## 📋 Características

- ✅ Anti-detección con User-Agent rotativo
- ✅ Scroll automático simulando comportamiento humano
- ✅ Múltiples estrategias de extracción de datos
- ✅ Exportación a Excel y CSV
- ✅ Capturas de pantalla para debugging
- ✅ Compatible con modo headless (sin interfaz gráfica)
- ✅ Manejo de CAPTCHAs y bloqueos

## 🚀 Instalación

### 1. Instalar dependencias de Python

```bash
pip install -r requirements.txt
```

### 2. Instalar Chrome/Chromium (Linux)

**Amazon Linux 2023 / Fedora:**
```bash
sudo dnf install chromium
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install chromium-browser
```

### 3. Instalar ChromeDriver (opcional - webdriver-manager lo hace automático)

```bash
pip install webdriver-manager
```

## 📖 Uso

### Versión Básica (web_scraper.py)

Usa Microsoft Edge (Windows):

```python
# Editar configuración en el archivo
url = "https://www.ebay.com/sch/i.html?_nkw=laptop"
selectores_items = ["li.s-item", ".s-item"]

# Ejecutar
python web_scraper.py
```

### Versión Mejorada (web_scraper_improved.py)

Usa Chrome/Chromium (multiplataforma):

```python
# Editar configuración en el archivo
url = "https://books.toscrape.com/"
selectores_items = ["article.product_pod", ".product_pod"]
modo_headless = True  # False para ver el navegador

# Ejecutar
python web_scraper_improved.py
```

## 🎯 Ejemplos de Configuración

### Amazon
```python
url = "https://www.amazon.com/s?k=laptop"
selectores_items = [
    "div[data-component-type='s-search-result']",
    ".s-result-item",
    "div.sg-col-inner"
]
```

### eBay
```python
url = "https://www.ebay.com/sch/i.html?_nkw=laptop"
selectores_items = ["li.s-item", ".s-item"]
```

### Shein
```python
url = "https://www.shein.com/search?q=dress"
selectores_items = [".product-card", ".S-product-item", "article"]
```

### Sitio de Prueba (Books to Scrape)
```python
url = "https://books.toscrape.com/"
selectores_items = ["article.product_pod", ".product_pod"]
```

## 📂 Archivos Generados

- `productos_extraidos.xlsx` - Datos en formato Excel
- `productos_extraidos.csv` - Datos en formato CSV (fallback)
- `page_full.html` - HTML completo de la página
- `captura_inicial.png` - Screenshot al cargar la página
- `captura_final.png` - Screenshot después del scroll

## 🔧 Solución de Problemas

### Error: "ChromeDriver not found"

**Solución 1 - Usar webdriver-manager:**
```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
```

**Solución 2 - Instalar manualmente:**
```bash
# Descargar de: https://chromedriver.chromium.org/
# Mover a /usr/local/bin/
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
```

### Error: "No se encontraron productos"

1. Abre `page_full.html` en un navegador
2. Click derecho en un producto → Inspeccionar
3. Encuentra la clase CSS del contenedor
4. Actualiza `selectores_items` en el código

### Error: CAPTCHA detectado

- Usa VPN o Proxy
- Reduce la frecuencia de requests
- Usa cookies de sesión válidas
- Considera usar APIs oficiales

### Error: "Session not created"

Versión de Chrome/ChromeDriver incompatible:
```bash
# Ver versión de Chrome
google-chrome --version
chromium --version

# Instalar ChromeDriver compatible
pip install webdriver-manager
```

## ⚠️ Consideraciones Legales

- ✅ Respeta los `robots.txt` de los sitios
- ✅ No sobrecargues los servidores (usa delays)
- ✅ Revisa los Términos de Servicio
- ✅ Considera usar APIs oficiales cuando estén disponibles
- ❌ No uses para fines maliciosos

## 🛡️ Anti-Detección

El scraper incluye:
- User-Agent rotativo
- Eliminación de propiedades `navigator.webdriver`
- Scroll humano aleatorio
- Delays aleatorios
- Deshabilitación de señales de automatización

## 📊 Estructura de Datos

El DataFrame generado contiene:
- **Producto**: Nombre/título del producto
- **Precio**: Precio extraído (o "No disponible")
- **Enlace**: URL del producto

## 🤝 Contribuciones

Para mejorar el scraper:
1. Añade más selectores para diferentes sitios
2. Mejora las estrategias de extracción
3. Añade soporte para más formatos de exportación
4. Implementa rotación de proxies

## 📝 Notas

- El modo headless es más rápido pero algunos sitios lo detectan
- Algunos sitios requieren JavaScript complejo (usa Selenium)
- Para scraping masivo, considera Scrapy o APIs oficiales
- Las imágenes están deshabilitadas por defecto para velocidad
