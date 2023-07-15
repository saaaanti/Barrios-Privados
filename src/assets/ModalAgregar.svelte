<script>
	import { tablasInfo } from "../store";
	export let titulo;
	export let tabla;

	export let cerrar;

	let form;

	const enviar = async () => {
		const formData = new FormData(form);

		fetch(`http://127.0.0.1:5000/cargar/${tabla}`, {
			method: "POST",

			body: formData,
		});

		const response = await fetch(`http://127.0.0.1:5000/${tabla}`);
		const data = response.json();
		data.then((d) => {
			tablasInfo.update((valores) => {
				return {
					...valores,
					[tabla]: d,
				};
			});

			cerrar();
		});
	};
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="fixed w-full h-full top-0 left-0 p-20" on:click={cerrar}>
	<div class=" w-full h-full z-20 flex items-center justify-center">
		<div class="absolute inset-0 bg-gray-950 opacity-75 z-10" />
		<div
			on:click|stopPropagation
			class="relative bg-slate-400 text-black p-8 max-h-full z-20 rounded-lg overflow-auto"
		>
			<p class="text-xl font-bold text-center">{titulo}</p>
			<form
				class="flex flex-col items-center h-full p-2"
				on:submit|preventDefault={enviar}
				id="form"
				bind:this={form}
			>
				<slot name="formContent" />

				<button class="bg-lime-400 p-2 rounded-lg" type="submit"
					>Cargar
				</button>
			</form>
		</div>
	</div>
</div>
