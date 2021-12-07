const btn_conf = document.querySelector(".btn-confirmation");

btn_conf.addEventListener("click", async () => {
  try {
    const reponse = await envoyer_requete();
    alert(reponse);
  } catch (erreur) {
    alert(erreur);
  }
  window.location.href("http://localhost:5000/");
});

const envoyer_requete = async () => {
  path = "/api" + window.location.pathname;
  const reponse = await fetch(path, {
    method: "DELETE",
  });
  if (!reponse.ok) {
    return reponse.json().then((msg) => {
      throw new Error(msg);
    });
  }
  return reponse.json();
};
