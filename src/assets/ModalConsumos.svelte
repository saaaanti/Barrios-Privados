<script>
	import Modal from "./Modal.svelte";
	import { _ } from "svelte-i18n";
	import Tabla from "./Tabla.svelte";
	export let cerrar;
	export let id;
	const fetchConsumos = async () => {
		console.log("Lmaman consumo");
		const response = await fetch(`http://127.0.0.1:5000/consumos/${id}`);
		const data = await response.json();
		console.log("recibimo,s", data);
		return data;
	};

	let columnasCons = {
		id: null,
		lote: "lote",
		mes: "mes",
		seguridad: "$",
		luz: "$",
		agua: "$",
		gas: "$",
		luzPublica: "$",
		aguaPFrente: "$",
		asfalto: "$",
		cochera: "$",
	};
</script>

<Modal {cerrar}>
	<div slot="contenido">
		<div class="bg-slate-600 p-4 rounded-lg text-white">
			<div class="flex items-center text-black justify-between">
				<h1 class="text-2xl font-bold">{$_("consumos")}</h1>
			</div>
			{#await fetchConsumos()}
				<h1>{$_("cargando")}</h1>
			{:then dataCons}
				<Tabla columnas={columnasCons} data={dataCons} />
			{/await}
		</div>
	</div>
</Modal>
