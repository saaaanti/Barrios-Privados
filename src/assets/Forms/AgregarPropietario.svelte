<script>
	import ModalAgregar from "../ModalAgregar.svelte";
	export let cerrar;
	import { _ } from "svelte-i18n";
</script>

<ModalAgregar tabla="propietarios" titulo={$_("propNuevo")} {cerrar}>
	<div slot="formContent" class="  h-full flex flex-col p-4">
		<div class="flex flex-col py-4">
			<label for="prop_nombre">{$_("Nombre")}:</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="text"
				name="prop_nombre"
				required
			/>
		</div>
		<div class="flex flex-col py-4">
			<label for="prop_apellido">{$_("Apellido")}:</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="text"
				name="prop_apellido"
				required
			/>
		</div>
	</div>
</ModalAgregar>
