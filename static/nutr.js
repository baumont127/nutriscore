function deplier(e){
    var q = e.target;
    var r = q.nextElementSibling;

    if (r.classList.contains("reponse-cachee")){
        r.classList.remove("reponse-cachee");
        r.classList.add("reponse-visible");
    }
    else {
        r.classList.add("reponse-cachee");
        r.classList.remove("reponse-visible");
    }
}

/* Chargement de la page FAQ */
function load_faq(){
    var hash=window.location.hash;

    /* Si lien vers une ancre, on déplie la réponse correspondante */
    if (hash){
        hash=hash.substring(1,hash.length);
        r = document.getElementById(hash).nextElementSibling;
        r.classList.remove("reponse-cachee");
        r.classList.add("reponse-visible");
    }

}