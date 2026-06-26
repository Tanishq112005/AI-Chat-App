import { useState } from "react";
import "./ChatInputComponent.css";

function ChatInputComponent() {
  const [inputValue, setInputValue] = useState("");
  
  // Set the default to "gemini" so the second option is pre-selected
  const [selectedModel, setSelectedModel] = useState("Jarvis");

  function sendButtonOnClick() {
    console.log(inputValue);
  }

  return (
    <div className="chatBoxInputComponent">

        <input
        className="writingSection"
        type="text"
        placeholder={`Ask ${selectedModel}...`} 
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
      />
      
      <select 
        className="modelSelector"
        value={selectedModel}
        onChange={(e) => setSelectedModel(e.target.value)}
        aria-label="Select AI model" 
        title="Select AI model"
      >
        <option value="Jarvis">Jarvis</option>
        <option value="Gemini">Gemini Pro</option>
        <option value="GPT">GPT-4</option>
      </select>

      <button className="submitButton" onClick={sendButtonOnClick}>
        Send
      </button>

    </div>
  );
}

export default ChatInputComponent;