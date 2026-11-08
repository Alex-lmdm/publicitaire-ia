/* Les objets connus : ce que tout le monde reconnaît d'un coup d'œil, dans ses vraies couleurs
   (le dossier bleu du Mac, les fichiers PDF, Word, Excel, PowerPoint, une vidéo, une image, un son,
   une archive). Dessinés par nous, d'après leur allure courante, sans reprendre un fichier d'Apple
   ni de Microsoft. Ils gardent leurs couleurs dans toutes les marques : c'est la touche de couleur
   vraie qui évite une vidéo toute dans les trois couleurs du client (image.md, « Les objets
   connus »). K.ic("objet-pdf") rend le SVG ; `palette` connaît ces couleurs (COULEURS_CONNUES de
   studio_motion.py, à garder identiques). Couleur d'outil : chaque teinte ci-dessous. L'étiquette
   d'un fichier (« PDF ») est une texture qu'on reconnaît, pas un texte à lire : data-layout-ignore. */
(function () {
  var page = function (glyphe, etiquette, couleur) {
    return '<svg viewBox="0 0 84 104" xmlns="http://www.w3.org/2000/svg" fill="none">' +
      '<path d="M11 4h43l26 26v63a7 7 0 0 1-7 7H11a7 7 0 0 1-7-7V11a7 7 0 0 1 7-7z" fill="#ffffff" stroke="#d1d1d6" stroke-width="2.5"/>' +
      '<path d="M54 4v19a7 7 0 0 0 7 7h19" fill="#ececf0" stroke="#d1d1d6" stroke-width="2.5" stroke-linejoin="round"/>' +
      glyphe +
      (etiquette ? '<rect x="13" y="70" width="58" height="22" rx="6" fill="' + couleur + '"/>' +
        '<text data-layout-ignore="" x="42" y="86.5" text-anchor="middle" font-family="Inter, Helvetica, Arial, sans-serif" font-size="15" ' +
        'font-weight="800" letter-spacing="0.6" fill="#ffffff">' + etiquette + '</text>' : '') +
      '</svg>';
  };
  var lignes = '<rect x="16" y="34" width="38" height="4.5" rx="2.25" fill="#c7c7cc"/>' +
    '<rect x="16" y="43" width="52" height="4.5" rx="2.25" fill="#c7c7cc"/>' +
    '<rect x="16" y="52" width="46" height="4.5" rx="2.25" fill="#c7c7cc"/>';
  var c = {   // couleur d'outil : les teintes que ces fichiers ont partout
    pdf: "#d42d28", doc: "#2b67d1", tableur: "#1a7f45", presentation: "#c54d1d",
    video: "#7d4fe0", image: "#0b7d88", audio: "#d02a59", zip: "#6e6e73"
  };
  window.K_ICONES = Object.assign(window.K_ICONES || {}, {
    // Le dossier bleu du Mac : le dos plus soutenu, la face claire et son liseré.
    "objet-dossier": '<svg viewBox="0 0 128 100" xmlns="http://www.w3.org/2000/svg">' +
      '<path d="M10 19a10 10 0 0 1 10-10h25.5c3 0 5.6 1.2 7.6 3.4l5.4 6.1H108a10 10 0 0 1 10 10V40H10z" fill="#2f8fe6"/>' +
      '<rect x="10" y="29" width="108" height="64" rx="9" fill="#5db6f7"/>' +
      '<rect x="10" y="29" width="108" height="5" rx="2.5" fill="#8dcffb"/></svg>',
    "objet-fichier": page(lignes, "", ""),
    "objet-pdf": page(lignes, "PDF", c.pdf),
    "objet-doc": page(lignes, "DOC", c.doc),
    "objet-tableur": page('<rect x="16" y="30" width="52" height="30" rx="3" stroke="' + c.tableur + '" stroke-width="2.5"/>' +
      '<path d="M33.3 30v30M50.6 30v30M16 40h52M16 50h52" stroke="' + c.tableur + '" stroke-width="2"/>', "XLS", c.tableur),
    "objet-presentation": page('<rect x="16" y="30" width="52" height="32" rx="3" stroke="' + c.presentation + '" stroke-width="2.5"/>' +
      '<rect x="24" y="46" width="7" height="10" rx="1.5" fill="' + c.presentation + '"/>' +
      '<rect x="38.5" y="40" width="7" height="16" rx="1.5" fill="' + c.presentation + '"/>' +
      '<rect x="53" y="35" width="7" height="21" rx="1.5" fill="' + c.presentation + '"/>', "PPT", c.presentation),
    "objet-video": page('<path d="M33 31.5v25.5l21-12.75z" fill="' + c.video + '"/>', "MP4", c.video),
    "objet-image": page('<path d="M16 60l15-17 9.5 10 7.5-7.5L68 60z" fill="' + c.image + '"/>' +
      '<circle cx="57" cy="36" r="5.5" fill="' + c.image + '"/>', "JPG", c.image),
    "objet-audio": page('<path d="M38 54.5V34l20-4.5v20" stroke="' + c.audio + '" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>' +
      '<circle cx="33.5" cy="55" r="5.5" fill="' + c.audio + '"/><circle cx="53.5" cy="50" r="5.5" fill="' + c.audio + '"/>', "MP3", c.audio),
    "objet-zip": page('<path d="M40 4v8h4v8h-4v8h4v8h-4v8h4" stroke="' + c.zip + '" stroke-width="3"/>' +
      '<rect x="36" y="44" width="12" height="14" rx="3" fill="' + c.zip + '"/>', "ZIP", c.zip)
  });
})();
