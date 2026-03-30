<script>
  import { crossfade, fade, fly } from 'svelte/transition';
  import Legend from '../lib/Legend.svelte';
  import { headerMinimised } from './stores';

  export let projects = [];

  function handleImageError(event) {
    event.target.src = '../img/cover.png';
    event.target.classList.add('fallback-image');
  }
</script>



<div class="cards" class:visible={$headerMinimised}>
  {#each projects as proj (proj.name)}
      <div class="card {proj.type}" transition:fade>
        <a href="{proj.url}" target="_blank" rel="noopener noreferrer">
          <div class="img-wrapper">
            <img 
              src="../img/{proj.img}" 
              alt="{proj.name}" 
              loading="lazy"
              on:error={handleImageError}
            />
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


<style>
  a {
    text-decoration: none;
  }


  .title-container {
    padding: 10px 0;
    min-height: 20px;
    display: flex;
    align-items: flex-start;
  }

  h4 {
    color: #000;
    font-size: 18px;
    font-weight: 800;
    line-height: 20px;
    text-decoration: none;
    text-align: left;
    margin: 0;
    padding: 0;
    text-wrap: balance;
  }

  .cards {
    width: calc(100vw - 40px);
    top: 0;
    left: 0;
    margin-top: 9vh;
    position: absolute;
    z-index: -1;
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem 1rem;
    flex-direction: row;
    justify-content: space-between;
    margin: 20px;
    margin-top: 9vh;
    opacity: 0;
    transition: opacity 1s ease-out;
  }

  .cards.visible {
    opacity: 1;
  }

  @media (prefers-reduced-motion: reduce) {
    .cards {
      transition: none;
      opacity: 1;
    }
  }

  .card {
    /* border: 1px solid #000; */
    height: 100%;
    flex-grow: 1;
    max-width: calc((100% / 3) - 1rem);
  }

  @media screen and (max-width: 768px) {
    .card {
      max-width: calc((100% / 2) - 1rem);

    }
  }

  @media screen and (min-width: 1400px) {
    .card {
      max-width: calc((100% / 4) - 1rem);

    }
  }

  .card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .img-wrapper {
    aspect-ratio: 16/9;
    object-fit: cover;
  }

  .fallback-image {
    opacity: 0.6;
    filter: grayscale(0.3);
  }
</style>





