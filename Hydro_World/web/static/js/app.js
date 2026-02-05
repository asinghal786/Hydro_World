// Hydro_World Frontend Logic
// Step 3: Connect form to backend API

const form = document.getElementById("waterForm");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    // Collect input values
    const inputs = form.querySelectorAll("input");

    const payload = {
        pH: parseFloat(inputs[0].value),
        turbidity: parseFloat(inputs[1].value),
        electrical_conductivity: parseFloat(inputs[2].value),
        tds: parseFloat(inputs[3].value),
        dissolved_oxygen: parseFloat(inputs[4].value),
        temperature: parseFloat(inputs[5].value),
        hardness: parseFloat(inputs[6].value),
        alkalinity: parseFloat(inputs[7].value),
        chloride: parseFloat(inputs[8].value),
        sulfate: parseFloat(inputs[9].value)
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/api/train", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        // Temporary display (NO ML yet)
        document.querySelectorAll(".placeholder-text").forEach(el => {
            el.textContent = "Backend reached successfully. Training logic coming next.";
        });

        console.log("Backend response:", result);

    } catch (error) {
        alert("Error connecting to backend. Is it running?");
        console.error(error);
    }
});
