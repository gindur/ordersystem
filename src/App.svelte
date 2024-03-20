<script>
	import Table from './Table.svelte';
	import Modal from './Modal.svelte';
	import Header from './components/Header.svelte'
	import {onMount} from 'svelte';
	import { fetchOrders } from './order_api';

  	let showModal = false;

	const toggleModal = () => {
		showModal = !showModal;
	}

	const handleSubmit = () => {
		console.log('submitted')
	}

	let orders = [];

  onMount(async () => {
    orders = await fetchOrders();
  });

  
</script>


<Modal {showModal} on:click={toggleModal}>
	<form on:submit|preventDefault={handleSubmit}>
		<input type="text" placeholder="Företagsnamn">
		<input type="email" placeholder="E-post">
		<button>Lägg till</button>
	</form>
</Modal>

<Header />

<main>
	
	<h1>Välkommen till ordermail</h1>
	<p>Nedan kan du se beställningar och lägga in nya beställningar.</p>
	<button on:click={() => toggleModal()}>Skapa order</button>
	<div class="mainTable">
		<Table data={orders} />
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