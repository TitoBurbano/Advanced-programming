async function callMessage() {
    try {
        const response = await fetch('http://localhost:8002/hello_ud');
        const data = await response.text();
        document.getElementById('result').textContent = data;
    } catch (error) {
        console.error('Error:', error);
    }
}

async function callWebService() {  //change function name in html
    try {
        const response = await fetch('http://localhost/data');
        const data = await response.json();
        
        let table = '<table>';
        table += '<tr><th>ID</th><th>Name</th><th>Description</th></tr>';
        
        data.forEach(item => {
            table += `<tr><td>${item.id}</td><td>${item.name}</td><td>${item.description}</td></tr>`;
        });
        
        table += '</table>';
        
        document.getElementById('result').innerHTML = table;
    } catch (error) {
        console.error('Error:', error);
    }
}
//Creation of the function showForm and addProduct


async function showForm() {
    const formDiv = document.getElementById('form');
    formDiv.style.display = 'block';
}

async function addProduct() {
    const productIdElement = document.getElementById('productId');
    const nameElement = document.getElementById('name');
    const descriptionElement = document.getElementById('description');

    const id = productIdElement.value;
    const name = nameElement.value;
    const description = descriptionElement.value;

    const product = { id, name, description };

    try {
        const response = await fetch('http://localhost:8002/create_products', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(product),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Clear form and show success message
        productIdElement.value = '';
        nameElement.value = '';
        descriptionElement.value = '';
        alert('Product added successfully');
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to add product');
    }
}


