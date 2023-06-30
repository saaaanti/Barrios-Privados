<script>
	import VistaLotes from "./lib/views/VistaLotes.svelte";
	import Header from "./lib/Header.svelte";
	import Sidebar from "./lib/Sidebar.svelte";
	import { Router } from "svelte-router-spa";
	import { routes } from "./routes.js";

	const fetchImage = (async () => {
		const response = await fetch("http://127.0.0.1:5000/");
		console.log("???", response);

		const a = await response.json();
		console.log("a es ", a);
		return a;
	})();

	let sidebarActive = false;
</script>

<div class="h-full transition-all">
	<Header bind:active={sidebarActive} />
	<main class="flex max-w-full h-full">
		<Sidebar active={sidebarActive} />

		<div class="w-full">
			{#await fetchImage}
				<p>CARGANDOOO</p>
			{:then data}
				<div
					class="flex justify-center flex-col items-center flex- content-center w-full bg-slate-700"
				>
					<h1>Vistas</h1>
					<div>
						<Router {routes} {data} />
						<VistaLotes datos={data} />
					</div>
				</div>
			{/await}
		</div>
	</main>
</div>
