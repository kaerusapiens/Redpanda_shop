
document.addEventListener('DOMContentLoaded', function() {
  const updateButtons = document.querySelectorAll('.cart-update-btn');
  updateButtons.forEach(button => {
      button.addEventListener('click', function() {
            const pk = this.getAttribute('data-pk');
            const quantityInput = document.querySelector(`input[data-pk="${pk}"]`);
            const quantity = quantityInput.value;
            console.log(pk)
            console.log(quantityInput)
            console.log(quantity)
            fetch(`/cart/update/${pk}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ 
                    'quantity': quantity })
            })
            .then(response => response.json())
            .then(data => {
                console.log('Server Response:', data);
                //IF response was success
                if (data.success) {
                    const subtotalElement = document.getElementById(`subtotal-${pk}`);
                    const totalElement = document.getElementById('total');
                    subtotalElement.textContent = `¥　${data.subtotal}`;
                    totalElement.textContent = `合計 - ¥${data.total}`;
                //Catch error
                } else {
                    console.error('Update failed:', data.error);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
    });

// Function to get CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}