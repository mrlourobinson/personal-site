<script>
  import { crossfade, fade, fly } from 'svelte/transition';
  import Legend from '../lib/Legend.svelte';

  export let projects = [];
</script>

<div class="section-title bottom-border">
    
    <div class="key">
        <span class="key-label">Projects ({projects.length})</span>
    </div>
</div>



<div class="cards">
  {#each projects as proj (proj.name)}
      <div class="card {proj.type}" transition:fade>
        <a href="{proj.url}" target="_blank" rel="noopener noreferrer">
          {#if proj.new == 1}
            <div class="new">New</div>
          {/if}
          <Legend type={proj.type} />
          <div class="date">{proj.date}</div>
          <div class="img-wrapper">
            <img src="../img/{proj.img}" alt="{proj.name}" loading="lazy" />
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





