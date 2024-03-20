<script>
  import { Table, Tbody, Thead } from 'svelte-atoms';
  
  export let data = [];
  $: reversedData = [...data].reverse()
  let columns = ["Datum", "Företagsnamn", "E-post", "Telefon", "Namn", "Order"]

  const deleteRow = (id) => {
    data = data.filter( (row) => row.order_id != id)
  }
  
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
    {#each reversedData as order (order.order_id)}
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