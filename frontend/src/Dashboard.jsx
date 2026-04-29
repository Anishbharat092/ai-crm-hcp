import React from "react";
import FormView from "./FormView";
import ChatView from "./ChatView";

export default function Dashboard() {
  return (
    <div style={{ display: "flex", padding: "20px", gap: "20px" }}>
      {/* LEFT SIDE - FORM */}
      <div style={{ flex: 2, border: "1px solid #ccc", padding: "20px" }}>
        <h2>Log HCP Interaction</h2>
        <FormView />
      </div>

      {/* RIGHT SIDE - AI */}
      <div style={{ flex: 1, border: "1px solid #ccc", padding: "20px" }}>
        <h3>AI Assistant</h3>
        <ChatView />
      </div>
    </div>
  );
}
