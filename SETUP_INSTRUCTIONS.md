# 🚀 Setup Instructions for Web Scraper

## ⚠️ Important: Chrome/Chromium Required

The web scraper requires Chrome or Chromium browser to be installed. This sandbox environment **does not have Chrome installed**.

## 📦 Installation Steps

### For Amazon Linux 2023 / Fedora / RHEL

```bash
# Install Chromium
sudo dnf install chromium -y

# Verify installation
chromium --version
```

### For Ubuntu / Debian

```bash
# Update package list
sudo apt-get update

# Install Chromium
sudo apt-get install chromium-browser -y

# Or install Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f

# Verify installation
chromium-browser --version
# or
google-chrome --version
```

### For macOS

```bash
# Using Homebrew
brew install --cask google-chrome

# Or download from: https://www.google.com/chrome/
```

### For Windows

1. Download Chrome from: https://www.google.com/chrome/
2. Install normally
3. Use `web_scraper.py` (Edge version) instead

## 🐍 Python Dependencies

Already installed in this environment:

```bash
pip install -r requirements.txt
```

Packages installed:
- ✅ selenium (4.36.0)
- ✅ beautifulsoup4 (4.14.2)
- ✅ pandas (2.3.3)
- ✅ openpyxl (3.1.5)
- ✅ lxml (6.0.2)
- ✅ webdriver-manager (4.0.2)

## 🎯 Which Script to Use?

### 1. **web_scraper.py** (Original - Windows Edge)
- ✅ Best for: Windows users with Microsoft Edge
- ❌ Won't work on: Linux/Mac without Edge

### 2. **web_scraper_improved.py** (Linux/Mac - Chrome)
- ✅ Best for: Linux/Mac with Chrome/Chromium
- ✅ More organized code structure
- ✅ Better error handling
- ❌ Requires: Chrome/Chromium installed

### 3. **web_scraper_auto.py** (Recommended - Auto ChromeDriver)
- ✅ Best for: Any system with Chrome
- ✅ Automatically downloads correct ChromeDriver
- ✅ Simplest to use
- ✅ Most portable
- ❌ Requires: Chrome/Chromium installed

## 🧪 Testing Without Chrome

If you can't install Chrome, you can still test the HTML parsing logic:

```bash
# Create a test with saved HTML
python test_scraper_offline.py
```

## 🔧 Quick Start (After Chrome Installation)

```bash
# 1. Edit the configuration in web_scraper_auto.py
# Change these lines:
url = "https://books.toscrape.com/"
selectores_items = ["article.product_pod", ".product_pod"]

# 2. Run the scraper
python web_scraper_auto.py

# 3. Check the output
ls -lh productos_extraidos.*
```

## 📊 Output Files

After successful execution:
- `productos_extraidos.xlsx` - Excel file with scraped data
- `productos_extraidos.csv` - CSV fallback if Excel fails
- `page_full.html` - Complete HTML of the page
- `captura_inicial.png` - Screenshot at page load
- `captura_final.png` - Screenshot after scrolling

## 🐛 Troubleshooting

### Error: "ChromeDriver not found"
```bash
# Solution: webdriver-manager will auto-download
# Or manually install:
pip install webdriver-manager
```

### Error: "Chrome binary not found"
```bash
# Install Chrome/Chromium (see above)
# Or specify Chrome location:
chrome_options.binary_location = "/path/to/chrome"
```

### Error: "No se encontraron productos"
1. Open `page_full.html` in browser
2. Inspect a product element
3. Find the CSS selector
4. Update `selectores_items` in the script

### Error: "CAPTCHA detected"
- Use VPN or proxy
- Reduce request frequency
- Add more delays
- Consider using official APIs

## 🌐 Recommended Test Sites

Start with these scraper-friendly sites:

1. **Books to Scrape** (Best for testing)
   ```python
   url = "https://books.toscrape.com/"
   selectores_items = ["article.product_pod"]
   ```

2. **Quotes to Scrape**
   ```python
   url = "http://quotes.toscrape.com/"
   selectores_items = [".quote"]
   ```

3. **Scrapethissite**
   ```python
   url = "https://www.scrapethissite.com/pages/simple/"
   selectores_items = [".country"]
   ```

## ⚖️ Legal & Ethical Considerations

- ✅ Always check `robots.txt`
- ✅ Respect rate limits
- ✅ Read Terms of Service
- ✅ Use official APIs when available
- ❌ Don't overload servers
- ❌ Don't scrape personal data without consent

## 📚 Additional Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Web Scraping Best Practices](https://www.scrapehero.com/web-scraping-best-practices/)

## 💡 Tips for Success

1. **Start Simple**: Test with `books.toscrape.com` first
2. **Inspect Elements**: Use browser DevTools to find selectors
3. **Add Delays**: Don't scrape too fast
4. **Handle Errors**: Websites change, code should adapt
5. **Use APIs**: When available, APIs are better than scraping
