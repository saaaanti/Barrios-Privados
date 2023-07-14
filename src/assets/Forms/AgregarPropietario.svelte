<script>
	import ModalAgregar from "../ModalAgregar.svelte";

	let manzana = 1;
	let metrosFrente = "";
	let metrosProfundidad = "";
	let luz = false;
	let agua = false;
	let asfalto = false;
	let esquina = false;
</script>

<ModalAgregar titulo={"Agregar un propietario nuevo"}>
	<div slot="formContent" class="bg-red-500 w-full h-full flex flex-col p-4">
		<label for="manzana" class="text-white mb-2">Manzana:</label>
		<select
			id="manzana"
			class="bg-white text-black rounded p-2 mb-4"
			bind:value={manzana}
		>
			{#each Array.from({ length: 10 }, (_, i) => i + 1) as num}
				<option value={num}>{num}</option>
			{/each}
		</select>

		<label for="metrosFrente" class="text-white mb-2">Metros de frente:</label>
		<input
			type="number"
			id="metrosFrente"
			class="bg-white text-black rounded p-2 mb-4"
			min="0"
			bind:value={metrosFrente}
		/>

		<label for="metrosProfundidad" class="text-white mb-2"
			>Metros de profundidad:</label
		>
		<input
			type="number"
			id="metrosProfundidad"
			class="bg-white text-black rounded p-2 mb-4"
			min="0"
			bind:value={metrosProfundidad}
		/>

		<div class="flex items-center mb-4">
			<input type="checkbox" id="luz" class="mr-2" bind:checked={luz} />
			<label for="luz" class="text-white">Luz</label>
		</div>

		<div class="flex items-center mb-4">
			<input type="checkbox" id="agua" class="mr-2" bind:checked={agua} />
			<label for="agua" class="text-white">Agua</label>
		</div>

		<div class="flex items-center mb-4">
			<input type="checkbox" id="asfalto" class="mr-2" bind:checked={asfalto} />
			<label for="asfalto" class="text-white">Asfalto</label>
		</div>

		<div class="flex items-center mb-4">
			<input type="checkbox" id="esquina" class="mr-2" bind:checked={esquina} />
			<label for="esquina" class="text-white">Esquina</label>
		</div>
	</div>
</ModalAgregar>
