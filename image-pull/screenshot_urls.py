#!/usr/bin/env python3
"""
Screenshot script for taking desktop and mobile screenshots of URLs from projects.json
"""

import json
import os
import re
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright
import time


def remove_cookie_banners(page):
    """
    Remove common cookie consent banners and popups from the page.
    """
    try:
        # More comprehensive script to remove cookie banners and overlays
        page.evaluate('''
            // Remove common cookie banner elements
            const selectors = [
                '[id*="cookie"]',
                '[class*="cookie"]',
                '[id*="consent"]',
                '[class*="consent"]',
                '[id*="onetrust"]',
                '[class*="onetrust"]',
                '[id*="privacy"]',
                '[class*="privacy"]',
                '[class*="banner"]',
                '[class*="gdpr"]',
                '[id*="gdpr"]',
                '.evidon-banner',
                '.qc-cmp2-container',
                '[class*="CookieNotice"]',
                '[class*="cookie-notice"]',
                '[id*="CookieBanner"]',
                '[class*="CookieBanner"]',
                // CNN specific
                '.privacy-manager',
                '#privacy-manager',
                '.privacy-banner',
                '[class*="modal"]',
                '[class*="overlay"]',
                '[id*="modal"]'
            ];
            
            selectors.forEach(selector => {
                try {
                    document.querySelectorAll(selector).forEach(el => {
                        // Check if it might be a cookie banner (not too large)
                        const rect = el.getBoundingClientRect();
                        if (rect.height < window.innerHeight * 0.5 || el.innerText.toLowerCase().includes('cookie') || el.innerText.toLowerCase().includes('privacy') || el.innerText.toLowerCase().includes('consent')) {
                            el.remove();
                        }
                    });
                } catch (e) {}
            });
            
            // Remove any backdrop/overlay elements
            document.querySelectorAll('body > div').forEach(div => {
                const style = window.getComputedStyle(div);
                if (style.position === 'fixed' && style.zIndex > 1000 && 
                    (style.backgroundColor.includes('rgba') || style.background.includes('rgba'))) {
                    div.remove();
                }
            });
            
            // Re-enable scrolling if it was disabled
            document.body.style.overflow = 'auto';
            document.documentElement.style.overflow = 'auto';
        ''')
        
        # Wait a moment for any DOM updates
        time.sleep(0.5)
        
        # Try to click accept buttons
        accept_selectors = [
            'button:has-text("Accept")',
            'button:has-text("Agree")',
            'button:has-text("I Accept")',
            'button:has-text("OK")',
            'button:has-text("Got it")',
            '[class*="accept"][role="button"]',
            '[id*="accept"][role="button"]',
        ]
        
        for selector in accept_selectors:
            try:
                page.click(selector, timeout=500)
                time.sleep(0.5)
                break
            except:
                continue
                
    except Exception as e:
        # Silently fail if cookie banner removal doesn't work
        pass


def extract_slug_from_url(url):
    """
    Extract a slug from the URL path.
    For example: 'https://edition.cnn.com/interactive/2025/08/05/world/north-korea-it-worker-scheme-vis-intl-hnk/index.html'
    Returns: 'north-korea-it-worker-scheme-vis-intl-hnk'
    """
    parsed = urlparse(url)
    path = parsed.path
    
    # Remove leading/trailing slashes
    path = path.strip('/')
    
    # Split by slashes and get the last meaningful part
    parts = path.split('/')
    
    # Filter out common file names
    parts = [p for p in parts if p not in ['index.html', 'index.htm', '']]
    
    if parts:
        # Get the last part which is usually the slug
        slug = parts[-1]
        
        # Remove file extensions
        slug = re.sub(r'\.(html|htm|php)$', '', slug)
        
        return slug
    
    # Fallback: use the domain name if no path
    return parsed.netloc.replace('.', '-')


