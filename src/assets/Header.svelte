<script>
	// export let active = false;
	import { link } from "svelte-spa-router";
</script>

<header class="bg-slate-800 flex p-5 gap-5 items-center justify-between">
	<!-- <button on:click={() => (active = !active)} class="flex items-center"
		><span class="material-icons-round">menu</span></button
	> -->
	<nav>
		<ul class="flex items-center gap-4">
			<li class="">
				<a
					href="/propietarios"
					use:link
					class="shadow-md bg-slate-600 p-2 rounded-md dra flex items-center"
				>
					<span class="material-icons-round pr-2">people</span> Propietarios
				</a>
			</li>
			<li class="">
				<a
					href="/lotes"
					use:link
					class="shadow-xl dr bg-slate-500 p-2 rounded-md dra flex items-center"
				>
					<span class="material-icons-round pr-2">home</span>Lotes
				</a>
			</li>
			<li class="">
				<a
					href="/pagos"
					use:link
					class="shadow-md bg-slate-600 p-2 rounded-md dra flex items-center"
				>
					<span class="material-icons-round pr-2">receipt_long</span>Pagos
				</a>
			</li>
			<li class="">
				<a
					href="/costos"
					use:link
					class="shadow-md bg-slate-600 p-2 rounded-md dra flex items-center"
				>
					<span class="material-icons-round pr-2">payments</span>Tabla de costos
				</a>
			</li>
		</ul>
	</nav>
	<a href="/" use:link>
		<h1 class="text-xl h-min font-bold font">
			Administración de Barrios Privados
		</h1>
	</a>
</header>
