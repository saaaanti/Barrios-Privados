<script>
	import VistaBase from "../../assets/VistaBase.svelte";
	import AgregarPropietario from "../../assets/Forms/AgregarPropietario.svelte";
	import Chip from "../../assets/Chip.svelte";

	let agregando = false;
</script>

<VistaBase
	idEditando={null}
	usaAgregar={true}
	esProp={true}
	columnasCustom={null}
	bind:agregando
	nombre="propietarios"
	headers={["ID", "Nombre", "Apellido", "Lotes"]}
>
	<div slot="chips">
		<Chip texto="Todos" />
	</div>
	<AgregarPropietario cerrar={() => (agregando = false)} slot="modalAgregar" />
</VistaBase>
