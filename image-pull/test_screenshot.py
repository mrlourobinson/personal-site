#!/usr/bin/env python3
"""
Test script - new approach with smooth scrolling to trigger lazy loading
"""

import json
import os
import re
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright
import time


def remove_cookie_banners(page):
    """Remove cookie banners"""
    try:
        page.evaluate('''
            // Remove cookie banners
            const selectors = [
                '[id*="cookie"]', '[class*="cookie"]',
                '[id*="consent"]', '[class*="consent"]',
                '[id*="onetrust"]', '[class*="onetrust"]',
                '[id*="privacy"]', '[class*="privacy"]',
                '[class*="banner"]', '[class*="modal"]',
                '[class*="overlay"]', '[id*="modal"]'
            ];
            
            selectors.forEach(selector => {
                try {
                    document.querySelectorAll(selector).forEach(el => {
                        const rect = el.getBoundingClientRect();
                        if (rect.height < window.innerHeight * 0.5 || 
                            el.innerText.toLowerCase().includes('cookie') || 
                            el.innerText.toLowerCase().includes('privacy') || 
                            el.innerText.toLowerCase().includes('consent')) {
                            el.remove();
                        }
                    });
                } catch (e) {}
            });
            
            // Remove backdrop overlays
            document.querySelectorAll('body > div').forEach(div => {
                const style = window.getComputedStyle(div);
                if (style.position === 'fixed' && style.zIndex > 1000 && 
                    (style.backgroundColor.includes('rgba') || style.background.includes('rgba'))) {
                    div.remove();
                }
            });
            
            document.body.style.overflow = 'auto';
            document.documentElement.style.overflow = 'auto';
        ''')
        time.sleep(0.5)
    except:
        pass


def extract_slug_from_url(url):
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    parts = path.split('/')
    parts = [p for p in parts if p not in ['index.html', 'index.htm', '']]
    if parts:
        slug = parts[-1]
        slug = re.sub(r'\.(html|htm|php)$', '', slug)
        return slug
    return parsed.netloc.replace('.', '-')


# Load first project
with open('projects.json', 'r') as f:
    projects = json.load(f)

project = projects[0]
url = project['url']
slug = extract_slug_from_url(url)

print(f"Testing with: {project['name']}")
print(f"URL: {url}\n")

os.makedirs('screenshots/desktop', exist_ok=True)
os.makedirs('screenshots/mobile', exist_ok=True)

