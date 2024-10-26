function submitForm() {
    // Collect form data
    const modelType = document.getElementById("model_type").value;
    const age = document.getElementById("age").value;
    const glucose = document.getElementById("glucose").value;
    const insulin = document.getElementById("insulin").value;
    const bmi = document.getElementById("bmi").value;

    // Form the data object
    const data = {
        model_type: modelType,
        age: age,
        glucose: glucose,
        insulin: insulin,
        bmi: bmi
    };

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById("result").innerText = `Diabetes Type Prediction: ${result.diabetes_type}`;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerText = "An error occurred. Please try again.";
    });
}
