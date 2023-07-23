<script>
	import { tablasInfo } from "../../store";
	import ModalEditar from "../ModalEditar.svelte";
	export let cerrar;
	export let idEditando;

	const fetchData = (async () => {
		const response = await fetch(
			`http://127.0.0.1:5000/uno_solo/propietarios/${idEditando}`
		);
		const data = await response.json();

		return data;
	})();

	if ($tablasInfo == null) {
		alert(
			`Es null y salió todo mal, creo que tendríasque abrir la tabla ${"propietarios"} primero`
		);
	}
</script>

<ModalEditar {cerrar} tabla={"propietarios"} titulo={"Editar un propietario"}>
	<div slot="formContent" class=" w-full h-full flex flex-col p-4">
		{#await fetchData then data}
			<div class="flex flex-col py-4">
				<label for="prop_id">ID:</label>
				<input
					class="text-white px-2 rounded-md"
					type="text"
					name="prop_id"
					value={data[0].prop_id}
					readonly
				/>
			</div>

			<div class="flex flex-col py-4">
				<label for="prop_nombre">Nombre:</label>
				<input
					class="bg-white rounded-md outline-none px-2"
					type="text"
					name="prop_nombre"
					required
					value={data[1].prop_nombre}
				/>
			</div>
			<div class="flex flex-col py-4">
				<label for="prop_apellido">Apellido:</label>
				<input
					class="bg-white rounded-md outline-none px-2"
					type="text"
					name="prop_apellido"
					required
					value={data[2].prop_apellido}
				/>
			</div>
		{/await}
	</div>
</ModalEditar>
