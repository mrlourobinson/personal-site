<script>
  import { crossfade, fade, fly } from 'svelte/transition';
  import Legend from '../lib/Legend.svelte';

  export let projects = [];

  let filtered = false;
  let currentFilter = '';
  let sortBy = 'date'; // 'date', 'name', 'type'
  let sortOrder = 'desc'; // 'asc', 'desc'
  let visibleProjects = [...projects];

    function filterCards(classToKeep, event) {
    if (!filtered || currentFilter !== classToKeep) {
        // Activate filter
        currentFilter = classToKeep;
        filtered = true;
    } else {
        // Deactivate filter (show all)
        currentFilter = '';
        filtered = false;
    }
    // Remove focus from the button after action
    event.target.blur();
    updateVisibleProjects();
    }

    function updateVisibleProjects() {
        let filteredProjects = [...projects];
        
        // Apply category filter
        if (filtered && currentFilter) {
            filteredProjects = filteredProjects.filter(p => p.type.includes(currentFilter));
        }
        
        // Apply sorting
        filteredProjects.sort((a, b) => {
            let aVal, bVal;
            
            if (sortBy === 'date') {
                // Convert date strings to comparable format
                aVal = new Date(a.date + ' 1, 2000').getTime(); // Add year for parsing
                bVal = new Date(b.date + ' 1, 2000').getTime();
            } else if (sortBy === 'name') {
                aVal = a.name.toLowerCase();
                bVal = b.name.toLowerCase();
            } else if (sortBy === 'type') {
                aVal = a.type.toLowerCase();
                bVal = b.type.toLowerCase();
            }
            
            if (sortOrder === 'asc') {
                return aVal > bVal ? 1 : -1;
            } else {
                return aVal < bVal ? 1 : -1;
            }
        });
        
        visibleProjects = filteredProjects;
    }

    function showAllProjects() {
        filtered = false;
        currentFilter = '';
        updateVisibleProjects();
    }

    // Reactive statement to update visible projects when sorting changes
    $: if (sortBy || sortOrder) {
        updateVisibleProjects();
    }
</script>

<div class="section-title bottom-border">
    
    <div class="key">
        <span class="key-label">Projects ({visibleProjects.length})</span>
        <span id="key-buttons" style="white-space: nowrap;">
            <span class="key-label">Filter: </span>
            <button class="key-text data" class:highlighted={currentFilter === 'data'} on:click={(e) => filterCards('data', e)} aria-label="Filter by data projects">Data</button> 
            <button class="key-text carto" class:highlighted={currentFilter === 'carto'} on:click={(e) => filterCards('carto', e)} aria-label="Filter by cartography projects">Cartography</button> 
            <button class="key-text interactive" class:highlighted={currentFilter === 'interactive'} on:click={(e) => filterCards('interactive', e)} aria-label="Filter by interactive projects">Interactive</button> 
            <button class="key-text explainer" class:highlighted={currentFilter === 'explainer'} on:click={(e) => filterCards('explainer', e)} aria-label="Filter by explainer projects">Explainer</button> 
        </span> 
    </div>
    
    <!-- <div class="sort-container">
        <span class="key-label">Sort by: </span>
        <select bind:value={sortBy} class="sort-select" aria-label="Sort projects by">
            <option value="date">Date</option>
            <option value="name">Name</option>
            <option value="type">Type</option>
        </select>
        <button 
            class="sort-order-btn" 
            on:click={() => sortOrder = sortOrder === 'desc' ? 'asc' : 'desc'}
            aria-label="Toggle sort order"
        >
            {sortOrder === 'desc' ? '↓' : '↑'}
        </button>
    </div> -->
</div>



<div class="cards">
  {#if visibleProjects.length === 0}
    <div class="empty-state">
      <p>No projects found for the selected filter.</p>
      <button class="key-text" on:click={() => showAllProjects()}>Show all projects</button>
    </div>
  {:else}
    {#each visibleProjects as proj (proj.name)}
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
  {/if}
</div>





