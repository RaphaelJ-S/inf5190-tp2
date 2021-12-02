const connecterBtn = document.getElementById("btn-connect");
const rememberBtn = document.getElementById("btn-remember");

connecterBtn.addEventListener("click", async (e) => {
  e.preventDefault();
  retour = await send();
});

rememberBtn.addEventListener("click", (e) => {
  e.preventDefault();
});

async function send() {
  let inputs = getFormInputs();
  let retour = null;
  console.log(inputs);
  console.log(JSON.stringify(inputs));
  const response = await fetch("/login", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify(inputs),
  });
  if (response.status < 200 || response.status > 299) {
    console.log(response.status);
  } else {
    retour = response;
  }

  return retour;
}

function getFormInputs() {
  const form = document.getElementById("formulaire-login").elements;
  inputs = {};
  for (let i = 0; i < form.length; i++) {
    if (form[i].name !== "") {
      inputs[form[i].name] = form[i].value;
    }
  }
  return inputs;
}
