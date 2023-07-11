<script>
	import { link } from "svelte-spa-router";
	import { fly } from "svelte/transition";

	export let ruta;
	export let texto;

	let expanded = false;
</script>

<li class="py-1">
	<div class="flex items-center">
		<a href={ruta} use:link class=" ">
			<p class="h-full flex justify-center items-center">{texto}</p>
		</a>
		<button
			class="flex ml-3 w-full items-center justify-end"
			on:click={() => (expanded = !expanded)}
		>
			<span class="material-icons-round text-red">chevron_right</span>
		</button>
	</div>

	{#if expanded}
		<ul class="pl-4 pt-1 text-slate-600 flex flex-col">
			<a href={ruta + "/consulta"} class="py-1">Consulta</a>
			<a href={ruta + "/carga"} class="py-1">Carga</a>
		</ul>
	{/if}
</li>
