<script>
	import { tablasInfo } from "../../store";
	import ModalEditar from "../ModalEditar.svelte";
	export let cerrar;
	export let idEditando;
	import { _ } from "svelte-i18n";

	const fetchData = (async () => {
		const response = await fetch(
			`http://127.0.0.1:5000/uno_solo/lotes/${idEditando}`
		);
		const data = await response.json();
		return data;
	})();

	if ($tablasInfo == null) {
		console.log("Es null y salió todo mal");
	}

	console.log($tablasInfo.propietarios);
</script>

<ModalEditar {cerrar} tabla="propietarios" titulo={$_("editandoLote")}>
	<div slot="formContent">
		{#await fetchData}
			<p>{$_("cargando")}</p>
			<!-- Spinner -->
		{:then data}
			<div class="flex gap-2 bg-red-500">
				<div class="bg-red-400">
					<p>ID</p>
					<p class="text-slate-700">{Object.values(data[0])}</p>
				</div>

				<div class="bg-purple-200">
					<p>{$_("Manzana")}</p>
					<p>{Object.values(data[1])}</p>
				</div>

				<div>
					<p>{$_("propietario")}</p>
					{#if Object.values(data[8])[0] != null}
						<p>{Object.values(data[8])}</p>
					{:else}
						<p>{$_("ninguno")}</p>
					{/if}
					<input type="select" required value={Object.values(data[8])[0]} />
					<!-- TODO: que le pase una lista de los nombres de los propietarios -->
				</div>

				<div>
					<p>{$_("metrosFrente")}</p>
					<p>{Object.values(data[2])}</p>
					<input
						size="6"
						type="number"
						accept=""
						value={Object.values(data[2])}
						required
						min="0"
					/>
				</div>
				<div>
					<p>{$_("metrosProfundidad")}</p>
					<p>{Object.values(data[3])}</p>
					<input
						size="6"
						type="number"
						accept=""
						value={Object.values(data[3])}
						required
						min="0"
					/>
				</div>

				<div>
					<p>{$_("tieneLuz")}</p>
					<p>{Object.values(data[4])}</p>
					<input type="checkbox" />
				</div>

				<div>
					<p>{$_("tieneAgua")}</p>
					<p>{Object.values(data[5])}</p>
					<input type="checkbox" />
				</div>

				<div>
					<p>{$_("tieneAsfalto")}</p>
					<p>{Object.values(data[6])}</p>
					<input type="checkbox" />
				</div>

				<div>
					<p>{$_("tieneEsquina")}</p>
					<p>{Object.values(data[7])}</p>
					<input type="checkbox" />
				</div>

				<!-- Dueño -->

				<!-- {#each data as i}
					<div class="flex bg-purple-300 flex-col p-2">
						<p>
							{Object.values(i)}
						</p>
						<input type="text" name={Object.keys(i)[0]} id="" />
					</div>
				{/each} -->
			</div>
		{/await}
	</div>
</ModalEditar>
