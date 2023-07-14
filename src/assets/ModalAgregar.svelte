<script>
	export let titulo;
	let form;
	const enviar = () => {
		const formData = new FormData(form);

		fetch("http://127.0.0.1:5000/form", {
			method: "POST",

			body: formData,
		});
	};
</script>

<div class="fixed w-full h-full top-0 left-0 p-20">
	<div class="realtive w-full h-full z-20">
		<div class="absolute inset-0 bg-gray-950 opacity-75 z-10" />
		<div
			class="relative bg-slate-400 text-black p-8 top-0 left-0 w-full h-full z-20 rounded-lg"
		>
			<p class="text-lg text-center">{titulo}</p>
			<form
				class="flex flex-col items-center h-full p-2"
				on:submit|preventDefault={enviar}
				id="form"
				bind:this={form}
			>
				<slot name="formContent" />

				<input
					class="bg-lime-400 p-2 rounded-lg"
					type="submit"
					value="Cargar"
				/>
			</form>
		</div>
	</div>
</div>
