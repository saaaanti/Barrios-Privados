<script>
	import ModalAgregar from "../ModalAgregar.svelte";
	export let cerrar;
</script>

<ModalAgregar
	tabla="propietarios"
	titulo={"Agregar un propietario nuevo"}
	{cerrar}
>
	<div slot="formContent" class="  h-full flex flex-col p-4">
		<div class="flex flex-col py-4">
			<label for="prop_nombre">Nombre:</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="text"
				name="prop_nombre"
				required
			/>
		</div>
		<div class="flex flex-col py-4">
			<label for="prop_apellido">Apellido:</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="text"
				name="prop_apellido"
				required
			/>
		</div>
	</div>
</ModalAgregar>
