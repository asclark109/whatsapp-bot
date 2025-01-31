import express from 'express';
import bodyParser from 'body-parser';
import { sendMessage, getChatHistory, getChatID } from './whatsapp-bot.js';

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Endpoint to send a message
app.post('/send-message', async (req, res) => {
    console.log("request received: /send-message")
    const { phoneIDOrChatID, message } = req.body;
    try {
        // await clientReadyPromise;  // Wait for client to be ready
        await sendMessage(phoneIDOrChatID, message);
        res.status(200).send({ success: true, message: 'Message sent' });
    } catch (error) {
        res.status(500).send({ success: false, error: error.message });
    }
});

// Endpoint to get chat history
app.get('/chat-history', async (req, res) => {
    console.log("request received: /chat-history")
    const { phoneIDOrChatID } = req.query;

    try {
        // await clientReadyPromise;  // Wait for client to be ready
        const messages = await getChatHistory(phoneIDOrChatID, 1e4);
        res.status(200).send({ success: true, data: messages });
    } catch (error) {
        res.status(500).send({ success: false, error: error.message });
    }
});

// Endpoint to get chat id by name
app.get('/chat-id', async (req, res) => {
    console.log("request received: /chat-id")
    const { chatName } = req.query;

    try {
        // await clientReadyPromise;  // Wait for client to be ready
        const chatID = await getChatID(chatName);
        res.status(200).send({ success: true, data: chatID });
    } catch (error) {
        res.status(500).send({ success: false, error: error.message });
    }
});

app.listen(port, () => {
    console.log(`WhatsApp Bot API running on http://localhost:${port}`);
});
