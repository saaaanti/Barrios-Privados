<script>
	import CustomTable from "../../assets/CustomTable.svelte";
	import Paginas from "../../assets/Paginas.svelte";

	const fetchData = (async () => {
		const response = await fetch("http://127.0.0.1:5000/");
		console.log("???", response);

		const a = await response.json();
		console.log("a es ", a);
		return a;
	})();
</script>

<div>
	<h1>VISTA DE LOTES</h1>

	<CustomTable>
		<tr class="">
			<th class="font-bolder px-3 py-2">ID</th>
			<th class="font-bolder px-3 py-2">Manzana</th>
			<th class="font-bolder px-3 py-2">Metros frente</th>
			<th class="font-bolder px-3 py-2">Metros profundidad</th>
			<th class="font-bolder px-3 py-2">Luz</th>
			<th class="font-bolder px-3 py-2">Agua</th>
			<th class="font-bolder px-3 py-2">Asfalto</th>
			<th class="font-bolder px-3 py-2">Esquina</th>
		</tr>
		{#await fetchData}
			<p>CARAGNDOOOOOOAOSDOADOIASD</p>
		{:then datos}
			{#each datos as row}
				<tr class="border-b border-t border-slate-600">
					{#each row as col}
						<td class="py-2 text-center">
							{#if typeof col[Object.keys(col)[0]] == "boolean"}
								{#if col[Object.keys(col)[0]]}
									<span class="material-symbols-outlined text-green-300"
										>done</span
									>
								{:else}
									<span class="material-symbols-outlined text-red-300"
										>close</span
									>
								{/if}
							{:else}
								{col[Object.keys(col)[0]]}
							{/if}
						</td>
					{/each}
				</tr>
			{/each}
		{:catch error}
			<p>Algo salió mal xd {error.message}</p>
		{/await}
	</CustomTable>
	<Paginas />
</div>
