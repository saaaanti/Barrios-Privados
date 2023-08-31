<script>
	// export let active = false;
	import { link } from "svelte-spa-router";
	import { _ } from "svelte-i18n";
	import LanguageChanger from "./LanguageChanger.svelte";
</script>

<header class="bg-slate-800 flex p-5 gap-5 items-center justify-between">
	<!-- <button on:click={() => (active = !active)} class="flex items-center"
		><span class="material-icons-round">menu</span></button
	> -->
	<nav>
		<ul class="flex items-center gap-4">
			<li class="">
				<a
					href="/propietarios"
					use:link
					class="shadow-md bg-slate-600 p-2 rounded-md dra flex items-center"
				>
					<span class="material-icons-round pr-2">people</span>
					{$_("propietarios")}
				</a>
			</li>
			<li class="">
				<a
					href="/lotes"
					use:link
					class="shadow-xl dr bg-slate-500 p-2 rounded-md dra flex items-center"
				>
					<span class="material-icons-round pr-2">home</span>{$_("lotes")}
				</a>
			</li>
			<li class="">
				<a
					href="/consumos"
					use:link
					class="shadow-md bg-slate-600 p-2 rounded-md dra flex items-center"
				>
					<span class="material-icons-round pr-2">receipt_long</span>{$_(
						"consumos"
					)}
				</a>
			</li>
			<li class="">
				<a
					href="/costos"
					use:link
					class="shadow-md bg-slate-600 p-2 rounded-md dra flex items-center"
				>
					<span class="material-icons-round pr-2">payments</span>{$_(
						"tablaCostos"
					)}
				</a>
			</li>
		</ul>
	</nav>
	<div class="flex gap-10 items-center">
		<a href="/" use:link class="">
			<h1 class="text-3xl font-black tracking-tight">
				{$_("barriosPrivados")}
			</h1>
		</a>
		<LanguageChanger />
	</div>
</header>
