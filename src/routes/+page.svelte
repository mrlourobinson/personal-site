<script>
    import ProjectCards from '../lib/ProjectCards.svelte'
    import CardShuffle from '../lib/CardShuffle.svelte'
  
    import projects from './assets/projects.json'
  </script>

<ProjectCards {projects}/>

<!-- <CardShuffle /> -->