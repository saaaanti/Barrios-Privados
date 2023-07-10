<script>
	import VistaLotes from "./lib/routes/VistaLotes.svelte";
	import VistaDefault from "./lib/routes/VistaDefault.svelte";
	import VistaTest from "./lib/routes/VistaTest.svelte";
	import Header from "./lib/Header.svelte";
	import Sidebar from "./lib/Sidebar.svelte";

	import Router from "svelte-spa-router";
	import { link } from "svelte-spa-router";

	let sidebarActive = false;

	const routes = {
		"/": VistaDefault,
		"/lotes": VistaLotes,
		"*": VistaTest,
	};
</script>

<div class="h-full transition-all">
	<Header bind:active={sidebarActive} />
	<a href="/lotes" use:link>Lotes xd</a>
	<main class="flex max-w-full h-full">
		<Sidebar active={sidebarActive} />

		<div class="w-full">
			<div
				class="flex justify-center flex-col items-center flex- content-center w-full bg-slate-700"
			>
				<h1>Vistas</h1>
				<Router {routes} />
			</div>
		</div>
	</main>
</div>
