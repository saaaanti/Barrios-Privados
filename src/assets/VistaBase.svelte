<script>
	import { tablasInfo } from "../store";
	import CustomTable from "./CustomTable.svelte";
	import Paginas from "./Paginas.svelte";
	import { link } from "svelte-spa-router";

	export let nombre;
	// MUYIMPORANTE EL NOMBRE QUE ES LO QUE USAMOS PARA BUSCAR EN LA API
	export let headers;

	export let columnasCustom;

	export let agregando = false;
	export let editando = false;

	export let usaAgregar = true;
	export let esProp = false;
	export let usaEditar = true;
	export let idEditando;

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
		editando = false;
		agregando = !agregando;
	};

	const funcEditar = (id) => {
		agregando = false;
		editando = !editando;
		idEditando = id;
	};
</script>

<div class="  flex items-center flex-col max-w-full">
	<!-- <div class=" w-fit pt-4 p-2">
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
	</div> -->
	{#if $tablasInfo[nombre] != null}
		<CustomTable {funcAgregar} {usaAgregar}>
			<div class="flex" slot="chips">
				<!-- <slot name="chips" /> -->
				<p class="text-xl font-bold tracking-wide px-2">Viendo los {nombre}</p>
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
							<td class="p-2 text-center align-middle">
								{#if col[Object.keys(col)[0]] == null}
									-
								{:else if columnasCustom}
									{#if row.indexOf(col) in columnasCustom}
										<!-- aca empiezaz -->
										<!-- bool -->
										{#if columnasCustom[row.indexOf(col)] == "bool"}
											{#if col[Object.keys(col)[0]]}
												<span class="material-icons-round text-green-300"
													>done</span
												>
											{:else}
												<span class="material-icons-round text-red-300"
													>close</span
												>
											{/if}
											<!-- propeitario -->
										{:else if columnasCustom[row.indexOf(col)] == "propietario"}
											<a
												href={`/propietarios/${col[Object.keys(col)[1]]}`}
												use:link
												class="flex items-center gap-2 justify-between bg-slate-700 py-1 px-2 rounded-full"
											>
												<p class="text-center w-full">
													{col[Object.keys(col)[0]]}
												</p>
												<span class="material-icons-round">open_in_new</span>
											</a>
										{:else if columnasCustom[row.indexOf(col)] == "plata"}
											${col[Object.keys(col)[0]]
												.toFixed()
												.replace(/\B(?=(\d{3})+(?!\d))/g, ".")}
										{/if}
									{:else}
										{col[Object.keys(col)[0]]}
									{/if}
								{:else}
									{col[Object.keys(col)[0]]}
								{/if}
							</td>
							<!-- TODO: no tener el arbol de elifs que ta feo -->
						{/each}
						{#if esProp}
							<td class="p-2 text-center align-middle">
								<div class="">
									<button
										class=" rounded-full max-h-[32px]
                            p-1 bg-slate-500"
									>
										<a href={`/propietarios/${row["0"]["prop_id"]}`} use:link>
											<span class="material-icons-round"> open_in_new </span>
										</a>
									</button>
								</div>
							</td>
						{:else if usaEditar}
							<td class="p-2 text-center align-middle">
								<div class="">
									<button
										on:click={() => funcEditar(row[0][Object.keys(row[0])[0]])}
										class=" rounded-full max-h-[32px]
                            p-1 bg-slate-500"
									>
										<span class="material-icons-round"> edit </span>
									</button>
								</div>
							</td>
						{/if}
					</tr>
				{/each}
			</div>
		</CustomTable>
		<Paginas />
	{/if}
</div>
{#if agregando}
	<slot name="modalAgregar" />
{:else if editando}
	<slot name="modalEditar" />
{/if}
