document.addEventListener("DOMContentLoaded", () => {
  const analyzeBtn = document.getElementById("analyzeBtn");
  const clearBtn = document.getElementById("clearBtn");
  const input = document.getElementById("inputText");
  const output = document.getElementById("output");

  analyzeBtn.addEventListener("click", async () => {
    const text = input.value.trim();
    if (!text) {
      output.innerHTML = '<span style="color:#a33;">Please enter some text.</span>';
      return;
    }
    output.innerHTML = "Analyzing...";
    try {
      const resp = await fetch("/api/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text})
      });
      if (!resp.ok) {
        const err = await resp.json();
        output.innerHTML = `<span style="color:#a33;">Error: ${err.error || resp.statusText}</span>`;
        return;
      }
      const data = await resp.json();
      const label = data.label || "UNKNOWN";
      const score = typeof data.score === "number" ? (data.score * 100).toFixed(2) : "N/A";
      const cls = (label === "POSITIVE") ? "positive" : (label === "NEGATIVE" ? "negative" : "neutral");
      output.innerHTML = `<div>Label: <span class="${cls}">${label}</span></div><div>Confidence: ${score}%</div>`;
    } catch (e) {
      output.innerHTML = `<span style="color:#a33;">Network error: ${e.message}</span>`;
    }
  });

  clearBtn.addEventListener("click", () => {
    input.value = "";
    output.innerHTML = "";
  });
});
