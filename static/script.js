async function solve() {
  const formula = document.getElementById("formula").value;
  const x0 = document.getElementById("x0").value;
  const tol = document.getElementById("tol").value;
  const max_iter = document.getElementById("max_iter").value;

  const response = await fetch("/solve", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ formula, x0, tol, max_iter }),
  });

  const data = await response.json();
  const resultDiv = document.getElementById("result");
  const tableBody = document.querySelector("#iteration-table tbody");

  tableBody.innerHTML = ""; // پاک کردن جدول قبلی

  if (data.status === "success") {
    resultDiv.innerHTML = "Root = <b>" + data.root.toFixed(10) + "</b>";

    data.iterations.forEach((row) => {
      const tr = document.createElement("tr");

      tr.innerHTML = `
        <td>${row.iter}</td>
        <td>${row.x.toFixed(10)}</td>
        <td>${row["f(x)"].toFixed(10)}</td>
        <td>${row.error.toFixed(10)}</td>
      `;

      tableBody.appendChild(tr);
    });
  } else {
    resultDiv.innerHTML = "⛔ " + data.message;
  }
}
