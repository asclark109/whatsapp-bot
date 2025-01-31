import pkg from 'whatsapp-web.js';
const { Client, LocalAuth } = pkg;
import qrcode from 'qrcode-terminal';

const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: { 
        headless: true ,
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-gpu',
            '--disable-dev-shm-usage'
        ]
    }
});

// Track when the client is ready
const clientReadyPromise = new Promise((resolve, reject) => {
    client.on('ready', () => {
        console.log('WhatsApp bot is ready!');
        isClientReady = true;  // Update the readiness state
        resolve();  // Resolve the promise when the client is ready
    });

    client.on('authenticated', () => {
        console.log('Authenticated');
    });

    client.on('auth_failure', () => {
        console.log('Authentication failed');
        reject(new Error('Authentication failed'));
    });

    client.on('qr', (qr) => {
        qrcode.generate(qr, { small: true });
        console.log('Please scan the QR code to authenticate.');
    });
});

client.initialize()

// // Create a writable stream to save messages incrementally
// const writeStream = fs.createWriteStream('chat_history.txt', { flags: 'a' });

// // Function to send a message to the found group
// const sendMessageToGroup = (chat, message) => {
//     chat.sendMessage(message).then(response => {
//         console.log('Message sent successfully:', response);
//     }).catch(err => {
//         console.log('Failed to send message:', err);
//     });
// };
// Function to send a message, but only if the client is ready
const sendMessage = async (chatIDorPhoneID, message) => {
    try {
        await clientReadyPromise;  // Wait for the client to be ready
        const chat = await client.getChatById(chatIDorPhoneID);
        if (chat) {
            await chat.sendMessage(message);
        } else {
            throw new Error('No chat found with this number');
        }
    } catch (error) {
        console.error('Error sending message:', error.message);
    }
};

// // Function to fetch chat history incrementally and write to file
// const fetchChatHistory = async (chat) => {
//     let messageCount = 0;
    
//     const messages = await chat.fetchMessages({
//         limit: 1e4,  // Number of messages per batch
//     });

//     // Write each message immediately to file
//     messages.forEach(msg => {
//         const messageLine = `[${new Date(msg.timestamp * 1000).toISOString()}] ${msg.from}: ${msg.body}\n`;
//         writeStream.write(messageLine);  // Write to file
//         messageCount++;
//     });
//     console.log(`Fetched ${messages.length} messages... Total messages: ${messageCount}`);
// };
// Function to get chat history, but only if the client is ready
const getChatHistory = async (chatIDorPhoneID, limit = 50) => {
    try {
        await clientReadyPromise;  // Wait for the client to be ready
        const chat = await client.getChatById(chatIDorPhoneID);
        if (chat) {
            return chat.fetchMessages({ limit });
        } else {
            throw new Error('No chat found with this number');
        }
    } catch (error) {
        console.error('Error fetching chat history:', error.message);
        return [];
    }
};

const getChatID = async (chatName) => {
    try {
        await clientReadyPromise;  // Wait for the client to be ready
        // Get all chats
        const chats = await client.getChats();

        // Find the chat with the matching group name
        const groupChat = chats.find(chat => chat.name === chatName);

        if (groupChat) {
            // If the group chat is found, log the chatID
            console.log(`Chat ID for "${chatName}": ${groupChat.id._serialized}`);
            return groupChat.id._serialized
        } else {
            throw new Error(`Group chat with name "${chatName}" not found.`);
        }
    } catch (error) {
        console.error('Error fetching chat history:', error.message);
        return null;
    }
};



// client.on('ready', () => {
//     console.log('Client is ready!');
// });

// client.on('authenticated', () => {
//     console.log('Authenticated');
// });

export { sendMessage, getChatHistory, getChatID, clientReadyPromise };