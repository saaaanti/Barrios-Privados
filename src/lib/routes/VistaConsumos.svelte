<script>
	import VistaBase from "../../assets/VistaBase.svelte";
	import Chip from "../../assets/Chip.svelte";
</script>

<VistaBase
	nombre="consumos"
	headers={[
		"ID",
		"Lote",
		"Propietario",
		"Precios del",
		"Seguridad",
		"Luz",
		"Agua",
		"Gas",
		"Luz publica",
		"Agua por frente",
		"Asfalto por frente",
		"Cochera",
	]}
>
	<div slot="chips">
		<Chip texto="Todos" />
	</div>
</VistaBase>
