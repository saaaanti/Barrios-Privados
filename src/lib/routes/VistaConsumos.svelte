<script>
	import VistaBase from "../../assets/VistaBase.svelte";
	import Chip from "../../assets/Chip.svelte";
</script>

<VistaBase
	idEditando={null}
	columnasCustom={{
		2: "propietario",
		4: "plata",
		5: "plata",
		6: "plata",
		7: "plata",
		8: "plata",
		9: "plata",
		10: "plata",
		11: "plata",
	}}
	usaAgregar={false}
	usaEditar={false}
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
	<!-- <div slot="chips">
		<Chip texto="Todos" />
	</div> -->
</VistaBase>
