<script>
  import { crossfade, fade, fly } from 'svelte/transition';
  import Legend from '../lib/Legend.svelte';

  export let projects = [];

  let filtered = false;
  let currentFilter = '';
  let visibleProjects = [...projects];

    function filterCards(classToKeep) {
    if (!filtered || currentFilter !== classToKeep) {
        visibleProjects = projects.filter(p => p.type.includes(classToKeep));
        filtered = true;
        currentFilter = classToKeep;
    } else {
        visibleProjects = [...projects];
        filtered = false;
        currentFilter = '';
    }
    }
</script>

<div class="section-title bottom-border">
    
    <div class="key">
        <span class="key-label">Projects</span>
        <span id="key-buttons" style="white-space: nowrap;">
            <span class="key-label">Filter: </span>
            <button class="key-text data" on:click={() => filterCards('data')}>Data</button> 
            <button class="key-text carto" on:click={() => filterCards('carto')}>Cartography</button> 
            <button class="key-text interactive" on:click={() => filterCards('interactive')}>Interactive</button> 
            <button class="key-text explainer" on:click={() => filterCards('explainer')}>Explainer</button> 
        </span> 
    </div>
</div>



<div class="cards">
  {#each visibleProjects as proj (proj.name)}
    <div class="card {proj.type}" transition:fade>
      <a href="{proj.url}">
        {#if proj.new == 1}
          <div class="new">New</div>
        {/if}
        <Legend type={proj.type} />
        <div class="date">{proj.date}</div>
        <div class="img-wrapper">
          <img src="../img/{proj.img}" alt="{proj.name}" />
        </div>
        <section class="title-container">
          <div class="text-area">
            <h4>{proj.name}</h4>
          </div>
        </section>
      </a>
    </div>
  {/each}
</div>





