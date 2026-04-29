import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { updateField } from "./interactionSlice";

export default function FormView() {
  const dispatch = useDispatch();
  const data = useSelector((state) => state.interaction);

  const handleChange = (field, value) => {
    dispatch(updateField({ field, value }));
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
      <input
        placeholder="HCP Name"
        value={data.hcpName}
        onChange={(e) => handleChange("hcpName", e.target.value)}
      />

      <input
        type="date"
        value={data.date}
        onChange={(e) => handleChange("date", e.target.value)}
      />

      <input
        type="time"
        value={data.time}
        onChange={(e) => handleChange("time", e.target.value)}
      />

      <input
        placeholder="Interaction Type"
        value={data.type}
        onChange={(e) => handleChange("type", e.target.value)}
      />

      <textarea
        placeholder="Topics Discussed"
        value={data.topics}
        onChange={(e) => handleChange("topics", e.target.value)}
      />

      <input
        placeholder="Sentiment"
        value={data.sentiment}
        onChange={(e) => handleChange("sentiment", e.target.value)}
      />

      <textarea
        placeholder="Outcomes"
        value={data.outcomes}
        onChange={(e) => handleChange("outcomes", e.target.value)}
      />

      <textarea
        placeholder="Follow-ups"
        value={data.followUps}
        onChange={(e) => handleChange("followUps", e.target.value)}
      />
    </div>
  );
}
