<script>
    import Legend from '../lib/Legend.svelte'

    export let projects = []
    let filtered = false;
    let currentFilter = '';
    
    function filterCards(classToKeep) {

        // Select all card elements
        const cards = document.querySelectorAll('.card');

        
        
        if(filtered == false || filtered == true && currentFilter != classToKeep) {
            // Loop through each card
            cards.forEach(card => {
                // Check if the card contains the secondary class
                if (!card.classList.contains(classToKeep)) {
                    // If the card doesn't have the secondary class, hide it but maintain layout
                    card.style.display = 'none';
                } else {
                    card.style.display = 'flex';
                }
            });

            const buttons = document.querySelectorAll('.key-text');

            buttons.forEach(but => {
                    // Check if the card contains the secondary class
                    if (!but.classList.contains(classToKeep)) {
                        // If the card doesn't have the secondary class, hide it but maintain layout
                        but.style.opacity = 0.5;
                        but.classList.remove('highlighted');
                        
                    } else {
                        but.style.opacity = 1;     
                        but.classList.add('highlighted');
           
                    }
                })


            filtered = true;
            currentFilter = classToKeep;
        } else {
            // Loop through each card
            cards.forEach(card => {
                // Check if the card contains the secondary class
                if (!card.classList.contains(classToKeep)) {
                    // If the card doesn't have the secondary class, hide it but maintain layout
                    card.style.display = 'flex';
                }
            });

            const buttons = document.querySelectorAll('.key-text')
            buttons.forEach(but => {
                but.style.opacity = 1;
                but.classList.remove('highlighted');
            })

            filtered = false;
            currentFilter = '';
        }

    }



</script>

<div class="section-title bottom-border">
    Projects
</div>

<div class="key">
    <span class="key-label">Filter: </span>
    <span style="white-space: nowrap;">
        <button class="key-text data" on:click={() => filterCards('data')}>Data</button> 
        <button class="key-text carto" on:click={() => filterCards('carto')}>Cartography</button> 
        <button class="key-text interactive" on:click={() => filterCards('interactive')}>Interactive</button> 
        <button class="key-text explainer" on:click={() => filterCards('explainer')}>Explainer</button> 
    </span> 
</div>

<div class="cards">
    {#each projects as proj}
    <div class="card {proj.type}">
        <a href="{proj.url}">
            <div class="img-wrapper">
                <img src="../img/{proj.img}" alt="{proj.name}">
            </div>
            <section class="title-container">
                <div class="legend-container">
                    <Legend type={proj.type}/>
                </div>
                <div class="text-area">
                    <h4>{proj.name}</h4>
                </div>
            </section>
        </a>
        {#if proj.new == 1}
            <div class="new" style="background-image: url('../img/new.svg')">NEW</div>
        {/if}
    </div>
    {/each}
</div>





