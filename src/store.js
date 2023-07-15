import { writable } from "svelte/store";

export const tablasInfo = writable({
	propietarios: null,
	lotes: null,
	consumos: null,
	costos: null,
});
