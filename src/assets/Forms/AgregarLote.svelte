<script>
	import ModalAgregar from "../ModalAgregar.svelte";
	export let cerrar;
</script>

<ModalAgregar tabla="lotes" titulo={"Agregar un lote nuevo"} {cerrar}>
	<div slot="formContent" class=" w-full h-full flex gap-8 p-4">
		<div class="flex flex-col">
			<div class="flex flex-col py-4">
				<label for="lote_manz_id">Manzana:</label>
				<input
					class="bg-white rounded-md outline-none px-2"
					type="number"
					name="lote_manz_id"
					required
				/>
			</div>

			<!-- <div class="flex flex-col py-4">
			<label for="lote_prop_id">Propietario (TODO)</label>
			<input
				class="bg-white rounded-md outline-none px-2"
				type="number"
				name="lote_prop_id"
			/>
		</div> -->
			<!-- ES UN TODO: RE GORDO TODO ESTO -->

			<div class="flex flex-col py-4">
				<label for="lote_m_frente">Metros de frente</label>
				<input
					class="bg-white rounded-md outline-none px-2"
					type="number"
					name="lote_m_frente"
					required
				/>
			</div>

			<div class="flex flex-col py-4">
				<label for="lote_m_prof">Metros de profundidad</label>
				<input
					class="bg-white rounded-md outline-none px-2"
					type="number"
					name="lote_m_prof"
					required
				/>
			</div>
		</div>

		<div class="flex flex-col">
			<div class="flex flex-col py-4">
				<label for="lote_luz_bool">lote_luz_bool</label>
				<div>
					<input
						type="radio"
						id="lote_luz_bool_false"
						name="lote_luz_bool"
						value={0}
					/>
					<label for="lote_luz_bool_false">No</label>
				</div>
				<div>
					<input
						type="radio"
						id="lote_luz_bool_true"
						name="lote_luz_bool"
						value={1}
					/>
					<label for="lote_luz_bool_true">Si</label>
				</div>
			</div>

			<div class="flex flex-col py-4">
				<label for="lote_agua_bool">lote_agua_bool</label>
				<div>
					<input
						type="radio"
						id="lote_agua_bool_false"
						name="lote_agua_bool"
						value={0}
					/>
					<label for="lote_agua_bool_false">No</label>
				</div>
				<div>
					<input
						type="radio"
						id="lote_agua_bool_true"
						name="lote_agua_bool"
						value={1}
					/>
					<label for="lote_agua_bool_true">Si</label>
				</div>
			</div>
</div>
<div class='flex flex-col'>

			<div class="flex flex-col py-4">
				<label for="lote_asf_bool">lote_asf_bool</label>
				<div>
					<input
						type="radio"
						id="lote_asf_bool_false"
						name="lote_asf_bool"
						value={0}
					/>
					<label for="lote_asf_bool_false">No</label>
				</div>
				<div>
					<input
						type="radio"
						id="lote_asf_bool_true"
						name="lote_asf_bool"
						value={1}
					/>
					<label for="lote_asf_bool_true">Si</label>
				</div>
			</div>

			<div class="flex flex-col py-4">
				<label for="lote_esq_bool">lote_esq_bool</label>
				<div>
					<input
						type="radio"
						id="lote_esq_bool_false"
						name="lote_esq_bool"
						value={0}
					/>
					<label for="lote_esq_bool_false">No</label>
				</div>
				<div>
					<input
						type="radio"
						id="lote_esq_bool_true"
						name="lote_esq_bool"
						value={1}
					/>
					<label for="lote_esq_bool_true">Si</label>
				</div>
</div>
		</div>
	</div>
</ModalAgregar>
