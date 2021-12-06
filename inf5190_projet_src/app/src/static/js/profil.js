const div_select = document.querySelector(".select-arr");
const arr_select = document.querySelector(".liste-arr");
const btn_ajouter = document.querySelector(".ajouter-arr");
const btn_supprimer = document.querySelector(".supprimer-arr");
const btn_soumettre = document.querySelector(".soumission");
const msg_erreur = document.querySelector(".msg-erreur");

btn_ajouter.addEventListener("click", async () => {
  if (arr_select.childElementCount === 0) {
    const noms = await chercher_nom_arr();
    arr_select.innerHTML = creer_select_arr(noms);
  } else {
    let clone = arr_select.children[0].cloneNode(true);
    clone.nodeValue = "";
    arr_select.append(clone);
  }
});

btn_soumettre.addEventListener("click", async () => {
  try {
    reponse = await envoyer_requete(former_corps());
    alert("Votre profil a été créé avec succès.");
    window.location.href = "http://localhost:5000/";
  } catch (erreur) {
    afficher_erreur(erreur);
  }
});

btn_supprimer.addEventListener("click", () => {
  if (arr_select.childElementCount > 0) {
    arr_select.childNodes.item(arr_select.childNodes.length - 1).remove();
  }
});

const former_corps = () => {
  const liste_arr = document.querySelectorAll(".arrondissement");
  const input_courriel = document.querySelector("#courriel-profil");
  const input_nom = document.querySelector("#nom-profil");
  let liste = [];
  liste_arr.forEach((arr) => {
    if (arr.value !== "") {
      liste.push(arr.value);
    }
  });
  let body = {
    nom: input_nom.value,
    email: input_courriel.value,
    liste_arr: liste,
  };
  return body;
};

const chercher_nom_arr = async () => {
  const response = await fetch("/api/arrondissements", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (!response.ok) {
    return response.json().then((msg) => {
      throw new Error(msg);
    });
  }
  return response.json();
};

const envoyer_requete = async (corps) => {
  const reponse = await fetch("/api/profil", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(corps),
  });
  if (!reponse.ok || reponse.status === 200) {
    return reponse.json().then((msg) => {
      throw new Error(msg);
    });
  }
  return reponse.json();
};

const creer_select_arr = (noms) => {
  let selection =
    "<select name='liste_arr[]' class='arrondissement form-select mb-2'>" +
    "<option selected value=''>Sélectionnez l'arrondissement que vous désirez suivre</option>";
  noms.forEach((nom) => {
    selection += "<option value=" + nom + " >" + nom + "</option>";
  });
  selection += "</select>";
  return selection;
};

const reset_erreur = () => {
  msg_erreur.innerHTML = "&nbsp;";
  msg_erreur.classList.add("cache");
};

const afficher_erreur = (erreur) => {
  msg_erreur.innerHTML =
    "Une erreur s'est produite lors de votre requête :" + erreur.message;
  msg_erreur.classList.remove("cache");
};
