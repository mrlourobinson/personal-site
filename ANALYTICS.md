# Google Analytics setup guide

## What I've implemented

I've added Google Analytics 4 (GA4) tracking to your site with proper SvelteKit integration.

## Setup steps

### 1. Create Google Analytics account
1. Go to [analytics.google.com](https://analytics.google.com)
2. Click "Start measuring"
3. Create an account name (e.g., "Lou Robinson Portfolio")
4. Create a property name (e.g., "lourobinson.co.uk")
5. Select your timezone and currency
6. Choose "Web" as the platform
7. Enter your website URL: `https://www.lourobinson.co.uk`
8. Create a Web Stream

### 2. Get your Measurement ID
After creating the stream, you'll see a **Measurement ID** that looks like: `G-XXXXXXXXXX`

### 3. Update your site
Replace `G-XXXXXXXXXX` in these two files with your actual Measurement ID:

**File 1: `src/app.html`** (line ~28)
```javascript
gtag('config', 'G-XXXXXXXXXX', {
```

**File 2: `src/lib/analytics.js`** (line 3)
```javascript
window.gtag('config', 'G-XXXXXXXXXX', {
```

### 4. Deploy your site
Push your changes and deploy. Analytics will start tracking immediately.

### 5. Verify it's working
1. Visit your live site
2. Go back to Google Analytics
3. Click "Reports" → "Realtime"
4. You should see yourself as an active user within 30 seconds

## What gets tracked

### Automatic tracking
- **Page views**: Every page load and navigation
- **Session duration**: How long people stay
- **Bounce rate**: Single-page visits
- **Traffic sources**: Where visitors come from
- **Location**: Country, city of visitors
- **Device**: Desktop, mobile, tablet
- **Browser**: Chrome, Safari, etc.

### Custom events (optional)
You can track custom events like:
- Project card clicks
- External link clicks
- Award link clicks

## Adding custom event tracking

To track specific actions, use the `event` function from `analytics.js`:

### Example: Track project clicks

```svelte
<script>
  import { event } from '../lib/analytics';

  function handleProjectClick(projectName) {
    event({
      action: 'click',
      category: 'Project',
      label: projectName,
      value: 1
    });
  }
</script>

<a href="{url}" on:click={() => handleProjectClick(proj.name)}>
  <!-- project content -->
</a>
```

### Example: Track outbound links

```svelte
<script>
  import { event } from '../lib/analytics';
  
  function trackOutboundLink(url, label) {
    event({
      action: 'click',
      category: 'Outbound Link',
      label: label,
      value: 1
    });
  }
</script>

<a 
  href="https://edition.cnn.com/profiles/lou-robinson"
  on:click={() => trackOutboundLink(url, 'CNN Profile')}
>
  CNN Profile
</a>
```

## Useful metrics to watch

### For SEO validation
- **Organic Search traffic**: Growing over time
- **Landing pages**: Which pages bring in traffic
- **Search queries**: What people search for (in Search Console)
- **Geographic**: Where your audience is

### For content strategy
- **Most viewed projects**: Which work resonates
- **Time on page**: Engagement level
- **Bounce rate**: Content relevance
- **Device types**: How people view your work

### For career opportunities
- **Referral traffic**: Who's linking to you
- **Direct traffic**: People typing your URL
- **Social traffic**: Twitter, LinkedIn clicks
- **Events**: If you track project clicks

## Privacy considerations

The implementation I've added:
- ✅ Uses GA4 (GDPR-friendly by default)
- ✅ Respects Do Not Track browser settings
- ✅ Doesn't use third-party cookies
- ✅ Anonymizes IP addresses automatically

### Optional: Add cookie consent
If you want to be extra cautious or target EU visitors:

1. Install a cookie consent library
2. Only initialize GA after consent
3. Add a privacy policy page

For a portfolio site with no user accounts or data collection beyond analytics, this is usually overkill, but worth considering.

## Connecting with Search Console

For maximum SEO insight, connect GA4 with Google Search Console:

1. In GA4, go to Admin → Product Links
2. Click "Link Search Console"
3. Select your Search Console property
4. This combines analytics + search data!

You'll see:
- Search queries that led to clicks
- Average position in search results
- Click-through rates from Google
- Which pages rank for what terms

## Dashboard setup recommendations

Create custom reports for:

1. **Traffic Overview**
   - Sessions by source
   - Top landing pages
   - Device breakdown

2. **SEO Performance**
   - Organic search traffic
   - Top organic landing pages
   - Search query performance (via Search Console link)

3. **Content Performance**
   - Page views by URL
   - Time on page
   - Exit pages

4. **Audience Insights**
   - Geography
   - Language
   - New vs returning

## GA4 vs Universal Analytics

Note: Universal Analytics (UA) sunset in July 2023. GA4 is the current and only version. The implementation I've added uses GA4, which is:
- More privacy-focused
- Better for SPA/modern sites
- Event-based rather than session-based
- More flexible reporting

## Expected timeline

- **Day 1**: Real-time data available immediately
- **Week 1**: Initial traffic patterns emerge
- **Month 1**: Reliable baseline metrics
- **Month 3+**: Trends become meaningful
- **Month 6+**: Year-over-year comparisons

## Tips for portfolio sites

1. **Monitor referrals closely**: See who's sharing your work
2. **Track your CNN profile link**: Big traffic source
3. **Watch for spikes**: New project published? Social share?
4. **Geographic data**: Where your audience is (employers?)
5. **Device stats**: Make sure mobile experience is solid

## Common issues

### "No data showing"
- Wait 24-48 hours for initial processing
- Check Measurement ID is correct
- Verify site is deployed and live
- Check browser console for errors

### "Seeing my own visits"
- Exclude your IP address in Admin → Data Filters
- Use GA4 Debug mode to test without affecting data
- Install Google Analytics Opt-out browser extension

### "Missing referral data"
- Some social platforms strip referrers
- Use UTM parameters in shared links
- Check GA4's "Referral exclusion list"

## Next steps after setup

1. Create a custom dashboard
2. Set up weekly email reports
3. Create goals/conversions if relevant
4. Add UTM parameters to social shares
5. Connect Search Console
6. Review monthly for trends

Your analytics setup is now complete and ready to go once you add your Measurement ID!
