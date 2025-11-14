# 🚀 Quick Start Guide

## ⚡ 5-Minute Setup

### Step 1: Install Chrome (if not installed)
```bash
# Amazon Linux 2023 / Fedora
sudo dnf install chromium -y

# Ubuntu / Debian
sudo apt-get install chromium-browser -y

# macOS
brew install --cask google-chrome
```

### Step 2: Verify Dependencies
```bash
# Already installed in this environment!
pip install -r requirements.txt
```

### Step 3: Configure Your Target
Edit `web_scraper_auto.py`:
```python
# Line 23-24: Set your target URL and selectors
url = "https://books.toscrape.com/"
selectores_items = ["article.product_pod", ".product_pod"]
```

### Step 4: Run!
```bash
python3 web_scraper_auto.py
```

### Step 5: Check Results
```bash
# View the Excel file
ls -lh productos_extraidos.xlsx

# Or CSV if Excel failed
ls -lh productos_extraidos.csv
```

## 🎯 Finding CSS Selectors

1. Open target website in Chrome
2. Right-click on a product → **Inspect**
3. Find the container element (usually `<div>`, `<article>`, or `<li>`)
4. Look for the `class` attribute
5. Use that class in `selectores_items`

**Example:**
```html
<article class="product_pod">
  <h3>Product Name</h3>
  <p class="price_color">$19.99</p>
</article>
```

**Selector:** `"article.product_pod"` or `".product_pod"`

## 📝 Common Configurations

### Books to Scrape (Easy - Recommended for Testing)
```python
url = "https://books.toscrape.com/"
selectores_items = ["article.product_pod"]
```

### eBay
```python
url = "https://www.ebay.com/sch/i.html?_nkw=laptop"
selectores_items = ["li.s-item", ".s-item"]
```

### Amazon (Requires VPN/Proxy)
```python
url = "https://www.amazon.com/s?k=laptop"
selectores_items = [
    "div[data-component-type='s-search-result']",
    ".s-result-item"
]
```

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Chrome not found | Install Chrome/Chromium |
| No products found | Check CSS selectors in DevTools |
| CAPTCHA detected | Use VPN, add delays, or use APIs |
| Timeout errors | Increase `tiempo_espera_inicial` |
| Script hangs | Set `modo_headless = False` to debug |

## 📊 Output Files

After successful run:
- ✅ `productos_extraidos.xlsx` - Your data in Excel
- ✅ `page_full.html` - Full page HTML for debugging
- ✅ `captura_inicial.png` - Screenshot at start
- ✅ `captura_final.png` - Screenshot after scroll

## 💡 Pro Tips

1. **Test First**: Always test with `books.toscrape.com` before real sites
2. **Headless Mode**: Set `modo_headless = False` to see what's happening
3. **Increase Delays**: If getting blocked, increase wait times
4. **Check robots.txt**: Visit `https://example.com/robots.txt`
5. **Use APIs**: Many sites offer official APIs (better than scraping)

## 🚨 Important Notes

- ⚠️ **This sandbox doesn't have Chrome** - install it first!
- ⚠️ **Respect websites** - don't overload servers
- ⚠️ **Check legality** - read Terms of Service
- ⚠️ **Use responsibly** - for educational purposes

## 📚 Need More Help?

- **Full Guide**: See `README_SCRAPER.md`
- **Installation**: See `SETUP_INSTRUCTIONS.md`
- **Overview**: See `SUMMARY.md`

## ✅ Verification

Test the scraper logic without Chrome:
```bash
python3 test_scraper_offline.py
```

This should output:
```
✅ 5 PRODUCTOS EXTRAÍDOS
📂 Excel guardado: /vercel/sandbox/test_productos.xlsx
```

---

**Ready to scrape? Edit `web_scraper_auto.py` and run it!** 🎉
