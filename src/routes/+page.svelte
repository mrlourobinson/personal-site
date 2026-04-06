<script>
    import ProjectCards from '../lib/ProjectCards.svelte'
    import projects from './assets/projects.json'
</script>

<svelte:head>
  <title>Lou Robinson - Data Visualization & Interactive Journalism</title>
  <meta name="description" content="Portfolio of data visualization, cartography, and interactive journalism projects by Lou Robinson at CNN. Specializing in maps, charts, and news graphics." />
  <meta property="og:title" content="Lou Robinson - Data Visualization & Interactive Journalism" />
  <meta property="og:description" content="Portfolio of data visualization, cartography, and interactive journalism projects by Lou Robinson at CNN." />
  <meta property="og:url" content="https://www.lourobinson.co.uk/" />
  <meta property="og:image" content="https://www.lourobinson.co.uk/img/cover.png" />
  <meta name="twitter:title" content="Lou Robinson - Data Visualization & Interactive Journalism" />
  <meta name="twitter:description" content="Portfolio of data visualization, cartography, and interactive journalism projects by Lou Robinson at CNN." />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content="https://www.lourobinson.co.uk/img/cover.png" />
  <link rel="canonical" href="https://www.lourobinson.co.uk/" />
</svelte:head>

<ProjectCards {projects}/>