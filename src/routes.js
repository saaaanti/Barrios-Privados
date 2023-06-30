import VistaLotes from "./lib/views/VistaLotes.svelte"
import VistaDefault from "./lib/views/VistaDefault.svelte"


const routes = [
		{ name: "/", component: VistaDefault },
		{ name: "/lotes", component: VistaLotes },
	];

export {routes}
