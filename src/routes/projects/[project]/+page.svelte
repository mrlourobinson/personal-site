<script>
    import {page} from '$app/stores';
    const projectId = $page.params.project;

    import projects from '../../assets/projects.json';

    // Filter projects based on the projectId
    let filteredProject = projects.find(proj => proj.url === projectId);
  </script>
 
  <div class="section-title bottom-border">
    {filteredProject.name} 
  </div>
  
  <div class="container">
    <section class="left">
      {#each filteredProject.imgs as img}
        <img src="../img/{img}" alt="">
      {/each}
    </section>
    <section class="right">
      <p class="bottom-border">{filteredProject.blurb}</p>

      <a href="{filteredProject.liveUrl}" alt="">>> View full project here</a>
    </section>
</div>

