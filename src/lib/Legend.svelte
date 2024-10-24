<script>
    export let type = []

    let classes = type.split(" ");
</script>

{#each classes as legCol}
    <div class="legendIcon {legCol}">&#8226;</div>
{/each}