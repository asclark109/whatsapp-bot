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

clientReadyPromise.catch((error) => {
    console.error("Error in client ready promise:", error);
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
        console.info("Waiting for client to be ready...");
        await clientReadyPromise;  // Wait for the client to be ready
        console.info("Client is ready.");
        const chat = await client.getChatById(chatIDorPhoneID);
        console.info("found chat for id="+chatIDorPhoneID)
        if (chat) {
            const messages = chat.fetchMessages({ limit });
            console.info("Fetched messages:", messages.length);
            return messages;
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


const getContactsByIds = async (ids) => {
    try {
        await clientReadyPromise;  // Wait for the client to be ready
        const contacts = [];

        // Loop through each ID in the provided array
        for (let id of ids) {
            console.log("requesting information on "+id)
            const contact = await client.getContactById(id);
            if (contact) {
                contacts.push(contact);
                console.log(`Found contact for ID "${id}": ${contact.name}`);
            } else {
                console.log(`No contact found for ID "${id}"`);
            }
        }

        // Return the list of contact objects
        return contacts;
    } catch (error) {
        console.error('Error fetching contacts:', error.message);
        return [];
    }
};


export { sendMessage, getChatHistory, getChatID, getContactsByIds, clientReadyPromise };