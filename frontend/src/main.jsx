import React, { useState } from "react";
import { io } from "socket.io-client";

const socket = io("http://localhost:5000");

function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState("");
  const [status, setStatus] = useState("");

  React.useEffect(() => {
    socket.on("status", (data) => setStatus(data.message));
    return () => {
      socket.off("status");
    };
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult("Submitting...");
    const res = await fetch("http://localhost:5000/api/execute", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ tool: "sqlmap", params: { target_url: url } }),
    });
    const data = await res.json();
    setResult(JSON.stringify(data, null, 2));
  };

  return (
    <div style={{ maxWidth: 600, margin: "2rem auto", fontFamily: "sans-serif" }}>
      <h1>HexStrike</h1>
      <div>Status: {status}</div>
      <form onSubmit={handleSubmit} style={{ margin: "1rem 0" }}>
        <input
          type="text"
          placeholder="Target URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          style={{ width: "70%", padding: "0.5rem" }}
        />
        <button type="submit" style={{ padding: "0.5rem 1rem", marginLeft: "1rem" }}>
          Scan
        </button>
      </form>
      <pre style={{ background: "#f4f4f4", padding: "1rem" }}>{result}</pre>
    </div>
  );
}

export default App;
