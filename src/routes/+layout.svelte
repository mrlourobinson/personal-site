<script>
  import NameHeader from '../lib/NameHeader.svelte';
  import { fade } from 'svelte/transition';
  import { page } from '$app/stores';
  import { pageview } from '../lib/analytics';
  import { afterNavigate } from '$app/navigation';

  // Track page views on navigation
  afterNavigate(() => {
    pageview($page.url.pathname);
  });
</script>

<main>
  
      <NameHeader />

  <section class="content">

    {#key $page.url.pathname}
      <div in:fade={{ duration: 150 }} out:fade={{ duration: 0 }}>
        <slot />
      </div>
    {/key}

  </section>



</main>
<footer>
</footer>

<style>
@import '../app.css';

@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
</style>