import "./App.css";
import CanvasDraw from "react-canvas-draw";
import { useEffect, useState } from "react";
import axios from "axios";

const label = {
  0: "Zero",
  1: "One",
  2: "Two",
  3: "Three",
  4: "Four",
  5: "Five",
  6: "Six",
  7: "Seven",
  8: "Eight",
  9: "Nine",
};

function dataURLtoBlob(dataurl) {
  var arr = dataurl.split(","),
    mime = arr[0].match(/:(.*?);/)[1],
    bstr = atob(arr[1]),
    n = bstr.length,
    u8arr = new Uint8Array(n);
  while (n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }
  return new Blob([u8arr], { type: mime });
}

const classify = async (file) => {
  const headers = {
    "Content-Type": "multipart/form-data",
    accept: "application/json",
  };
  var blob = dataURLtoBlob(file);

  var formData = new FormData();
  formData.append("file", blob, "img.png");

  //Change url by http://127.0.0.1:3000/classify if you are in local.
  const req = await axios.post(
    "http://18.208.165.239:3000/classify",
    formData,
    {
      headers,
    }
  );
  const data = req.data;
  return data;
};

function App() {
  const [canvas, setCanvas] = useState(null);
  const [prediction, setPrediction] = useState("-");
  const [proba, setProba] = useState(0.5);

  const makePrediction = async () => {
    const imgEncode = canvas.getDataURL("image/png", false, "#000000");
    const data = await classify(imgEncode);
    setPrediction(data.prediction);
    setProba(data.proba);
  };
  const clear = () => {
    canvas.clear();
  };

  return (
    <div className="App">
      <div className="draw-section">
        <div className="title">
          <h1>Digit classifier</h1>
        </div>
        <div className="subtitle">
          <h2>Draw a digit</h2>
        </div>

        <CanvasDraw
          canvasWidth={400}
          canvasHeight={400}
          loadTimeOffset={0}
          lazyRadius={-4}
          brushRadius={15}
          ref={(canvasDraw) => setCanvas(canvasDraw)}
          brushColor={"white"}
          hideGrid
          backgroundColor={"black"}
          onChange={() => console.log("onChange")}
        />
        <div className="button-sec">
          <button
            className="me-1"
            onClick={() => {
              clear();
            }}
          >
            Clear
          </button>
          <button
            onClick={() => {
              makePrediction();
            }}
          >
            Classify
          </button>
        </div>
      </div>
      <div className="info-section ms-1">
        <div className="title">
          <h1></h1>
        </div>
        <div className="subtitle">
          <h2>Information</h2>
        </div>
        <div className="info">
          <div className="circle">
            <div className="inner-circle">{prediction}</div>
          </div>
          <h2>{label[prediction]}</h2>
          <div className="">Score</div>
          <div className="progress">
            <div style={{ width: `${proba * 100}%` }} className="advance"></div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
