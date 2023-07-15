<script>
	import ModalAgregar from "../ModalAgregar.svelte";
	export let cerrar;
</script>

<ModalAgregar
	tabla="costos"
	titulo={"Agregar una tabla de precios nueva"}
	{cerrar}
>
	<div slot="formContent" class=" w-full h-full flex flex-col p-4">
		<div class="flex flex-col py-4">
			<label for="cos_seguridad">Seguridad fijo</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="number"
				name="cos_seguridad"
				required
			/>
		</div>

		<div class="flex flex-col py-4">
			<label for="cos_kw">Precio por KW</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="number"
				name="cos_kw"
				required
			/>
		</div>

		<div class="flex flex-col py-4">
			<label for="cos_m3_agua">M3 agua</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="number"
				name="cos_m3_agua"
				required
			/>
		</div>
		<div class="flex flex-col py-4">
			<label for="cos_m3_gas">M3 gas</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="number"
				name="cos_m3_gas"
				required
			/>
		</div>

		<div class="flex flex-col py-4">
			<label for="cos_total_luz">Costo total de la luz</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="number"
				name="cos_total_luz"
				required
			/>
		</div>

		<div class="flex flex-col py-4">
			<label for="cos_mf_agua">Costo de agua por metros de frente</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="number"
				name="cos_mf_agua"
				required
			/>
		</div>

		<div class="flex flex-col py-4">
			<label for="cos_mf_asf">Costo de asfalto por metros de frente</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="number"
				name="cos_mf_asf"
				required
			/>
		</div>

		<div class="flex flex-col py-4">
			<label for="cos_vehiculos">Cochera por vehículo</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="number"
				name="cos_vehiculos"
				required
			/>
		</div>

		<div class="flex flex-col py-4">
			<label for="cos_m2_valor">Precio por m2 de terreno</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="number"
				name="cos_m2_valor"
				required
			/>
		</div>

		<div class="flex flex-col py-4">
			<label for="cos_mes">Mes de estos precios</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="text"
				name="cos_mes"
				required
			/>
		</div>
		<!-- >TODO mes -->
	</div>
</ModalAgregar>
