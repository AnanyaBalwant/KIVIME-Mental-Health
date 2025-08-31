$(document).ready(function() {
    // Toggle chatbot visibility
    $('.chat_icon').click(function() {
        $('.chat_box').toggleClass('active');
    });

    // Initialize chat interface
    let chatBox = $('.chat_box');
    let messageArea = $('<div class="message_area"></div>');
    let inputArea = $('<div class="input_area">' +
        '<input type="text" id="message_input" placeholder="Type your message...">' +
        '<button id="send_button">Send</button>' +
        '</div>');

    // Replace existing content with new chat interface
    chatBox.html('').append(messageArea).append(inputArea);

    // Add welcome message
    addMessage("Hello! I'm your mental health companion. How are you feeling today?", 'bot');

    // Handle send button click
    $('#send_button').click(sendMessage);

    // Handle enter key press
    $('#message_input').keypress(function(e) {
        if(e.which == 13) {
            sendMessage();
        }
    });

    function sendMessage() {
        let input = $('#message_input');
        let message = input.val().trim();
        
        if(message) {
            // Add user message to chat
            addMessage(message, 'user');
            input.val('');

            // Send message to backend
            $.ajax({
                url: '/chat',
                method: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ message: message }),
                success: function(response) {
                    addMessage(response.response, 'bot');
                },
                error: function() {
                    addMessage("I'm having trouble connecting. Please try again.", 'bot');
                }
            });
        }
    }

    function addMessage(message, sender) {
        let messageElement = $('<div class="message ' + sender + '">' +
            '<div class="message_content">' + message + '</div>' +
            '</div>');
        messageArea.append(messageElement);
        messageArea.scrollTop(messageArea[0].scrollHeight);
    }
}); 