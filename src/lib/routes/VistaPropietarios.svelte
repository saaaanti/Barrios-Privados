<script>
	import VistaBase from "../../assets/VistaBase.svelte";
	import AgregarPropietario from "../../assets/Forms/AgregarPropietario.svelte";
	import Chip from "../../assets/Chip.svelte";

	let agregando = false;
	import { _ } from "svelte-i18n";
</script>

<VistaBase
	idEditando={null}
	usaAgregar={true}
	esProp={true}
	columnasCustom={null}
	bind:agregando
	nombre="propietarios"
	headers={["ID", $_("nombre"), $_("apellido"), $_("lotes")]}
>
	<!-- <div slot="chips">
		<Chip texto="Todos" />
	</div> -->
	<AgregarPropietario cerrar={() => (agregando = false)} slot="modalAgregar" />
</VistaBase>
