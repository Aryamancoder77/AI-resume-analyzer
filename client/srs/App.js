import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const uploadResume = async () => {
    const formData = new FormData();
    formData.append("resume", file);

    const res = await axios.post("http://localhost:5000/upload", formData);
    setResult(res.data);
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>AI Resume Analyzer</h1>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={uploadResume}>Analyze</button>

      {result && (
        <div>
          <h2>Score: {result.score}</h2>
          <h3>Skills: {result.skills.join(", ")}</h3>
          <h3>Suggestions:</h3>
          <ul>
            {result.suggestions.map((s, i) => (
              <li key={i}>{s}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
