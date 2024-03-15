<script>
	import Table from './Table.svelte';
	import Modal from './Modal.svelte';

  	let showModal = false;

	const toggleModal = () => {
		showModal = !showModal;
	}

	const handleSubmit = () => {
		console.log('submitted')
	}

	let tableData = [
		{
			id: "1",
			date: "2024-03-14",
			companyName: 'Dygnet runt städ AB',
			email: 'linda.harvigsson@dygnetruntgruppen.se',
			phone: '010-174 73 05',
			name: 'Linda Harvigsson',
			order: 'Nordin 1 44'
		},
		{
			id: "2",
			date: "2024-03-14",
			companyName: 'Collinder märksystem AB',
			email: 'piotr.karaszewski@collinder.se',
			phone: '010-174 73 05',
			name: 'Piotr',
			order: 'Björkom 2- 43'
		}
	];
</script>


<Modal {showModal} on:click={toggleModal}>
	<form on:submit|preventDefault={handleSubmit}>
		<input type="text" placeholder="Företagsnamn">
		<input type="email" placeholder="E-post">
		<button>Lägg till</button>
	</form>
</Modal>
<main>
	<h1>Välkommen till ordermail!</h1>
	<p>Nedan kan du se beställningar och lägga in nya beställningar.</p>
	<button on:click={() => toggleModal()}>Skapa order</button>
	<div class="mainTable">
		<Table data={tableData} />
	</div>
	
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: black;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
	.mainTable{
		align-items: center;
	}
</style>