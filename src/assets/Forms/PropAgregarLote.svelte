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

<ModalAgregar {cerrar} tabla="proploteventa" titulo={$_("asignarLote")}>
	<div slot="formContent" class="text-white">
		<div class="flex flex-col py-4">
			<label for="plv_prop_id">{$_("propietario")}</label>
			<input
				class="px-2 rounded-md text-white"
				type="text"
				required
				name="plv_prop_id"
				value={id}
				readonly
				id=""
			/>
			<p>{nombre}</p>
		</div>

		<div class="flex flex-col py-4">
			<label for="plv_lote_id">{$_("lote")}</label>
			{#await fetchData}
				cargando
			{:then data}
				<select
					class="bg-white text-black rounded-md outline-none px-2"
					name="plv_lote_id"
					required
					size="1"
				>
					{#each data as lote}
						<option value={lote[0].lote_id}>{lote[0].lote_id}</option>
					{/each}
				</select>
			{/await}
		</div>

		<div class="flex flex-col py-4">
			<label for="plv_fecha_compra">{$_("fechaCompra")}:</label>
			<input name="plv_fecha_compra" type="date" required />
		</div>
	</div>
</ModalAgregar>
