<script>
    import { page } from "$app/stores";
    import { headerMinimised } from "./stores";

    let name = "Lou Robinson";
    let start_delay = 0.5;
    let fade_duration = 0.05;
    let name_array = name.split("");
    name_array = name_array.map((letter) => (letter === " " ? "&nbsp;" : letter));
    let title = "Designer and visual journalist";
    let title_array = title.split("");
    title_array = title_array.map((letter) => (letter === " " ? "&nbsp;" : letter));

    for (let i = 0; i < name_array.length; i++) {
        name_array[i] = { letter: name_array[i], delay: start_delay + i * fade_duration };
    }

    let animation_duration = name_array[name_array.length - 1].delay;
    let header_state = "maximised";
    let title_visible = false;
    let link_visible = false;

    $: about = $page.url.pathname.includes("about");

    function handleNameAnimationEnd() {
        title_visible = true;
    }

    function handleTitleTransitionEnd() {
        setTimeout(() => {
            header_state = "minimised";
            link_visible = true;
            headerMinimised.set(true);
        }, 1000);
    }
    
</script>

<div class="header-container {header_state}">
    <header>
        <section class="titles">
            <span class="top-item name">
                {#each name_array as letter, index}
                    {#if index === name_array.length - 1}
                        <span class="letter" style="animation-delay: {letter.delay}s;" on:animationend={handleNameAnimationEnd}>{@html letter.letter}</span>
                    {:else}
                        <span class="letter" style="animation-delay: {letter.delay}s;">{@html letter.letter}</span>
                    {/if}
                {/each}
            </span>

            <span class="top-item title" class:visible={title_visible} on:transitionend={handleTitleTransitionEnd}>
                {#each title_array as letter, index}
                    <span class="letter" >{@html letter}</span>
                {/each}
            </span>

            <section class="links">
                {#if about}
                    <span class="top-item link" class:visible={link_visible} id="work">
                        <a href="/">Work</a>
                    </span>
                {:else}
                    <span class="top-item link" class:visible={link_visible} id="about">
                        <a href="/about">About</a>
                    </span>
                {/if}
            </section>
        </section>
    </header>
</div>





<style lang="scss">
    .letter {
        display: inline-block;
        animation: bounce 0.5s ease-in-out forwards;
        opacity: 0;
    }

    @keyframes bounce {
        0% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-10px);
            opacity: 1;
        }
        100% {
            transform: translateY(0);
            opacity: 1;
        }
    }

    .title {
        transition: opacity 1s ease-in;
        opacity: 0;
    }

    .header-container {
        scrollbar-gutter: stable;
        width: calc(100vw - 40px);
        max-width: 100%;
        height: calc(100% - 40px);
        top: 0;
        left: 0;
        position: fixed;
        display: flex;
        justify-content: center;
        align-items: center;
        // background-color: rgb(0, 189, 189);
        margin: 20px;

        transition: all 0.6s ease-in-out;
    }

    header {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        background-color: rgba(219, 219, 219, 0.8);
        backdrop-filter: blur(5px);
        color: #212121;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .header-container.maximised {
        border-radius: 5px;
    }

    .header-container.minimised {
            height: 6lvh;
            width: 100%;
            border-radius: 0 !important;
            min-height: 70px;
            margin: 0;


            header .titles {
                padding: 0 20px;
            }
            

            header .name {
                font-size: 24px !important;
            }

            header .title {
                font-size: 14px !important;
            }
        }

    .titles {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        padding: 0 20px;
    }

    .name {
        font-family: "Gasoek One", sans-serif;
        font-size: 50px;
        font-weight: 800;
        letter-spacing: 0;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: all 0.5s ease-in-out;
    }

    .name:hover {
        letter-spacing: 0px;
    }

    .title {
        font-family: "Public Sans", sans-serif;
        font-size: 20px;
        font-weight: 400;
        width: 100%;
        justify-content: center;
        align-items: center;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: all 0.5s ease-in-out;
        opacity: 0;
    }

    .title.visible {
        opacity: 1;
    }

    .link {
        font-size: 14px;
        position: absolute;
        bottom: 35%;
        right: 20px;
        color: #212121;
        opacity: 0;
        transition: all 0.5s ease-in-out;

        a {
            color: #212121;
            text-decoration: none;
        }

        a:hover {
            font-weight: 600;
        }
    }

    .link.visible {
        opacity: 1;
    }

    @media (prefers-reduced-motion: reduce) {
        .letter {
            animation: none;
            opacity: 1;
        }
        
        .title, .link {
            transition: none;
            opacity: 1;
        }
        
        .header-container {
            transition: none;
        }
    }
</style>
