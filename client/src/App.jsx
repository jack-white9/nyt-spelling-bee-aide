import React, { useState } from "react";
import "./App.css";

export const App = () => {
  const [centerLetter, setCenterLetter] = useState("");
  const [outsideLetters, setOutsideLetters] = useState("");
  const [apiResponse, setApiResponse] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();

    const apiUrl = `TEMP_URL?center=${centerLetter}&outside=${outsideLetters}`;
    try {
      const response = await fetch(apiUrl);
      const data = await response.json();
      setApiResponse(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div className="app-container">
      <header>
        <h1>NYT Spelling Bee Aide</h1>
      </header>
      <form onSubmit={handleSubmit}>
        <label htmlFor="centerLetter">Center letter:</label>
        <input
          type="text"
          id="centerLetter"
          value={centerLetter}
          onChange={(e) => setCenterLetter(e.target.value)}
          required
        />
        <br />
        <label htmlFor="outsideLetters">Outside letters:</label>
        <input
          type="text"
          id="outsideLetters"
          value={outsideLetters}
          onChange={(e) => setOutsideLetters(e.target.value)}
          required
        />
        <br />
        <button type="submit">Submit</button>
      </form>
      {apiResponse && (
        <div className="api-response">
          <p>API Response:</p>
          <p>{apiResponse}</p>
        </div>
      )}
    </div>
  );
};
