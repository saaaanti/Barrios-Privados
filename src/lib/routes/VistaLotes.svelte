<script>
	import VistaBase from "../../assets/VistaBase.svelte";
	import Chip from "../../assets/Chip.svelte";
	import AgregarLote from "../../assets/Forms/AgregarLote.svelte";
	import EditarLote from "../../assets/Forms/EditarLote.svelte";
	let agregando = false;
	let editando = false;
	let idEditando = 1;
	import { _ } from "svelte-i18n";
</script>

<VistaBase
	columnasCustom={{
		2: "propietario",
		5: "bool",
		6: "bool",
		7: "bool",
		8: "bool",
	}}
	usaAgregar={true}
	bind:agregando
	bind:editando
	bind:idEditando
	nombre="lotes"
	headers={[
		"ID",
		$_("manzana"),
		$_("propietario"),
		$_("metrosFrente"),
		$_("metrosProfundidad"),
		$_("electricidad"),
		$_("agua"),
		$_("asfalto"),
		$_("esquina"),
	]}
>
	<!-- <div slot="chips">
		<Chip texto="Todos" />
	</div> -->
	<EditarLote
		{idEditando}
		cerrar={() => (editando = false)}
		slot="modalEditar"
	/>
	<AgregarLote cerrar={() => (agregando = false)} slot="modalAgregar" />
</VistaBase>
