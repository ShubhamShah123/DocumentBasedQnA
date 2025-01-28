css = '''
<style>
.chat-message {
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 1rem;
    display: flex;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
}

.chat-message.user {
    background-color: #6fb4e9;
    color: black;
    align-items: right;
    text-align: right;
}

.chat-message.bot {
    # background-color: #0e1117;
    color: white;
    align-items: center;
    # box-shadow: 0 8px 16px 0 black;
}

.chat-message .avatar {
    width: 15%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.chat-message .avatar img {
    max-width: 50px;
    max-height: 50px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    width: 85%;
    padding: 0 1rem;
    font-size: 1rem;
    font-family: 'Arial', sans-serif;
}

.chat-message:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}
</style>
'''

bot_template = '''
<div class="chat-message bot"">
    <div class="message">{msg}</div>
</div>
'''

user_template = '''
<div class="chat-message user" >
    <div class="message">{msg}</div>
</div>
'''