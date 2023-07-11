<script>
	function ruedita(e) {
		e.currentTarget.scrollLeft += e.deltaY * 0.3;
	}
</script>

<div class="w-full flex items-center justify-center">
	<div
		class=" scrollbar overflow-x-auto mx-4 max-w-[90%] pb-8 bg-slate-800 rounded-lg shadow-sm"
		on:wheel|preventDefault={ruedita}
	>
		<table class="  transition-all p-8 bg-slate-800">
			<tbody class="">
				<slot />
			</tbody>
		</table>
	</div>
</div>
