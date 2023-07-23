<script>
	export let cerrar;
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="fixed w-full h-full top-0 left-0 p-20" on:click={cerrar}>
	<div class=" w-full h-full z-20 flex items-center justify-center">
		<div class="absolute inset-0 bg-gray-950 opacity-75 z-10" />
		<div
			on:click|stopPropagation
			class="relative bg-slate-400 text-black p-8 max-h-full z-20 rounded-lg overflow-auto"
		>
			<div class=" flex items-center justify-end">
				<button on:click={cerrar}>
					<span
						class=" text-3xl bg-red-500 w-10 h-10 flex items-center justify-center rounded-full -m-4 mb-1 material-icons-round"
						>close</span
					>
				</button>
			</div>
			<slot name="contenido" />
		</div>
	</div>
</div>
