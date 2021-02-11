<script lang="ts">
	export let handleKeyPress, score, clickHandler
	let fired = false
	async function handleClick(val) {
		if (fired === true) {
			await new Promise((resolve) => {
				setTimeout(resolve, 150)
			})
		}
		fired = true
		clickHandler(val)
	}
	document.onkeydown = (e) => {
		handleKeyPress(e)
	}
</script>

<main>
	<h1>Chess - RL</h1>
	<p />
	<div class="center_">
		<h4><span id="score">{score}</span></h4>
		<h4><span id="highest_score">{score}</span></h4>
	</div>
	<div class="grid" id="grid" />
</main>

<style>
	.grid {
		display: flex;
		flex-wrap: wrap;
	}
	p {
		margin-top: 0;
	}
	.center_ {
		display: flex;
		padding: 0 10px;
		flex-wrap: wrap;
		width: calc(400px - 20px);
		height: 40px;
		justify-content: space-between;
		margin-bottom: 10px;
	}
</style>
