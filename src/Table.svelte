<script>
  export let data = [];

  import { Table, Tbody, Thead } from 'svelte-atoms';
  
  let columns = ["Datum", "Företagsnamn", "E-post", "Telefon", "Namn", "Order"]

  const deleteRow = (id) => {
    data = data.filter( (row) => row.id != id)
  }
</script>
<Table hoverable="true">
  <Thead>
    <tr>
      {#each columns as column}
      <th>{column}</th>
      {/each}
    </tr>
  </Thead>
  <Tbody>
    {#each data as {id, date, companyName, email, phone, name, order}}
      <tr>
        <td>{date}</td>
        <td contenteditable="true" >{companyName}</td>
        <td>{email}</td>
        <td>{phone}</td>
        <td>{name}</td>
        <td>{order}</td>
        <td><button on:click={() => deleteRow(id)}>DELETE</button></td>
      </tr>
    {/each}
  </Tbody>
</Table>

<style>

</style>