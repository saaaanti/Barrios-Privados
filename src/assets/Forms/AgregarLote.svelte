<script>
	import ModalAgregar from "../ModalAgregar.svelte";
	export let cerrar;
	import { _ } from "svelte-i18n";
</script>

<ModalAgregar tabla="lotes" titulo={$_("loteNuevo")} {cerrar}>
	<div slot="formContent" class=" w-full h-full flex gap-8 p-4">
		<div class="flex flex-col">
			<div class="flex flex-col py-4">
				<label for="lote_manz_id">{$_("manzana")}:</label>
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
				<label for="lote_m_frente">{$_("metrosFrente")}</label>
				<input
					class="bg-white rounded-md outline-none px-2"
					type="number"
					name="lote_m_frente"
					required
				/>
			</div>

			<div class="flex flex-col py-4">
				<label for="lote_m_prof">{$_("metrosProfundidad")}</label>
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
				<label for="lote_luz_bool">{$_("loteLuz")}</label>
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
					<label for="lote_luz_bool_true">{$_("Si")}</label>
				</div>
			</div>

			<div class="flex flex-col py-4">
				<label for="lote_agua_bool">{$_("loteAgua")}</label>
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
					<label for="lote_agua_bool_true">{$_("Si")}</label>
				</div>
			</div>
		</div>
		<div class="flex flex-col">
			<div class="flex flex-col py-4">
				<label for="lote_asf_bool">{$_("loteAsf")}</label>
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
					<label for="lote_asf_bool_true">{$_("Si")}</label>
				</div>
			</div>

			<div class="flex flex-col py-4">
				<label for="lote_esq_bool">{$_("loteEsq")}</label>
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
					<label for="lote_esq_bool_true">{$_("Si")}</label>
				</div>
			</div>
		</div>
	</div>
</ModalAgregar>
