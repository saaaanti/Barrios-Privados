<script>
	import VistaBase from "../../assets/VistaBase.svelte";
	import Chip from "../../assets/Chip.svelte";
	import AgregarCostos from "../../assets/Forms/AgregarCostos.svelte";
	let agregando = false;
	let idEditando = null;
</script>

<VistaBase
	{idEditando}
	columnasCustom={{
		1: "plata",
		2: "plata",
		3: "plata",
		4: "plata",
		5: "plata",
		6: "plata",
		7: "plata",
		8: "plata",
		9: "plata",
	}}
	usaAgregar={true}
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
	<!-- <div slot="chips">
		<Chip texto="Todos" />
	</div> -->

	<AgregarCostos cerrar={() => (agregando = false)} slot="modalAgregar" />
</VistaBase>
