// ==================== CHATBOT JS =====================

const messagesList = document.querySelector('.messages-list');
const messageForm = document.querySelector('.message-form');
const messageInput = document.querySelector('.message-input');

// upon submission of send button...
messageForm.addEventListener('submit', (event)=> {
    event.preventDefault() // prevent refresh of page on click
    
    const message = messageInput.value.trim();
    if (message.length === 0){
    return;
    }

    const messageItem = document.createElement('li');
    messageItem.classList.add('message','sent');
    messageItem.innerHTML = ` 
        <div class="message-text">
        <div class="message-sender">
            <b>Vous</b>
        </div>
        <div class="message-content">
            ${message}
        </div>
        </div>
    `;
    messagesList.appendChild(messageItem);

    //clear from input box  
    messageInput.value = '';

    //send data to backend
    fetch("{% url 'send_message' %}", {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
        'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        'user_message': message
    })
    })
    .then(response => response.json())
    .then(data => {
        const response = data.response;
        const messageItem = document.createElement('li');
        messageItem.classList.add('message', 'received');
        messageItem.innerHTML = `
        <div class="message-text">
            <div class="message-sender">
            <b>Chatbot</b>
            </div>
            <div class="message-content">
                ${response}
            </div>
        </div>
        `;
        messagesList.appendChild(messageItem);
    });
});
