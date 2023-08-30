<script>
	let currentLang = "es";

	import { locale, locales } from "svelte-i18n";

	console.log(locale, locales, $locale);

	let switchLang = () => {
		if (currentLang == "es") {
			currentLang = "en";
			$locale = "en";
		} else {
			currentLang = "es";
			$locale = "es";
		}
	};
</script>

<div>
	<button class=" text-white" on:click={switchLang}>
		<p class="material-icons-round">language</p>
		<p>{currentLang}</p>
	</button>
</div>
