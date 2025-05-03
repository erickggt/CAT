
document.getElementById("cat-form").addEventListener("submit", async function(e) {
  e.preventDefault();
  const formData = new FormData(this);
  const data = {};
  formData.forEach((value, key) => {
    data[key] = value;
  });

  const response = await fetch("https://SEU_BACKEND_URL/enviar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const msg = await response.text();
  document.getElementById("mensagem").innerText = msg;
});
