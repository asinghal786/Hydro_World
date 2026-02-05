async function analyze() {
    const fields = [
        "ph","Hardness","Solids","Chloramines","Sulfate",
        "Conductivity","Organic_carbon","Trihalomethanes","Turbidity"
    ];

    let data = {};
    for (let f of fields) {
        data[f] = parseFloat(document.getElementById(f).value);
    }

    const resultDiv = document.getElementById("result");
    resultDiv.innerText = "Analyzing water...";

    try {
        const res = await fetch("/api/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        const out = await res.json();

        if (out.potability === "Safe") {
            resultDiv.innerText = "✅ SAFE TO DRINK";
            resultDiv.style.color = "#00ffcc";
        } else {
            resultDiv.innerText = "❌ UNSAFE TO DRINK";
            resultDiv.style.color = "#ff6b6b";
        }
    } catch (err) {
        resultDiv.innerText = "Error analyzing water";
        resultDiv.style.color = "yellow";
    }
}
