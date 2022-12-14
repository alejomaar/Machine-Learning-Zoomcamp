import { useState } from "react";
import "./App.css";
import axios from "axios";

const questions = [
  {
    description: "Cries when feels down or things are not going well ๐ข",
    name: "life_struggles",
  },
  { description: "like PC software, hardware ๐จโ๐ป", name: "pc" },
  { description: "like shopping ๐๏ธ", name: "shopping" },
  { description: "like war movies ", name: "war" },
  { description: "like action movies โ๏ธ", name: "action" },
  { description: "like cars ๐", name: "cars" },
  {
    description: "like science and technology ๐งช",
    name: "science_and_technology",
  },
  { description: "like romantic movies โค๏ธ", name: "romantic" },
  { description: "like poetry reading ๐", name: "reading" },
  { description: "like western movies ๐ค ", name: "western" },
  { description: "like dancing ๐ต", name: "dancing" },
  { description: "like theatre ๐ญ", name: "theatre" },
  { description: "Are you afraid of darkness? โซ", name: "darkness" },
];

function App() {
  const submit = async () => {
    let response = questions.reduce((acc, { name }) => {
      const input = document.querySelector(`input[name=${name}]:checked`);
      return {
        ...acc,
        [name]: +input?.value,
      };
    }, {});
    response["height"] = +document.getElementById("height")?.value;
    response["weight"] = +document.getElementById("weight")?.value;

    const res = await axios.post(
      "http://54.204.130.172:3000/classify",
      response
    );
    const data = res.data;
    console.log(data);
    setGender(data.class);
  };

  const [gender, setGender] = useState(null);

  if (gender)
    return (
      <div
        className="d-flex justify-content-center align-items-center flex-column"
        style={{ width: "100%", height: "80vh", margin: "1rem 0rem" }}
      >
        <h1 style={{ margin: "1rem auto" }}>Your gender prediction is:</h1>

        <span style={{ textAlign: "center" }} className="end">
          {gender === "women" ? "๐ง๐ฝ" : "๐ฆ"}
        </span>
        <button className="btn" onClick={() => setGender(null)}>
          Retry
        </button>
      </div>
    );

  if (!gender)
    return (
      <div className="app d-flex flex-column justify-content-center">
        <h1 style={{ margin: "1rem auto" }}>Are you ๐ง๐ฝ or ๐ฆ?</h1>
        <p style={{ margin: "0rem auto" }}>
          Fill out this questionnaire and your gender will be revealed.
        </p>
        <div className="card d-flex flex-column align-items-center">
          <label htmlFor="">What is your height(cm)?</label>
          <div style={{ marginTop: "0.5rem" }}>
            <input id="height" type="number" />
          </div>
        </div>
        <div className="card d-flex flex-column align-items-center">
          <label htmlFor="">What is your weight(kg)?</label>
          <div style={{ marginTop: "0.5rem" }}>
            <input id="weight" type="number" />
          </div>
        </div>
        {questions.map(({ description, name }) => (
          <div className="card d-flex flex-column align-items-center">
            <label htmlFor="">{description}</label>
            <div style={{ marginTop: "0.5rem" }} className="d-flex">
              <span className="warning">Disagree</span>
              <div>
                <input type="radio" name={name} id="" value={1} />
                <input type="radio" name={name} id="" value={2} />
                <input type="radio" name={name} id="" value={3} />
                <input type="radio" name={name} id="" value={4} />
                <input type="radio" name={name} id="" value={5} />
              </div>
              <span className="ok">Agree</span>
            </div>
          </div>
        ))}

        <div
          className="d-flex justify-content-center"
          style={{ width: "100%", margin: "1rem 0rem" }}
        >
          <button className="btn" onClick={() => submit()}>
            Submit
          </button>
        </div>
      </div>
    );
}

export default App;
