export async function fetchOrders() {
    try {
        const response = await fetch('http://localhost:3000/api/orders');
        if (!response.ok) {
            throw new Error('Failed to fetch orders')
        }
        const data = await response.json();
        console.log('Fetched orders:', data);  // Log the fetched data
        return data;
    } catch (error) {
        console.log('Error fetching orders:', error)
        return [];
    }
}