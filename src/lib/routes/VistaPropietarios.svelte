<script>
	import VistaBase from "../../assets/VistaBase.svelte";
	import AgregarPropietario from "../../assets/Forms/AgregarPropietario.svelte";
</script>

<VistaBase
	nombre="propietarios"
	headers={[
		"ID",
		"Nombre",
		"Apellido",
		"Lote",
		"Fecha de compra",
		"Superficie cubierta",
		"Habitantes",
		"Vehículos",
		"Consumo de luz",
		"Consumo de agua",
		"Consumo de gas",
	]}
>
	<AgregarPropietario slot="modalAgregar" />
</VistaBase>
