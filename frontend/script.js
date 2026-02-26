async function getWeather() {
  const city = document.getElementById("city").value;
  const res = await fetch(`http://localhost:8000/weather/${city}`);
  const data = await res.json();

  document.getElementById("result").innerHTML = `
    <h3>${data.city}</h3>
    <p>🌡️ ${data.temperature} °C</p>
    <p>💧 ${data.humidity}%</p>
    <p>${data.description}</p>
  `;
}
