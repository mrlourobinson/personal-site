<script>
    export let type = []

    let classes = type.split(" ");
</script>

{#each classes as legCol}
    <span class="legendIcon {legCol}">&#8226;</span>
{/each}