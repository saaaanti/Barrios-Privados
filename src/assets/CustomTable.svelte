<script>
	function ruedita(e) {
		e.currentTarget.scrollLeft += e.deltaY * 0.3;
	}
	export let funcAgregar;
</script>

<div class="w-full flex items-center flex-col justify-center">
	<!-- Header de la tabla -->
	<div class="p-4 px-8 w-full shadow-sm">
		<div
			class="bg-slate-500 p-2 rounded-lg flex gap-3 justify-between items-center"
		>
			<div>
				<slot name="chips" />
			</div>

			<div class="flex items-center gap-3 text-black">
				<p
					class="bg-green-500 pl-2 rounded-l-md shadow-sm -mr-4 after:w-full after:px-2"
				>
					Agregar
				</p>
				<button
					on:click={funcAgregar}
					class="bg-green-500 -mr-4 -my-10 rounded-full flex items-center p-5 drop-shadow-2xl text-black font-black hover:bg-green-300 transition-all"
				>
					<span class="material-icons-round">add</span>
				</button>
			</div>
		</div>
	</div>

	<!-- Contenido de la tabla -->
	<div class="w-full flex items-center justify-center">
		<div
			class=" scrollbar overflow-x-auto mx-8 max-w-full pb-8 bg-slate-800 rounded-lg shadow-sm"
			on:wheel|preventDefault={ruedita}
		>
			<table class="  transition-all p-8 bg-slate-800">
				<tbody class="">
					<slot name="content" />
				</tbody>
				<!-- TODO: Los editores mejor puestos -->
			</table>
		</div>
	</div>
</div>
