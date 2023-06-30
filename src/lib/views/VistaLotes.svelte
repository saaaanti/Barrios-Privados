<script>
	export let datos;
</script>

<table class="border-2 transition-all p-8 max-w-[330px] border-red-300">
	<tr>
		<th class="px-2 border-2 border-black">ID</th>
		<th class="px-2 border-2 border-black">Nombre</th>
		<th class="px-2 border-2 border-black">Apellido</th>
		<th class="px-2 border-2 border-black">ID Lote</th>
		<th class="px-2 border-2 border-black">Fecha compra</th>
		<th class="px-2 border-2 border-black">Superficie cubierta</th>
		<th class="px-2 border-2 border-black">Habitantes</th>
		<th class="px-2 border-2 border-black">Vehículos</th>
		<th class="px-2 border-2 border-black">Consumo luz</th>
		<th class="px-2 border-2 border-black">Consumo agua</th>
		<th class="px-2 border-2 border-black">Consumo gas</th>
	</tr>

	{#each datos as row}
		<tr class="border-2 border-green-400">
			{#each row as col}
				<td class="border-x-2 border-gray-900">{col[Object.keys(col)[0]]}</td>
			{/each}
		</tr>
	{/each}
</table>
