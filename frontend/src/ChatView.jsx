import React, { useState } from "react";
import axios from "axios";
import { useDispatch } from "react-redux";
import { setAll } from "./interactionSlice";

export default function ChatView() {
  const [message, setMessage] = useState("");
  const dispatch = useDispatch();

  const sendMessage = async () => {
    const res = await axios.post("http://localhost:8000/chat-log", {
      message,
    });

    dispatch(setAll(res.data));
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
      <textarea
        placeholder="Describe interaction..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button onClick={sendMessage}>Log</button>
    </div>
  );
}