def take_screenshots(json_file, output_dir='screenshots'):
    """
    Take desktop and mobile screenshots of all URLs in the JSON file.
    
    Args:
        json_file: Path to the JSON file containing URLs
        output_dir: Directory to save screenshots (default: 'screenshots')
    """
    # Create output directories
    desktop_dir = os.path.join(output_dir, 'desktop')
    mobile_dir = os.path.join(output_dir, 'mobile')
    os.makedirs(desktop_dir, exist_ok=True)
    os.makedirs(mobile_dir, exist_ok=True)
    
    # Load URLs from JSON
    with open(json_file, 'r') as f:
        projects = json.load(f)
    
    # Desktop viewport (1100px wide)
    desktop_viewport = {'width': 1100, 'height': 800}
    
    # iPhone 14 viewport
    # iPhone 14: 390 x 844 points (1170 x 2532 pixels at 3x)
    mobile_viewport = {'width': 390, 'height': 844}
    
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        
        print(f"Processing {len(projects)} URLs...\n")
        
        for idx, project in enumerate(projects, 1):
            url = project.get('url')
            if not url:
                print(f"[{idx}/{len(projects)}] Skipping project (no URL): {project.get('name', 'Unknown')}")
                continue
            
            # Skip interactive pages as they won't load properly
            if '/interactive/' in url:
                print(f"[{idx}/{len(projects)}] Skipping interactive page: {project.get('name', 'Unknown')}")
                print(f"  URL: {url}\n")
                continue
            
            slug = extract_slug_from_url(url)
            project_name = project.get('name', 'Unknown')
            
            print(f"[{idx}/{len(projects)}] Processing: {project_name}")
            print(f"  URL: {url}")
            print(f"  Slug: {slug}")
            
            try:
                # Desktop screenshot
                print(f"  Taking desktop screenshot...")
                context_desktop = browser.new_context(viewport=desktop_viewport)
                page_desktop = context_desktop.new_page()
                
                # Set longer timeout and wait for domcontentloaded first
                page_desktop.goto(url, wait_until='domcontentloaded', timeout=120000)
                
                print(f"  Waiting for initial load...")
                time.sleep(5)
                
                # Remove cookie banners early
                print(f"  Removing cookie banners...")
                remove_cookie_banners(page_desktop)
                
                # Perform multiple scroll passes to trigger all lazy loading
                print(f"  Triggering lazy load (pass 1/3)...")
                page_desktop.evaluate('''
                    async () => {
                        // Scroll in chunks to trigger lazy loading
                        const distance = 500;
                        const delay = 200;
                        const height = Math.max(
                            document.body?.scrollHeight || 0,
                            document.documentElement?.scrollHeight || 0
                        );
                        
                        if (height === 0) return;
                        
                        for (let scrolled = 0; scrolled < height; scrolled += distance) {
                            window.scrollTo(0, scrolled);
                            await new Promise(resolve => setTimeout(resolve, delay));
                        }
                        window.scrollTo(0, height);
                    }
                ''')
                time.sleep(8)
                
                # Second pass - go back up
                print(f"  Triggering lazy load (pass 2/3)...")
                page_desktop.evaluate('''
                    async () => {
                        const distance = 500;
                        const delay = 200;
                        const height = Math.max(
                            document.body?.scrollHeight || 0,
                            document.documentElement?.scrollHeight || 0
                        );
                        
                        if (height === 0) return;
                        
                        for (let scrolled = height; scrolled > 0; scrolled -= distance) {
                            window.scrollTo(0, scrolled);
                            await new Promise(resolve => setTimeout(resolve, delay));
                        }
                        window.scrollTo(0, 0);
                    }
                ''')
                time.sleep(8)
                
                # Third pass - quick final scroll
                print(f"  Triggering lazy load (pass 3/3)...")
                page_desktop.evaluate("window.scrollTo(0, Math.max(document.body?.scrollHeight || 0, document.documentElement?.scrollHeight || 0))")
                time.sleep(6)
                page_desktop.evaluate("window.scrollTo(0, 0)")
                time.sleep(4)
                
                # Wait for images and iframes
                print(f"  Waiting for images and iframes...")
                page_desktop.evaluate('''
                    new Promise((resolve) => {
                        const timeout = setTimeout(resolve, 15000); // 15 sec max wait
                        
                        // Wait for all images
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
                
                desktop_path = os.path.join(desktop_dir, f"{slug}.png")
                page_desktop.screenshot(path=desktop_path, full_page=True)
                print(f"  ✓ Desktop saved: {desktop_path}")
                
                page_desktop.close()
                context_desktop.close()
                
                # Mobile screenshot
                print(f"  Taking mobile screenshot...")
                context_mobile = browser.new_context(
                    viewport=mobile_viewport,
                    device_scale_factor=3,  # iPhone 14 has 3x display
                    is_mobile=True,
                    has_touch=True,
                    user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
                )
                page_mobile = context_mobile.new_page()
                
                # Set longer timeout and wait for domcontentloaded first
                page_mobile.goto(url, wait_until='domcontentloaded', timeout=120000)
                
                print(f"  Waiting for initial load...")
                time.sleep(5)
                
                # Remove cookie banners early
                remove_cookie_banners(page_mobile)
                
                # Perform multiple scroll passes to trigger all lazy loading
                print(f"  Triggering lazy load (pass 1/3)...")
                page_mobile.evaluate('''
                    async () => {
                        // Scroll in chunks to trigger lazy loading
                        const distance = 500;
                        const delay = 200;
                        const height = Math.max(
                            document.body?.scrollHeight || 0,
                            document.documentElement?.scrollHeight || 0
                        );
                        
                        if (height === 0) return;
                        
                        for (let scrolled = 0; scrolled < height; scrolled += distance) {
                            window.scrollTo(0, scrolled);
                            await new Promise(resolve => setTimeout(resolve, delay));
                        }
                        window.scrollTo(0, height);
                    }
                ''')
                time.sleep(8)
                
                # Second pass - go back up
                print(f"  Triggering lazy load (pass 2/3)...")
                page_mobile.evaluate('''
                    async () => {
                        const distance = 500;
                        const delay = 200;
                        const height = Math.max(
                            document.body?.scrollHeight || 0,
                            document.documentElement?.scrollHeight || 0
                        );
                        
                        if (height === 0) return;
                        
                        for (let scrolled = height; scrolled > 0; scrolled -= distance) {
                            window.scrollTo(0, scrolled);
                            await new Promise(resolve => setTimeout(resolve, delay));
                        }
                        window.scrollTo(0, 0);
                    }
                ''')
                time.sleep(8)
                
                # Third pass - quick final scroll
                print(f"  Triggering lazy load (pass 3/3)...")
                page_mobile.evaluate("window.scrollTo(0, Math.max(document.body?.scrollHeight || 0, document.documentElement?.scrollHeight || 0))")
                time.sleep(6)
                page_mobile.evaluate("window.scrollTo(0, 0)")
                time.sleep(4)
                
                # Wait for images and iframes
                page_mobile.evaluate('''
                    new Promise((resolve) => {
                        const timeout = setTimeout(resolve, 15000); // 15 sec max wait
                        
                        // Wait for all images
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
                
                mobile_path = os.path.join(mobile_dir, f"{slug}.png")
                page_mobile.screenshot(path=mobile_path, full_page=True)
                print(f"  ✓ Mobile saved: {mobile_path}")
                
                page_mobile.close()
                context_mobile.close()
                
                print(f"  ✓ Completed\n")
                
            except Exception as e:
                print(f"  ✗ Error: {str(e)}\n")
                continue
        
        browser.close()
    
    print(f"\n✓ All screenshots completed!")
    print(f"  Desktop screenshots: {desktop_dir}")
    print(f"  Mobile screenshots: {mobile_dir}")


if __name__ == '__main__':
    # Use the projects.json file in the current directory
    json_file = 'projects.json'
    
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found!")
        exit(1)
    
    take_screenshots(json_file)

