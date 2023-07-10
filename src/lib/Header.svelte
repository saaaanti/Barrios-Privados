<script>
	export let active = false;
	import { link } from "svelte-spa-router";
</script>

<header class="bg-slate-800 flex p-5 gap-5 items-center">
	<button on:click={() => (active = !active)} class="flex items-center"
		><span class="material-symbols-outlined">menu</span></button
	>
	<a href="/" use:link>
		<h1 class="text-xl h-min">Administración de Barrios Privados</h1>
	</a>
</header>
