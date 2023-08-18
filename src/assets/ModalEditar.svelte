<script>
	import Modal from "./Modal.svelte";
	import { tablasInfo } from "../store";
	import { dataAhora } from "../store";

	export let titulo;
	export let tabla;
	export let cerrar;
	import { _ } from "svelte-i18n";

	let form;

	const enviar = async () => {
		const formData = new FormData(form);
		console.log(form);
		console.log(formData);

		fetch(`http://127.0.0.1:5000/editar/${tabla}`, {
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
	// ESTO LO COPIAMOS PERO PONELE QUE TRANQUI
	// LO PODRÍAMOS ELEVAR A Modal.SVELTE PERO FUE
</script>

<Modal {cerrar}>
	<div slot="contenido">
		<p>{titulo}</p>

		<form on:submit|preventDefault={enviar} id="form" bind:this={form}>
			<slot name="formContent" />
			<button class="bg-lime-400 p-2 rounded-lg" type="submit"
				>{$_("cargar")}
			</button>
		</form>
	</div>
</Modal>
