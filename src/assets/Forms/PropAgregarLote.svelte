<script>
	import ModalAgregar from "../ModalAgregar.svelte";
	export let cerrar;
	export let id;
	export let nombre;
	import { _ } from "svelte-i18n";
	const fetchData = (async () => {
		const response = await fetch(`http://127.0.0.1:5000/lotes_libres`);
		const data = await response.json();
		console.log("recibimo,s", data);

		return data;
	})();
</script>

<ModalAgregar
	{cerrar}
	tabla="proplote"
	titulo="Asignar un lote a este propietario"
>
	<div slot="formContent">
		<div class="flex flex-col py-4">
			<label for="pl_prop_id">{$_("propietario")}</label>
			<input
				class="px-2 rounded-md text-white"
				type="text"
				required
				name="pl_prop_id"
				value={id}
				readonly
				id=""
			/>
			<p>{nombre}</p>
		</div>
		{#await fetchData}
			cargando
		{:then data}
			<div class="flex flex-col py-4">
				<label for="pl_lote_id">Lote:</label>
				<select
					class="bg-white rounded-md outline-none px-2"
					name="pl_lote_id"
					required
					size="1"
				>
					{#each data as lote}
						<option value={lote[0].lote_id}>{lote[0].lote_id}</option>
					{/each}
				</select>
			</div>
		{/await}
		<div class="flex flex-col py-4">
			<label for="pl_fecha_compra">{$_("fechaCompra")}:</label>
			<input name="pl_fecha_compra" type="date" required />
		</div>

		<div class="flex flex-col py-4">
			<label for="pl_superficie_cub">{$_("supCubierta")}</label>
			<input
				name="pl_superficie_cub"
				class="text-white"
				required
				type="number"
			/>
		</div>
		<div class="flex flex-col py-4">
			<label for="pl_habitantes"> {$_("supCubierta")} </label>
			<input name="pl_habitantes" class="text-white" required type="number" />
		</div>
		<div class="flex flex-col py-4">
			<label for="pl_vehiculos"> {$_("vehiculos")} </label>
			<input name="pl_vehiculos" class="text-white" required type="number" />
		</div>
		<div class="flex flex-col py-4">
			<label for="pl_cons_luz"> {$_("consLuz")} </label>
			<input name="pl_cons_luz" class="text-white" required type="number" />
		</div>
		<div class="flex flex-col py-4">
			<label for="pl_cons_agua"> {$_("consAgua")} </label>
			<input name="pl_cons_agua" class="text-white" required type="number" />
		</div>
		<div class="flex flex-col py-4">
			<label for="pl_cons_gas"> {$_("consGas")} </label>
			<input name="pl_cons_gas" class="text-white" required type="number" />
		</div>
	</div>
</ModalAgregar>
