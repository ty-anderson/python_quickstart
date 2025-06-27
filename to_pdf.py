from playwright.sync_api import sync_playwright
import os

INPUT_FILE = "site/print_page/index.html"
OUTPUT_FILE = "output/full_document.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("file://" + os.path.abspath(INPUT_FILE))
    page.pdf(
        path=OUTPUT_FILE,
        format="A4",
        print_background=True,
        margin={"top": "1in", "bottom": "1in", "left": "0.75in", "right": "0.75in"}
    )
    print(f"✅ Full PDF saved to {OUTPUT_FILE}")
    browser.close()
