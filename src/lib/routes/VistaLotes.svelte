<script>
	import VistaBase from "../../assets/VistaBase.svelte";
	import Chip from "../../assets/Chip.svelte";
	import AgregarLote from "../../assets/Forms/AgregarLote.svelte";
	let agregando = false;
</script>

<VistaBase
	bind:agregando
	nombre="lotes"
	headers={[
		"ID",
		"Manzana",
		"Propietario",
		"Metros frente",
		"Metros profundidad",
		"Luz",
		"Agua",
		"Asfalto",
		"Esquina",
	]}
>
	<div slot="chips">
		<Chip texto="Todos" />
	</div>
	<AgregarLote cerrar={() => (agregando = false)} slot="modalAgregar" />
</VistaBase>
