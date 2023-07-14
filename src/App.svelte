<script>
	import VistaLotes from "./lib/routes/VistaLotes.svelte";
	import VistaDefault from "./lib/routes/VistaDefault.svelte";
	import VistaTest from "./lib/routes/Vista404.svelte";
	import VistaPropietarios from "./lib/routes/VistaPropietarios.svelte";
	import Header from "./assets/Header.svelte";

	// @ts-ignore
	import Router from "svelte-spa-router";
	import VistaConsumos from "./lib/routes/VistaConsumos.svelte";
	import VistaCostos from "./lib/routes/VistaCostos.svelte";

	let sidebarActive = false;

	const routes = {
		"/": VistaDefault,
		"/lotes": VistaLotes,
		"/propietarios": VistaPropietarios,
		"/consumos": VistaConsumos,
		"/costos": VistaCostos,
		"*": VistaTest,
	};
</script>

<div class="h-full flex flex-col">
	<Header />
	<main class="flex flex-col max-w-full h-full bg-slate-700">
		<div class="flex max-w-full flex-col items-center h-full w-full">
			<Router {routes} />
		</div>

		<div
			class="bg-slate-800 border-t border-green-400 shadow-inner rounded-t-lg"
		>
			<p class="p-2 text-center font-extralight underline text-slate-300">
				Santiago Piñero Cortez - 2023
			</p>
		</div>
	</main>
</div>
