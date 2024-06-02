import React, { useState } from 'react';
import { ChromePicker } from 'react-color';
import { Slider, Typography } from '@material-ui/core';

function LEDControl() {
  const [color, setColor] = useState("#ffffff");  // Default white color
  const [brightness, setBrightness] = useState(0.5);  // Default brightness

  const updateLEDs = async (data) => {
    const response = await fetch('http://raspberrypi.tailc0c1b.ts.net:8000/api/control/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    const responseData = await response.json();
    console.log(responseData);
  };

  const handleColorChange = (color) => {
    setColor(color.hex);
    updateLEDs({ color: color.hex });
  };

  const handleBrightnessChange = (event, newValue) => {
    setBrightness(newValue);
    updateLEDs({ brightness: newValue });
  };

  return (
    <div style={{ padding: 20 }}>
      <Typography variant="h6">LED Control</Typography>
      
      <div>
        <Typography>Color</Typography>
        <ChromePicker color={color} onChangeComplete={handleColorChange} />
      </div>
      
      <div>
        <Typography>Brightness</Typography>
        <Slider
          value={brightness}
          onChange={handleBrightnessChange}
          step={0.01}
          min={0}
          max={1}
          valueLabelDisplay="auto"
        />
      </div>
    </div>
  );
}

export default LEDControl;
