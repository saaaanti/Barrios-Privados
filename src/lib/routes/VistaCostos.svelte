<script>
	import VistaBase from "../../assets/VistaBase.svelte";
	import Chip from "../../assets/Chip.svelte";
</script>

<VistaBase
	nombre="consumos"
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
		"Mes",
		"Valor p/m2",
	]}
>
	<div slot="chips">
		<Chip texto="hola" />
	</div>
</VistaBase>
