document.addEventListener('DOMContentLoaded', function () {
    var searchForm = document.getElementById('search-form');
    var searchInput = document.getElementById('search-input');
    if (searchForm && searchInput) {
        searchForm.addEventListener('submit', function (event) {
            event.preventDefault();
            var query = searchInput.value.trim();
            if (query) {
                $.ajax({
                    url: "/search/?q=".concat(encodeURIComponent(query)),
                    method: 'GET',
                    dataType: 'json',
                    success: function (results) {
                        // Handle successful response
                        console.log(results); // For demonstration purposes
                    },
                    error: function (xhr, status, error) {
                        // Handle errors
                        console.error('Error fetching search results:', status, error);
                    }
                });
            }
        });
    }
    else {
        console.error('Search form or input element not found.');
    }
});
