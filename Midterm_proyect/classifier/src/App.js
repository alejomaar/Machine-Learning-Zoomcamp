import "./App.css";

const questions = [
  {
    description: "Cries when feels down or things are not going well",
    name: "life_struggles",
  },
  { description: "like PC software, hardware", name: "pc" },
  { description: "like shopping", name: "shopping" },
  { description: "like war movies", name: "war" },
  { description: "like action movies", name: "action" },
  { description: "like cars ", name: "cars" },
  {
    description: "like science and technology",
    name: "science_and_technology",
  },
  { description: "like romantic movies", name: "romantic" },
  { description: "like poetry reading", name: "reading" },
  { description: "like western movies", name: "western" },
  { description: "like dancing", name: "dancing" },
  { description: "like theatre", name: "theatre" },
  { description: "Are you afraid of darkness?", name: "darkness" },
];

function App() {
  const submit = () => {
    let response = questions.reduce((acc, { name }) => {
      const input = document.querySelector(`input[name=${name}]:checked`);
      return {
        ...acc,
        [name]: +input?.value,
      };
    }, {});
    response["height"] = +document.getElementById("height")?.value;
    response["weight"] = +document.getElementById("weight")?.value;

    console.log(response);
  };

  return (
    <div className="app d-flex flex-column justify-content-center">
      <h1>Gender Classificator</h1>
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
