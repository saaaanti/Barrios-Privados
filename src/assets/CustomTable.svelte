<script>
	import { mesTrabajando } from "../store";
	import { tablasInfo } from "../store";

	let funcActualizar = async () => {
		const response = await fetch(
			`http://127.0.0.1:5000/actualizar/${$mesTrabajando}`
		);
		const data = await response.json();
		tablasInfo.update((valores) => {
			return {
				...valores,
				["consumos"]: data,
			};
		});
		return data;
	};

	function ruedita(e) {
		e.currentTarget.scrollLeft += e.deltaY * 0.3;
	}
	export let funcAgregar;

	export let usaAgregar;
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

			{#if usaAgregar}
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
			{:else}
				<div class="flex items-center gap-3 text-black">
					<!-- TODO: MES -->
					<p class="text-white">Con precios del:</p>
					<input class="text-white" bind:value={$mesTrabajando} type="month" />

					<p
						class="bg-amber-500 pl-2 rounded-l-md shadow-sm -mr-4 after:w-full after:px-2"
					>
						Actualizar
					</p>
					<button
						on:click={funcActualizar}
						class="bg-amber-500 -mr-4 -my-10 rounded-full flex items-center p-5 drop-shadow-2xl text-black font-black hover:bg-amber-300 transition-all"
					>
						<span class="material-icons-round">update</span>
					</button>
				</div>
			{/if}
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
