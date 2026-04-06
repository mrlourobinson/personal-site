# SEO optimization guide

## What I've implemented

### 1. Enhanced structured data (Schema.org)
Your site now includes comprehensive Schema.org markup that helps Google understand:
- Your name, job title, and professional details
- Your employer (CNN) and role
- Your location (London)
- Your skills and areas of expertise
- Links to your CNN profile

This is the foundation for appearing in Google Knowledge Panels when someone searches your name.

### 2. Open Graph and Twitter cards
Added complete social media metadata so when your site is shared:
- Shows proper title, description, and image
- Looks professional on LinkedIn, Twitter, Facebook
- Uses your cover image as the preview

### 3. SEO meta tags
- Dynamic page titles for each page
- Unique descriptions for home and about pages
- Keywords for search engines
- Canonical URLs to prevent duplicate content issues

### 4. Sitemap and robots.txt
- `sitemap.xml` - Tells search engines about all your pages
- `robots.txt` - Allows all search engines to crawl your site

### 5. Semantic HTML
Your existing structure already uses proper heading hierarchy and semantic elements.

## Next steps to maximize your Google presence

### A. Add a professional profile photo
1. Take or find a professional headshot (1200x1200px recommended)
2. Save it as `static/img/lou-robinson-profile.jpg`
3. Update the image URLs in `src/app.html` to use this photo

This helps Google show your photo in Knowledge Panels and search results.

### B. Submit to Google
1. Go to [Google Search Console](https://search.google.com/search-console)
2. Add your site (www.lourobinson.co.uk)
3. Submit your sitemap: `https://www.lourobinson.co.uk/sitemap.xml`
4. Request indexing for both pages

### C. Claim your Google Business Profile (optional)
If you want enhanced visibility:
1. Go to [Google Business Profile](https://business.google.com)
2. Create a profile as a "Service Area Business"
3. Link to your website

### D. Build backlinks
The more authoritative sites that link to you, the better:
- Your CNN profile already links here (excellent!)
- Add your website URL to:
  - LinkedIn profile
  - Twitter/X bio
  - GitHub profile
  - Any professional directories
  - Conference speaker bios
  - Guest articles or interviews

### E. Content optimization tips
- Keep updating your projects.json with new work
- Each project title acts as a keyword
- Your bio includes key terms like "data visualization", "CNN", "London"
- Consider adding blog posts about your work process (great for long-tail keywords)

### F. Social signals
- Share your work on social media with links back to your site
- Engage with the data journalism community
- Get featured in articles/podcasts about data visualization

## Technical details

### Current meta tags structure
```html
- Title: "Lou Robinson - Designer & Visual Journalist"
- Description: Natural language with key terms
- Schema.org Person type with full professional details
- Open Graph images for social sharing
- Twitter card metadata
```

### Keywords you're targeting
- Lou Robinson
- Data visualization
- Visual journalism
- CNN graphics
- Cartography
- Interactive design
- News graphics

## Monitoring your SEO

1. Google Search Console - Track impressions and clicks
2. Search your name in Google periodically
3. Use `site:www.lourobinson.co.uk` to see what Google has indexed
4. Check your CNN profile page links back to your site

## Timeline expectations

- Google crawl: 1-2 weeks after submission
- Initial ranking: 2-4 weeks
- Knowledge Panel: 2-6 months (requires building authority)
- Full optimization: 6-12 months

The most important factor is that your CNN profile page links to your site - this gives you massive authority in Google's eyes!
