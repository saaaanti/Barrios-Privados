<script>
	import { tablasInfo } from "../store";
	import Modal from "./Modal.svelte";
	export let titulo;
	export let tabla;

	export let cerrar;

	let form;
	import { _ } from "svelte-i18n";

	const enviar = async () => {
		const formData = new FormData(form);
		console.log("fechiando a ", `http://127.0.0.1:5000/cargar/${tabla}`);
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

<Modal {cerrar}>
	<div slot="contenido">
		<p class="text-xl font-bold text-center">{titulo}</p>
		<form
			class="flex flex-col items-center h-full p-2"
			on:submit|preventDefault={enviar}
			id="form"
			bind:this={form}
		>
			<slot name="formContent" />

			<button class="bg-lime-400 p-2 rounded-lg" type="submit"
				>{$_("cargar")}
			</button>
		</form>
	</div>
</Modal>
