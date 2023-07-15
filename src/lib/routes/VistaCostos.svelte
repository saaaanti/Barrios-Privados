<script>
	import VistaBase from "../../assets/VistaBase.svelte";
	import Chip from "../../assets/Chip.svelte";
	import AgregarCostos from "../../assets/Forms/AgregarCostos.svelte";
	let agregando = false;
</script>

<VistaBase
	bind:agregando
	nombre="costos"
	headers={[
		"ID",
		"Seguridad",
		"Luz p/Kw",
		"Agua p/m3",
		"Gas p/m3",
		"Luz pública",
		"Agua p/frente",
		"Asfalto p/frente",
		"Cochera p/vehículo",
		"Valor p/m2",
		"Mes",
	]}
>
	<div slot="chips">
		<Chip texto="Todos" />
	</div>

	<AgregarCostos cerrar={() => (agregando = false)} slot="modalAgregar" />
</VistaBase>
