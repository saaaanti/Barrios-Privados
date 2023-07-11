<script>
	import { each } from "svelte/internal";
	import CustomTable from "./CustomTable.svelte";
	import Paginas from "./Paginas.svelte";

	export let nombre;
	// MUYIMPORANTE EL NOMBRE QUE ES LO QUE USAMOS PARA BUSCAR EN LA API
	export let headers;

	const fetchData = (async () => {
		const response = await fetch(`http://127.0.0.1:5000/${nombre}`);

		const a = await response.json();

		return a;
	})();
</script>

<div class="  flex items-end flex-col max-w-full">
	<h1 class="py-4 w-full text-xl text-center">Vista de {nombre}</h1>

	<CustomTable>
		<tr class="">
			{#each headers as h}
				<th class="font-bolder px-3 py-2">{h}</th>
			{/each}
		</tr>
		{#await fetchData then datos}
			{#each datos as row}
				<tr class="border-b border-t border-slate-600">
					{#each row as col}
						<td class="p-2 text-center">
							{#if typeof col[Object.keys(col)[0]] == "boolean"}
								{#if col[Object.keys(col)[0]]}
									<span class="material-icons-round text-green-300">done</span>
								{:else}
									<span class="material-icons-round text-red-300">close</span>
								{/if}
							{:else}
								{col[Object.keys(col)[0]]}
							{/if}
						</td>
					{/each}
					<td class="p-2 text-center">
						<div class="">
							<button
								class=" rounded-full max-h-[32px]
                            p-1 bg-slate-500"
							>
								<span class="material-icons-round"> edit </span>
							</button>
						</div>
					</td>
				</tr>
			{/each}
		{:catch error}
			<p>Algo salió mal xd {error.message}</p>
		{/await}
	</CustomTable>
	<Paginas />
</div>
