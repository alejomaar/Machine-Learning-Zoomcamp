import "./App.css";
import CanvasDraw from "react-canvas-draw";
import { useEffect, useState } from "react";
import axios from "axios";

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
  const data = await axios.post("http://127.0.0.1:3000/analyze", formData, {
    headers,
  });
};

function App() {
  const [canvas, setCanvas] = useState(null);

  return (
    <div className="App">
      <button
        onClick={() => {
          const imgEncode = canvas.getDataURL("image/png", false, "#000000");
          classify(imgEncode);
        }}
      >
        GetDataURL
      </button>
      <CanvasDraw
        loadTimeOffset={0}
        lazyRadius={-7}
        brushRadius={10}
        ref={(canvasDraw) => setCanvas(canvasDraw)}
        brushColor={"white"}
        hideGrid
        backgroundColor={"black"}
        onChange={() => console.log("onChange")}
      />
    </div>
  );
}

export default App;
