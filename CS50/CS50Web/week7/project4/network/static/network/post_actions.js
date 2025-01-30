function getCookie(name) {
    const value = document.cookie.split('; ').find(row => row.startsWith(name));
    return value ? value.split('=')[1] : null;
}

function editPost(id) {
    const textareaValue = document.getElementById(`textarea_${id}`).value;
    const content = document.getElementById(`content_${id}`);
    const modal = document.getElementById(`modal_edit_post_${id}`);
    const successMessage = document.getElementById(`successMessage_${id}`); // Use unique ID for each post


    fetch(`/edit/${id}`, {
        method: "POST",
        headers: { "Content-type": "application/json", "X-CSRFToken": getCookie("csrftoken") },
        body: JSON.stringify({
            text: textareaValue
        })
    })
    .then(response => response.json())
    .then(result => {
        if (result.status === "success") {
            // Update post content
            content.innerHTML = textareaValue;

            // Show success message
            if (successMessage) {
                successMessage.innerHTML = "Change successful";
                successMessage.style.display = "block";

                // Optional: Hide the success message after 3 seconds
                setTimeout(() => {
                    successMessage.style.display = "none";
                }, 1000);
            }

            // Hide the modal after successful edit
            modal.classList.remove('show');
            modal.setAttribute('aria-hidden', 'true');
            modal.style.display = 'none';

            // Remove modal backdrop
            document.querySelectorAll('.modal-backdrop').forEach(backdrop => backdrop.remove());
        }
    });
}
// Function to handle the like/unlike action via AJAX
function toggleLike(postId) {
    const csrfToken = getCookie('csrftoken');  // Dynamically fetch the CSRF token from cookies

    fetch(`/toggle_like/${postId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken  // Use the fetched CSRF token here
        }
    })
    .then(response => response.json())
    .then(data => {
        const likeButton = document.querySelector(`#like-button-${postId}`);
        likeButton.textContent = data.liked ? 'Unlike' : 'Like';
        const likeCount = document.querySelector(`#like-count-${postId}`);
        likeCount.textContent = data.likes + ' Likes';
    })
    .catch(error => console.error('Error:', error));
}
