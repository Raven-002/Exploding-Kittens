document.addEventListener('DOMContentLoaded', () => {
    const appDiv = document.getElementById('app');
    const connectButton = document.getElementById('connectButton');

    appDiv.innerHTML = '<p>Frontend loaded!</p>';

    connectButton.addEventListener('click', async () => {
        try {
            const response = await fetch('/api/connect_server');
            const data = await response.json();
            console.log(data.message);
            appDiv.innerHTML += `<p>${data.message}</p>`;
        } catch (error) {
            console.error('Error connecting to server:', error);
            appDiv.innerHTML += `<p style="color: red;">Error connecting to server.</p>`;
        }
    });
});
