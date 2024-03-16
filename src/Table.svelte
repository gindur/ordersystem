<script>
  export let data = [];

  import { Table, Tbody, Thead } from 'svelte-atoms';
  
  let columns = ["Datum", "Företagsnamn", "E-post", "Telefon", "Namn", "Order"]

  const deleteRow = (id) => {
    data = data.filter( (row) => row.id != id)
  }
  $: data.forEach(order => console.log(order.email_address));
  
</script>
<Table >
  <Thead>
    <tr>
      {#each columns as column}
      <th>{column}</th>
      {/each}
    </tr>
  </Thead>
  <Tbody>
    {#each data.reverse() as order}
      <tr>
        <td>{order.order_id}</td>
        <td contenteditable="true" >{order.company_name}</td>
        <td type>{order.email_address}</td>
        <td>{order.phonenumber}</td>
        <td>{order.firstname +" " + order.lastname}</td>
        <td>{order.total_paid}</td>
        <td><button on:click={() => deleteRow(order.order_id)}>DELETE</button></td>
      </tr>
    {/each}
  </Tbody>
</Table>

<style>

</style>