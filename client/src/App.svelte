<script type="ts">
    let rand: string = -1;
    function getRand() {
        fetch("../rand")
            .then((d) => d.text())
            .then((d) => (rand = d));
    }
</script>

<main>
    <h1>Hello {rand}!</h1>
    <button on:click={getRand}>Get a random number</button>
</main>

<style>
    h1 {
        color: red;
    }
</style>
