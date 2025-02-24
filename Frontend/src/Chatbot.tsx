import React, { useState } from 'react';

interface Message {
  role: 'user' | 'assistant' | 'system';
  content: string;
}

// The hidden system prompt (never displayed in the chat)
const SYSTEM_MESSAGE: Message = {
  role: 'system',
  content:
    'You are a friendly Salon-AI secretary and assistant capable of taking appointments, providing hairstyle recommendations, and answering related inquiries in a polite and helpful manner.',
};

const Chatbot: React.FC = () => {
  // Only store user and assistant messages for display
  const [chatMessages, setChatMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage: Message = { role: 'user', content: input };

    // Prepare request messages (includes system prompt but not shown in UI)
    const requestMessages: Message = [
      SYSTEM_MESSAGE,
      ...chatMessages,
      userMessage,
    ];

    // Add the user's message to the chat UI
    const updatedChat: Message[] = [...chatMessages, { role: 'user', content: input }];
    setChatMessages(updatedChat);

    try {
      const response = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization:
            'Bearer YOUR_KEY_HERE', // Replace with your OpenAI API key
        },
        body: JSON.stringify({
          model: 'gpt-4o',
          messages: requestMessages,
          temperature: 0.7,
        }),
      });
      const data = await response.json();
      const reply = data.choices[0].message.content;
      const assistantMessage: Message = { role: 'assistant', content: reply };
      setChatMessages([...updatedChat, assistantMessage]);
    } catch (error) {
      console.error('Error calling OpenAI API:', error);
    }

    setInput('');
  };

  // Simple inline styles to mimic a messaging system
  const containerStyle: React.CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    maxWidth: '600px',
    margin: '0 auto',
  };

  const messagesContainerStyle: React.CSSProperties = {
    flexGrow: 1,
    overflowY: 'auto',
    padding: '10px',
    marginBottom: '20px',
    backgroundColor: '#f0f0f0',
    borderRadius: '10px',
    height: '300px',
  };

  const messageBubbleStyle = (isUser: boolean): React.CSSProperties => ({
    alignSelf: isUser ? 'flex-end' : 'flex-start',
    backgroundColor: isUser ? '#DCF8C6' : '#FFF',
    color: '#000',
    padding: '10px 15px',
    borderRadius: '20px',
    margin: '5px 0',
    maxWidth: '80%',
  });

  const inputStyle: React.CSSProperties = {
    flexGrow: 0,
    padding: '10px',
    width: 'calc(100% - 100px)',
    borderRadius: '20px',
    border: '1px solid #ccc',
    outline: 'none',
  };

  const buttonStyle: React.CSSProperties = {
    padding: '10px 20px',
    marginLeft: '10px',
    borderRadius: '20px',
    border: 'none',
    backgroundColor: '#34B7F1',
    color: '#fff',
    cursor: 'pointer',
  };

  return (
    <div style={containerStyle}>
      <h2 style={{ textAlign: 'center' }}>Salon-AI Chatbot</h2>
      <div style={messagesContainerStyle}>
        {chatMessages.map((msg, idx) => (
          <div key={idx} style={messageBubbleStyle(msg.role === 'user')}>
            {msg.content}
          </div>
        ))}
      </div>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <input
          type="text"
          placeholder="Type your message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          style={inputStyle}
        />
        <button onClick={handleSend} style={buttonStyle}>
          Send
        </button>
      </div>
    </div>
  );
};

export default Chatbot;