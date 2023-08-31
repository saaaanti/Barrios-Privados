<script>
	let currentLang = "🇦🇷";

	import { locale, locales } from "svelte-i18n";
	$locale = "es";

	console.log(locale, locales, $locale);

	let switchLang = () => {
		if ($locale == "es") {
			currentLang = "🇺🇸";
			$locale = "en";
		} else {
			currentLang = "🇦🇷";
			$locale = "es";
		}
	};
</script>

<div>
	<button
		class=" text-white p-0 h-fit flex items-center gap-2 border border-white px-2 rounded-full bg-slate-600"
		on:click={switchLang}
	>
		<p class="material-icons-round text-2xl p-0">language</p>
		<p class="text-2xl p-0">{currentLang}</p>
	</button>
</div>
