document.addEventListener('DOMContentLoaded', () => {
  const searchForm = document.getElementById('search-form') as HTMLFormElement;
  const searchInput = document.getElementById('search-input') as HTMLInputElement;

  if (searchForm && searchInput) {
    searchForm.addEventListener('submit', (event: Event) => {
      event.preventDefault();

      const query = searchInput.value.trim();
      if (query) {
        $.ajax({
          url: `/search/?q=${encodeURIComponent(query)}`,
          method: 'GET',
          dataType: 'json',
          success: (results) => {
            console.log(results); // For demonstration purposes
          },
          error: (xhr, error) => {
            // 오류 처리
            console.error('Error fetching search results:', xhr.status, xhr.responseText, error);
          }
        });
      }
    });
  } else {
    console.error('Search form or input element not found.');
  }
});