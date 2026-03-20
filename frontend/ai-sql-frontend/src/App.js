import { useState } from "react";
import './App.css';

function App() {
  const [question, setQuestion] = useState("");
  const [sql, setSql] = useState("");
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const API_URL = process.env.REACT_APP_API_URL;

  const runQuery = async () => {
    if (!question) return;

    setLoading(true);
    setSql("");
    setData([]);

    try {
      const res = await fetch(
      `${API_URL}/query?question=${encodeURIComponent(question)}`,
      {
        method: "POST",
      }
    );

      const result = await res.json();

      setSql(result.generated_sql || result.detail);
      setData(result.result || []);
    } catch (err) {
      alert("Error: " + err.message);
    }

    setLoading(false);
  };

  return (
    <div style={{ maxWidth: "900px", margin: "40px auto", fontFamily: "Arial" }}>
      <h1> AI SQL Generator</h1>

      <div style={{ marginBottom: "20px" }}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask something like: Show all users"
          style={{ width: "70%", padding: "10px" }}
        />

        <button onClick={runQuery} style={{ marginLeft: "10px", padding: "10px" }}>
          Run
        </button>
      </div>

      {loading && <p>⏳ Loading...</p>}

      {sql && (
        <>
          <h3>Generated SQL</h3>
          <pre>{sql}</pre>
        </>
      )}

      {data.length > 0 && (
        <>
          <h3>Results</h3>
          <table border="1" cellPadding="8" style={{ width: "100%" }}>
            <thead>
              <tr>
                {Object.keys(data[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {data.map((row, i) => (
                <tr key={i}>
                  {Object.values(row).map((val, j) => (
                    <td key={j}>{val}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </>
      )}
    </div>
  );
}

export default App;
