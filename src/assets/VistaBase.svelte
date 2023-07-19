<script>
	import { tablasInfo } from "../store";
	import CustomTable from "./CustomTable.svelte";
	import Paginas from "./Paginas.svelte";
	import EditarBase from "./EditarBase.svelte";

	export let nombre;
	// MUYIMPORANTE EL NOMBRE QUE ES LO QUE USAMOS PARA BUSCAR EN LA API
	export let headers;

	export let agregando = false;

	const fetchData = (async () => {
		const response = await fetch(`http://127.0.0.1:5000/${nombre}`);
		const data = await response.json();
		return data;
	})();

	fetchData.then((data) => {
		tablasInfo.update((valores) => {
			return {
				...valores,
				[nombre]: data,
			};
		});
	});

	const funcAgregar = () => {
		agregando = !agregando;
	};
</script>

<div class="  flex items-center flex-col max-w-full">
	<div class=" w-fit pt-4 p-2">
		<div class="flex items-center border bg-slate-800 p-2 rounded-xl">
			<span class="bg-slate-800 material-icons-round">search</span>
			<input
				class="bg-slate-800 border-none pl-2 focus:border-none outline-none active:border-none"
				placeholder="Click para buscar..."
				type="search"
				name={nombre}
				id={nombre}
			/>
		</div>
	</div>
	{#if $tablasInfo[nombre] != null}
		<CustomTable {funcAgregar}>
			<div slot="chips">
				<slot name="chips" />
			</div>

			<div slot="content">
				<tr class="">
					{#each headers as h}
						<th class="font-bolder px-3 py-2">{h}</th>
					{/each}
				</tr>
				{#each $tablasInfo[nombre] as row}
					<tr class="border-b border-t border-slate-600">
						{#each row as col}
							<td class="p-2 text-center">
								{#if typeof col[Object.keys(col)[0]] == "boolean"}
									{#if col[Object.keys(col)[0]]}
										<span class="material-icons-round text-green-300">done</span
										>
									{:else}
										<span class="material-icons-round text-red-300">close</span>
									{/if}
								{:else if col[Object.keys(col)[0]] == null}
									-
								{:else}
									{col[Object.keys(col)[0]]}
								{/if}
							</td>
							<!-- TODO: no tener el arbol de elifs que ta feo -->
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
			</div>
		</CustomTable>
		<Paginas />
	{/if}
</div>
{#if agregando}
	<slot name="modalAgregar" />
{/if}

<EditarBase />
