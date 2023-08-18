<script>
	let editando = false;
	let eliminando = false;
	let agregandoLote = false;
	import EditarPropietario from "../../assets/Forms/EditarPropietario.svelte";
	import PropAgregarLote from "../../assets/Forms/PropAgregarLote.svelte";
	import Modal from "../../assets/Modal.svelte";
	import { dataAhora } from "../../store";
	import { tablasInfo } from "../../store";
	export let params = {};
	import Tabla from "../../assets/Tabla.svelte";
	let idEditando = null;
	import { _ } from "svelte-i18n";
	let dataxd = null;

	const fetchData = async () => {
		console.log("Lmaman data");

		const response = await fetch(
			`http://127.0.0.1:5000/propietarios_lotes/${params.id}`
		);
		const data = await response.json();
		console.log("recibimo,s", data);
		idEditando = data[0][0][0].prop_id;
		dataxd = data;
		dataAhora.set(data);
		return data;
	};

	const enviar = async () => {
		const response = await fetch(
			`http://127.0.0.1:5000/eliminar/propietarios/${$dataAhora[0][0][0].prop_id}`
		);
		const data = response.json();
		data.then((d) => {
			tablasInfo.update((valores) => {
				return {
					...valores,
					propietarios: d,
				};
			});
		});
		window.location.href = "/#/propietarios";
	};

	const fetchConsumos = async () => {
		console.log("Lmaman consumo");
		const response = await fetch(
			`http://127.0.0.1:5000/consumos/${idEditando}`
		);
		const data = await response.json();
		console.log("recibimo,s", data);
		return data;
	};

	let columnasCons = {
		ID: null,
		Lote: "lote",
		"Mes del recibo": "mes",
		Seguridad: "$",
		Luz: "$",
		Agua: "$",
		Gas: "$",
		"Luz Publica": "$",
		"Agua frente": "$",
		Asfalto: "$",
		Cochera: "$",
	};

	let columnasLote = {
		ID: "lote",
		"Fecha de compra": "fecha",
		"Superficie cubierta": "metros",
		Habitantes: null,
		Vehículos: null,
		Luz: "luz",
		Agua: "agua",
		Gas: "gas",
		"": "eliminar",
	};
	const funcElimLote = async (idLote) => {
		const response = await fetch(
			`http://127.0.0.1:5000/prop_vende_lote/${params.id}/${idLote}`
		);
		const data = await response.json();
		dataxd = data;
		dataAhora.set(data);
		return data;
	};
</script>

{#await fetchData()}
	<h1>{$_("cargando")}</h1>
{:then data}
	<div class=" p-4">
		<div class=" bg-slate-500 p-4 rounded-lg flex gap-2">
			<div class="bg-slate-600 p-8 rounded-lg">
				<h1 class="text-2xl font-bold pb-4">{$_("propietario")}</h1>

				<div
					class="flex justify-between bg-slate-700 m-2 p-2 rounded-md w-full"
				>
					<p>ID:</p>
					<p>{$dataAhora[0][0][0].prop_id}</p>
				</div>
				<div
					class="flex justify-between bg-slate-700 m-2 p-2 rounded-md w-full"
				>
					<p>{$_("nombre")}:</p>
					<p>{$dataAhora[0][0][1].prop_nombre}</p>
				</div>
				<div
					class="flex justify-between bg-slate-700 m-2 p-2 rounded-md w-full"
				>
					<p>{$_("apellido")}:</p>
					<p>{$dataAhora[0][0][2].prop_apellido}</p>
				</div>

				<div class="flex items-center justify-center p-2">
					<button
						class="mx-3"
						on:click={() => {
							editando = true;
						}}
					>
						<span
							class="p-2 bg-slate-300 rounded-full text-black material-icons-round"
							>edit</span
						>
					</button>

					<button class="mx-3" on:click={() => (eliminando = true)}
						><span
							class="material-icons-round p-2 bg-red-500 rounded-full text-black"
							>close</span
						></button
					>
				</div>
			</div>
			<div class="flex flex-col gap-2">
				{#await fetchConsumos() then dataCons}
					<div class="bg-slate-600 p-4 rounded-lg">
						<h1 class="text-2xl font-bold">{$_("consumos")}</h1>
						<Tabla columnas={columnasCons} data={dataCons} />
					</div>
				{/await}

				<div class="bg-slate-600 p-4 rounded-lg">
					<div class="flex items-center justify-between">
						<h1 class="text-2xl font-bold">{$_("lotes")}</h1>
						<button
							on:click={() => (agregandoLote = true)}
							class="flex items-center mb-2 p-2 bg-slate-300 text-black rounded-full"
							><span class="material-icons-round">add</span></button
						>
					</div>

					<Tabla
						columnas={columnasLote}
						funcElim={funcElimLote}
						data={$dataAhora[1]}
					/>
				</div>
			</div>
		</div>
	</div>
{/await}
{#if editando}
	<EditarPropietario cerrar={() => (editando = false)} {idEditando} />
{/if}
{#if agregandoLote}
	<PropAgregarLote
		nombre={dataxd[0][0][1].prop_nombre + " " + dataxd[0][0][2].prop_apellido}
		id={idEditando}
		cerrar={() => (agregandoLote = false)}
	/>
{/if}

{#if eliminando}
	<Modal cerrar={() => (eliminando = false)}>
		<div slot="contenido">
			<p>{$_("elimProp")}</p>
			<p>{$_("seguro")}</p>

			<form
				on:submit|preventDefault={enviar}
				class="flex items-center justify-center"
			>
				<button
					class="bg-lime-200 p-2 m-2 rounded-lg"
					on:click={() => (eliminando = false)}
					>{$_("cancelar")}
				</button>

				<button class="bg-red-500 p-2 m-2 font-black rounded-lg" type="submit"
					>{$_("eliminar")}
				</button>
			</form>
		</div>
	</Modal>
{/if}
