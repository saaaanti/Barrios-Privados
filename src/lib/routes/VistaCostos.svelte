<script>
	import VistaBase from "../../assets/VistaBase.svelte";
	import Chip from "../../assets/Chip.svelte";
	import AgregarCostos from "../../assets/Forms/AgregarCostos.svelte";
	let agregando = false;
	let idEditando = null;
	let editando = false;
	import { _ } from "svelte-i18n";
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
		$_("seguridad"),
		$_("luz") + " p/Kw",
		$_("agua") + " p/m3",
		$_("gas") + " p/m3",
		$_("luzPublica"),
		$_("agua"),
		$_("asfalto"),
		$_("cochera") + " p/" + $_("vehiculo"),
		$_("valor") + " p/m2",
		$_("mes"),
	]}
>
	<!-- <div slot="chips">
		<Chip texto="Todos" />
	</div> -->

	<AgregarCostos cerrar={() => (agregando = false)} slot="modalAgregar" />
</VistaBase>
