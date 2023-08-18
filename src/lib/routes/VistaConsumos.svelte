<script>
	import VistaBase from "../../assets/VistaBase.svelte";
	import Chip from "../../assets/Chip.svelte";
	import { _ } from "svelte-i18n";
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
		$_("lote"),
		$_("propietario"),
		$_("preciosDel"),
		$_("seguridad"),
		$_("electricidad"),
		$_("agua"),
		$_("gas"),
		$_("luzPublica"),
		$_("aguaPFrente"),
		$_("asfPFrente"),
		$_("cochera"),
	]}
>
	<!-- <div slot="chips">
		<Chip texto="Todos" />
	</div> -->
</VistaBase>
