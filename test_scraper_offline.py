"""
Test del scraper sin necesidad de Chrome
Usa HTML de ejemplo para probar la lógica de extracción
"""

from bs4 import BeautifulSoup
import pandas as pd
import os

# HTML de ejemplo (Books to Scrape)
SAMPLE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Books to Scrape</title>
</head>
<body>
    <div class="container">
        <article class="product_pod">
            <h3><a href="/book1.html">A Light in the Attic</a></h3>
            <div class="product_price">
                <p class="price_color">£51.77</p>
            </div>
        </article>
        
        <article class="product_pod">
            <h3><a href="/book2.html">Tipping the Velvet</a></h3>
            <div class="product_price">
                <p class="price_color">£53.74</p>
            </div>
        </article>
        
        <article class="product_pod">
            <h3><a href="/book3.html">Soumission</a></h3>
            <div class="product_price">
                <p class="price_color">£50.10</p>
            </div>
        </article>
        
        <article class="product_pod">
            <h3><a href="/book4.html">Sharp Objects</a></h3>
            <div class="product_price">
                <p class="price_color">£47.82</p>
            </div>
        </article>
        
        <article class="product_pod">
            <h3><a href="/book5.html">Sapiens: A Brief History of Humankind</a></h3>
            <div class="product_price">
                <p class="price_color">£54.23</p>
            </div>
        </article>
    </div>
</body>
</html>
"""

def extraer_datos(html_content, selector_items):
    """Extrae productos, precios y links del HTML"""
    soup = BeautifulSoup(html_content, "html.parser")
    
    productos, precios, links = [], [], []
    
    # Buscar items
    items = soup.select(selector_items)
    
    print(f"📦 Total de elementos encontrados: {len(items)}\n")
    
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
        
        # Debug
        if idx < 5:
            print(f"--- Item {idx + 1} ---")
            if titulo:
                print(f"  Título: {titulo.get_text(strip=True)}")
            if precio:
                print(f"  Precio: {precio.get_text(strip=True)}")
            if link:
                print(f"  Link: {link.get('href')}")
            print()
        
        # Guardar datos
        if titulo:
            titulo_texto = titulo.get_text(strip=True)
            if len(titulo_texto) > 5:
                productos.append(titulo_texto)
                precios.append(precio.get_text(strip=True) if precio else "No disponible")
                
                if link:
                    href = link.get("href", "")
                    links.append(href)
                else:
                    links.append("No disponible")
    
    return productos, precios, links

def main():
    print("🧪 Test del Scraper (Modo Offline)\n")
    print("="*60)
    
    # Guardar HTML de ejemplo
    with open("test_page.html", "w", encoding="utf-8") as f:
        f.write(SAMPLE_HTML)
    print("💾 HTML de prueba guardado en 'test_page.html'\n")
    
    # Probar extracción
    selector = "article.product_pod"
    print(f"🔍 Usando selector: {selector}\n")
    
    productos, precios, links = extraer_datos(SAMPLE_HTML, selector)
    
    # Mostrar resultados
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
        
        print("📊 RESULTADOS:")
        print(df.to_string(index=False))
        print()
        
        # Guardar a Excel
        try:
            ruta_excel = os.path.join(os.getcwd(), "test_productos.xlsx")
            df.to_excel(ruta_excel, index=False, engine='openpyxl')
            print(f"📂 Excel guardado: {ruta_excel}")
        except Exception as e:
            print(f"⚠️  Error al guardar Excel: {e}")
            ruta_csv = os.path.join(os.getcwd(), "test_productos.csv")
            df.to_csv(ruta_csv, index=False, encoding='utf-8-sig')
            print(f"📂 CSV guardado: {ruta_csv}")
    
    print("\n" + "="*60)
    print("🎉 TEST COMPLETADO")
    print("="*60)
    print("\n💡 Este test demuestra que la lógica de extracción funciona.")
    print("   Para scraping real, necesitas Chrome/Chromium instalado.")

if __name__ == "__main__":
    main()
