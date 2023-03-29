import React, { useState } from 'react';
import axios from 'axios';
import './MissionControlPanel.css';

function App() {
    const [inputData, setInputData] = useState('');
    const [responseData, setResponseData] = useState(null);
    const [imageResponse, setImageResponse] = useState(null);
    const [selectedFile, setSelectedFile] = useState(null);

    const handleChange = (e) => {
        setInputData(e.target.value);
    };

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

            setImageResponse(response.data);
        } catch (error) {
            console.error('Error uploading image:', error);
            setImageResponse(null);
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
            <div className="mission-control-panel">
                <h1>Is it a Missile or Spaceship!?</h1>
                <div className="control-section">
                    <h2>Upload image of a Missile or a Falcon 9 Rocket to find out now!</h2>
                    <form onSubmit={handleUpload}>
                        <input type="file" onChange={handleFileChange} accept="image/*" />
                        <button type="submit">Upload</button>
                    </form>
                </div>

                {imageResponse && (
                    <div className="control-section image-response">
                        <h2>Image Upload Response:</h2>
                        <p>{imageResponse.message}</p>
                        
                        
                        <img
                            src={`http://localhost:5000/uploads/${imageResponse.filename}`}
                            alt="Uploaded"
                            className="uploaded-image"
                        />
                        <p>Prediction: {imageResponse.prediction}</p>
                        <p>Probability: {imageResponse.probability}</p>
                        <p> Please excuse any inaccurate results! This was built purely for fun! </p>
                        <p> Source Code: https://github.com/omthurman/ICBMorRocket  Created by Owen Thurman. Special Thanks to Corey Mccrea for hosting this for free!</p>
                    </div>
                )}
            </div>
        </div>
    );
}

export default App;