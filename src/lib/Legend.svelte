<script>
    export let type = []

    let classes = type.split(" ");
</script>

{#each classes as legCol}
    <span class="legendIcon {legCol}"></span>
     <!-- &#8226; -->
{/each}