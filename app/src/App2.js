import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [inputData, setInputData] = useState('');
  const [responseData, setResponseData] = useState(null);

  const handleChange = (e) => {
    setInputData(e.target.value);
  };

  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleUpload = async (e) => {
    e.preventDefault();
  
    if (!selectedFile) {
      alert('Please select a file before uploading.');
      return;
    }
  
    const formData = new FormData();
    formData.append('file', selectedFile);
  
    try {
      const response = await axios.post('http://localhost:5000/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
  
      console.log(response.data);
    } catch (error) {
      console.error('Error uploading image:', error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:5000/api/data', { data: inputData });
      setResponseData(response.data);
    } catch (error) {
      console.error('Error making API request:', error);
    }
  };

  return (
    <div className="App">
      <h1>React - Flask API Request</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" value={inputData} onChange={handleChange} placeholder="Enter some data" />
        <button type="submit">Send to Flask</button>
      </form>
      {responseData && (
        <div>
          <h2>Response from Flask:</h2>
          <p>{responseData.message}</p>
          <p>Data: {JSON.stringify(responseData.data)}</p>
        </div>
      )}
      <h2>Upload Image</h2>
      <form onSubmit={handleUpload}>
      <input type="file" onChange={handleFileChange} accept="image/*" />
      <button type="submit">Upload</button>
      </form>
      {responseData && (
        <div>
          <h2>Response from Flask:</h2>
          <p>{responseData.message}</p>
          <p>Data: {JSON.stringify(responseData.data)}</p>
        </div>
      )}
    </div>
  );
}

export default App;