desktop_viewport = {'width': 1100, 'height': 800}
mobile_viewport = {'width': 390, 'height': 844}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    print("=== DESKTOP ===")
    context = browser.new_context(viewport=desktop_viewport)
    page = context.new_page()
    
    print("Loading page...")
    page.goto(url, wait_until='domcontentloaded', timeout=120000)
    time.sleep(5)
    
    print("Removing cookie banners...")
    remove_cookie_banners(page)
    
    print("Smooth scroll pass 1 (down)...")
    page.evaluate('''
        async () => {
            const distance = 500;
            const delay = 200;
            const height = document.body.scrollHeight;
            
            for (let scrolled = 0; scrolled < height; scrolled += distance) {
                window.scrollTo(0, scrolled);
                await new Promise(resolve => setTimeout(resolve, delay));
            }
            window.scrollTo(0, height);
        }
    ''')
    time.sleep(8)
    
    print("Smooth scroll pass 2 (up)...")
    page.evaluate('''
        async () => {
            const distance = 500;
            const delay = 200;
            const height = document.body.scrollHeight;
            
            for (let scrolled = height; scrolled > 0; scrolled -= distance) {
                window.scrollTo(0, scrolled);
                await new Promise(resolve => setTimeout(resolve, delay));
            }
            window.scrollTo(0, 0);
        }
    ''')
    time.sleep(8)
    
    print("Final scroll pass...")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(6)
    page.evaluate("window.scrollTo(0, 0)")
    time.sleep(4)
    
    print("Waiting for images/iframes...")
    page.evaluate('''
        new Promise((resolve) => {
            const timeout = setTimeout(resolve, 15000);
            const images = Array.from(document.images);
            const iframes = Array.from(document.querySelectorAll('iframe'));
            const all = [...images, ...iframes];
            
            if (all.length === 0) {
                clearTimeout(timeout);
                resolve();
                return;
            }
            
            let loaded = 0;
            const checkComplete = () => {
                loaded++;
                if (loaded >= all.length) {
                    clearTimeout(timeout);
                    resolve();
                }
            };
            
            all.forEach(el => {
                if (el.complete || el.readyState === 'complete') {
                    checkComplete();
                } else {
                    el.addEventListener('load', checkComplete);
                    el.addEventListener('error', checkComplete);
                }
            });
        });
    ''')
    time.sleep(3)
    
    desktop_path = f"screenshots/desktop/{slug}.png"
    page.screenshot(path=desktop_path, full_page=True)
    print(f"✓ Saved: {desktop_path}\n")
    
    page.close()
    context.close()
    
    print("=== MOBILE ===")
    context = browser.new_context(
        viewport=mobile_viewport,
        device_scale_factor=3,
        is_mobile=True,
        has_touch=True,
        user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
    )
    page = context.new_page()
    
    print("Loading page...")
    page.goto(url, wait_until='domcontentloaded', timeout=120000)
    time.sleep(5)
    
    print("Removing cookie banners...")
    remove_cookie_banners(page)
    
    print("Smooth scroll pass 1 (down)...")
    page.evaluate('''
        async () => {
            const distance = 500;
            const delay = 200;
            const height = document.body.scrollHeight;
            
            for (let scrolled = 0; scrolled < height; scrolled += distance) {
                window.scrollTo(0, scrolled);
                await new Promise(resolve => setTimeout(resolve, delay));
            }
            window.scrollTo(0, height);
        }
    ''')
    time.sleep(8)
    
    print("Smooth scroll pass 2 (up)...")
    page.evaluate('''
        async () => {
            const distance = 500;
            const delay = 200;
            const height = document.body.scrollHeight;
            
            for (let scrolled = height; scrolled > 0; scrolled -= distance) {
                window.scrollTo(0, scrolled);
                await new Promise(resolve => setTimeout(resolve, delay));
            }
            window.scrollTo(0, 0);
        }
    ''')
    time.sleep(8)
    
    print("Final scroll pass...")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(6)
    page.evaluate("window.scrollTo(0, 0)")
    time.sleep(4)
    
    print("Waiting for images/iframes...")
    page.evaluate('''
        new Promise((resolve) => {
            const timeout = setTimeout(resolve, 15000);
            const images = Array.from(document.images);
            const iframes = Array.from(document.querySelectorAll('iframe'));
            const all = [...images, ...iframes];
            
            if (all.length === 0) {
                clearTimeout(timeout);
                resolve();
                return;
            }
            
            let loaded = 0;
            const checkComplete = () => {
                loaded++;
                if (loaded >= all.length) {
                    clearTimeout(timeout);
                    resolve();
                }
            };
            
            all.forEach(el => {
                if (el.complete || el.readyState === 'complete') {
                    checkComplete();
                } else {
                    el.addEventListener('load', checkComplete);
                    el.addEventListener('error', checkComplete);
                }
            });
        });
    ''')
    time.sleep(3)
    
    mobile_path = f"screenshots/mobile/{slug}.png"
    page.screenshot(path=mobile_path, full_page=True)
    print(f"✓ Saved: {mobile_path}\n")
    
    page.close()
    context.close()
    browser.close()

print("✓ Test complete!")
print(f"\nCheck screenshots:")
print(f"  Desktop: screenshots/desktop/{slug}.png")
print(f"  Mobile: screenshots/mobile/{slug}.png")
