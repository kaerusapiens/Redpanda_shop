//Product Search
document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    if (searchForm && searchInput) {
        searchForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const query = searchInput.value.trim();
            if (query) {
                fetch(`/search/?q=${encodeURIComponent(query)}`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json'
                    }
                })
                    .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                    .then(results => {
                    console.log(results); // For demonstration purposes
                })
                    .catch(error => {
                    console.error('Error fetching search results:', error);
                });
            }
        });
    }
    else {
        console.error('Search form or input element not found.');
    }
});
