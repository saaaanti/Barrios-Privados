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
	let idEditando = null;

	let dataxd = null;

	const fetchData = (async () => {
		const response = await fetch(
			`http://127.0.0.1:5000/propietarios_lotes/${params.id}`
		);
		const data = await response.json();
		console.log("recibimo,s", data);
		idEditando = data[0][0][0].prop_id;
		dataxd = data;
		dataAhora.set(data);
		return data;
	})();

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
		window.location.href = "/#c";
	};
</script>

{#await fetchData}
	<h1>Cargando flaco esperá un poco</h1>
{:then data}
	<div class=" p-4">
		<div class=" bg-slate-500 p-4 rounded-lg flex gap-2">
			<div class="bg-slate-600 p-8 rounded-lg">
				<h1 class="text-2xl font-bold pb-4">Propietario</h1>

				<div
					class="flex justify-between bg-slate-700 m-2 p-2 rounded-md w-full"
				>
					<p>ID:</p>
					<p>{$dataAhora[0][0][0].prop_id}</p>
				</div>
				<div
					class="flex justify-between bg-slate-700 m-2 p-2 rounded-md w-full"
				>
					<p>Nombre:</p>
					<p>{$dataAhora[0][0][1].prop_nombre}</p>
				</div>
				<div
					class="flex justify-between bg-slate-700 m-2 p-2 rounded-md w-full"
				>
					<p>Apellido:</p>
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
			<!-- TODO: Hacer esto una tablita fachera -->
			<div class="bg-slate-600 p-4 rounded-lg">
				<h1 class="text-2xl font-bold">Lotes</h1>

				<div
					class="flex p-2 bg-red-500 flex-col items-stretch justify-center gap-2"
				>
					<div class="flex justify-between bg-slate-900 gap-2 p-2">
						<p>ID</p>
						<p>Manzana</p>
						<p>Metros de frente</p>
						<p>Metros de profundo</p>
						<p>Luz</p>
						<p>Agua</p>
						<p>Asfalto</p>
						<p>Esquina</p>
						<p>Eliminar</p>
					</div>

					{#each $dataAhora[1] as lote}
						<div
							class="flex justify-between items-center bg-slate-900 gap-2 p-2"
						>
							{#each lote as datoLote}
								<p>
									{datoLote[Object.keys(datoLote)[0]]}
								</p>
							{/each}
							<button
								on:click={() =>
									alert(
										"ELIMINANOD EL LOTE DEL PROPIETARIO PERO TODAVÍA NO LO IMPLENTEMNTRE"
									)}
								class="flex items-center bg-red-500 p-1 rounded-full"
							>
								<span class="material-icons-round">close</span>
							</button>
						</div>
					{/each}
				</div>
				<div class="flex items-center justify-center p-8">
					<button
						on:click={() => (agregandoLote = true)}
						class="flex items-center p-2 bg-slate-300 text-black rounded-full"
						><span class="material-icons-round">add</span></button
					>
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
			<p>Eliminando un propietario</p>
			<p>Está seguro?</p>

			<form
				on:submit|preventDefault={enviar}
				class="flex items-center justify-center"
			>
				<button
					class="bg-lime-200 p-2 m-2 rounded-lg"
					on:click={() => (eliminando = false)}
					>Cancelar
				</button>

				<button class="bg-red-500 p-2 m-2 font-black rounded-lg" type="submit"
					>ELIMINAR
				</button>
			</form>
		</div>
	</Modal>
{/if}
