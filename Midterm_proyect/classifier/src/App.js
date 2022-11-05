import "./App.css";

function App() {
  const submit = () => {
    var x = document.querySelector("input[name=t]:checked");
    console.log(x.value);
  };

  return (
    <div className="app d-flex flex-column justify-content-center">
      <h1>Gender Classificator</h1>
      <div className="card d-flex flex-column align-items-center">
        <label htmlFor="">Cual es tu peso(kg)</label>
        <div>
          <input type="number" />
        </div>
      </div>
      <div className="card d-flex flex-column align-items-center">
        <label htmlFor="">Cual es tu altura(cm)</label>
        <div>
          <input type="number" />
        </div>
      </div>
      <div className="card d-flex flex-column align-items-center">
        <label htmlFor="">Te gustan las peliculas</label>
        <div className="d-flex">
          <span>Disagree</span>
          <div>
            <input type="radio" name="t" id="" value={1} />
            <input type="radio" name="t" id="" value={2} />
            <input type="radio" name="t" id="" value={3} />
            <input type="radio" name="t" id="" value={4} />
            <input type="radio" name="t" id="" value={5} />
          </div>
          <span>Agree</span>
        </div>
      </div>

      <button onClick={() => submit()}>Submit</button>
    </div>
  );
}

export default App;
