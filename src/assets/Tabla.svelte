<script>
	export let data;
	export let columnas;
	export let funcElim = null;
	export let funcEdit = null;

	let columnEntries = Object.entries(columnas);
	let columnValues = Object.values(columnas);
</script>

<div class="bg-slate-700 rounded-md">
	<table>
		<thead class="border-b text-center">
			<tr>
				{#each columnEntries as [col, tipo]}
					<th class=" p-2">{col}</th>
				{/each}
			</tr>
		</thead>
		<tbody>
			{#each data as d}
				<tr class="text-center border-t border-t-slate-600">
					{#each d as cell}
						<td class="p-2">
							{#if columnValues[d.indexOf(cell)] === null}
								{Object.values(cell)[0]}
							{:else if columnValues[d.indexOf(cell)] === "lote"}
								l {Object.values(cell)[0]}
							{:else if columnValues[d.indexOf(cell)] === "mes"}
								m {Object.values(cell)[0]}
							{:else if columnValues[d.indexOf(cell)] === "$"}
								$ {Number(Object.values(cell)[0]).toLocaleString()}
							{:else if columnValues[d.indexOf(cell)] === "fecha"}
								f {Object.values(cell)[0]}
							{:else if columnValues[d.indexOf(cell)] === "metros"}
								{Number(Object.values(cell)[0]).toLocaleString()}m2
							{:else if columnValues[d.indexOf(cell)] === "luz"}
								{Number(Object.values(cell)[0]).toLocaleString()}kw
							{:else if columnValues[d.indexOf(cell)] === "agua"}
								{Number(Object.values(cell)[0]).toLocaleString()}m3
							{:else if columnValues[d.indexOf(cell)] === "gas"}
								{Number(Object.values(cell)[0]).toLocaleString()}m3
							{/if}
						</td>
					{/each}

					{#if columnValues.indexOf("editar") !== -1}
						<td>
							<button
								on:click={funcEdit}
								class="flex items-center bg-cyan-700 rounded-full p-1 m-1"
								><span class="material-icons-round">edit</span></button
							>
						</td>
					{:else if columnValues.indexOf("eliminar") !== -1}
						<td>
							<button
								on:click={() => funcElim(Object.values(d[0])[0])}
								class="flex items-center bg-red-500 rounded-full p-1 m-1"
								><span class="material-icons-round">close</span></button
							>
						</td>
					{/if}
				</tr>
			{/each}
		</tbody>
	</table>
</div>
