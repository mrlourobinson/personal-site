<script>

    export let name = '';
    export let type = '';
    export let date = '';
    export let img = '';
    export let url = '';
</script>



<div class="square-card">
    <h1>{name}</h1>
    <div class="date">{date}</div>
    <div class="img-wrapper">
        <img src="../img/{img}" alt="{name}" loading="lazy" />
    </div>
    <section class="title-container">
        <div class="text-area">
            <h4>{name}</h4>
        </div>
    </section>
</div>


<style>
    .square-card {
        width: 100%;
        height: 100%;
        background-color: #fff;
        border-radius: 8px;
        padding: 10px;
    }
</style>