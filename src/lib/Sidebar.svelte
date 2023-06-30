<script>
	import { fly } from "svelte/transition";

	export let active = false;
</script>

{#if active}
	<aside transition:fly class="h-full bg-red-100 text-black">
		<h1 class="text-3xl">SIDEBAR MEGAFACHER</h1>
		<hr />
		<ul class="list-inside">
			<hr />

			<li>
				<h2>Lotes</h2>
				<ul>
					<li>Consulta</li>
					<li>Carga</li>
				</ul>
			</li>
			<hr />
			<li>Propietarios</li>
			<hr />
			<li>Consumos</li>
			<hr />
			<li>Costos</li>
		</ul>
	</aside>
{/if}
