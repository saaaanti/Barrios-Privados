<script>
	import VistaLotes from "./lib/routes/VistaLotes.svelte";
	import VistaDefault from "./lib/routes/VistaDefault.svelte";
	import VistaTest from "./lib/routes/VistaTest.svelte";
	import VistaPropietarios from "./lib/routes/VistaPropietarios.svelte";
	import Header from "./assets/Header.svelte";

	// @ts-ignore
	import Router from "svelte-spa-router";

	let sidebarActive = false;

	const routes = {
		"/": VistaDefault,
		"/lotes": VistaLotes,
		"/propietarios": VistaPropietarios,
		"*": VistaTest,
	};
</script>

<div class="h-full flex flex-col">
	<Header />
	<main class="flex max-w-full h-full">
		<div
			class="flex max-w-full flex-col items-center h-full w-full bg-slate-700"
		>
			<Router {routes} />
		</div>
	</main>
</div>
