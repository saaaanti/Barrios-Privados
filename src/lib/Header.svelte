<script>
	export let active = false;
</script>

<header class="bg-slate-800 flex p-5 gap-5 items-center">
	<button
		on:click={() => (active = !active)}
		class="fa-solid fa-bars text-xl bg-red-400 p-1 px-2 rounded-full"
	/>
	<h1 class="text-xl h-min">Administración de Barrios Privados</h1>
</header>
