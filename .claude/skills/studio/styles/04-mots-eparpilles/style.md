# Style n°4 · Mots éparpillés · d'après ElevenLabs (https://x.com/ElevenLabs/status/2100262886916358361)

**Ce qu'on voit :** un avant / après en deux mondes. L'avant est un papier clair quadrillé où la phrase du problème arrive un mot à la fois, éparpillée sur la grille ; avec chaque mot, une case de la grille surgit (une forme simple à ses couleurs, ou sa vraie matière : ses photos, les logos de ses outils) ; il est coupé d'écrans de nuit tramés où tombe la pastille de ce qu'il rate, chaque bascule se faisant en carrés de pixels. Puis la phrase pivot sur sa couleur pleine, qui se resserre en disque, bat et s'ouvre sur l'après : sa couleur, où une conversation arrive en bulles, avant une fin de nuit où un cadre au trait s'allume, devient les cartes de l'offre, puis le nom.
**Souvent utile pour :** un avant / après (la corvée d'avant, la vie avec l'offre), une offre qui répond, accompagne ou automatise (un assistant, un coaching, un logiciel), une vidéo de page ou une pub.

**D'après :** « Reception » d'ElevenLabs · 16:9 · 33 s · voix off, conversation jouée et musique douce.
**Mesures de l'original** (`studio_motion.py reference`) : 1,19 événement par seconde, écart médian 0,60 s, 23 coupes franches (presque toutes dans les transitions en pixels), image figée la plus longue 5,1 s (la fin noire).
**Mesures de l'essai du kit** (les 4 scènes bout à bout, 23,9 s, marque LMDM, 06/11/2026) : `rythme` 1,43 événement par seconde en 16:9 (écart médian 0,60 s), 1,58 en 9:16 (0,40 s), aucune image figée ; `palette` « ok » dans les deux formats.

> On reprend la grammaire (rythme, mises en page, typographie, mouvements, transitions, façon de
> montrer le produit), jamais le contenu : ni ses textes, ni ses objets, ni ses téléphones, ni ses
> couleurs, ni son logo, ni sa voix, ni sa musique. Ses images (les objets en 3D, les écrans tramés
> de couleurs, l'orbe) ne se redessinent pas : sa vraie matière les remplace, ou une forme simple.
> Tout passe aux couleurs et aux polices de la marque du client.

## 1. Le rythme

- **Deux tempos.** L'avant est haché : un mot toutes les 0,3 à 0,4 s, une case avec chaque mot, une transition en pixels toutes les 1,2 à 1,9 s (papier, écran, papier, écran, papier). L'après respire : une bulle toutes les 1,2 s, ses mots qui s'allument à 0,07 s d'écart, le fil qui remonte.
- **Le pivot est la seule pause voulue** : la phrase pivot se lit sur sa couleur (1 s), puis tout se resserre en disque ; le disque tient 1,5 s en vivant (il se pose, bat deux fois, ses anneaux répondent).
- **L'original est calme** (1,19 événement par seconde, des textes minuscules, 5 s de noir à la fin) : le kit le resserre pour passer le contrôle `rythme` du studio (cinq transitions en pixels en 7,4 s, des cases de sa nuit qui surgissent avec les mots, une pastille claire sur chaque écran, des points qui annoncent chaque réponse, des bulles de sa nuit sur sa couleur, une carte de résultat, le fond du cadre qui s'éclaircit à chaque mot de l'appel).
- **Le contrôle** : sur ce style, un mot seul, une case grise ou une forme de sa couleur sur le papier clair ne comptent pas comme un événement (trop peu de contraste à l'image) ; ce sont les formes de sa nuit qui surgissent, les carrés de pixels, les changements de fond, les bulles sombres et les recadrages qui font le rythme. Garde une ou deux formes de sa nuit par phrase (ou une vraie matière contrastée), sur les mots qui comptent.

## 2. Les gestes signature et leur place

La structure vient de la vidéo du client, jamais de l'original ([../README.md](../README.md),
« Appliquer un style ») : chaque scène de son plan prend le geste qui sert son rôle, les autres se
construisent dans la grammaire des sections 3 à 7. Au moins trois gestes par vidéo (deux sous
15 s) ; le détail de chaque mouvement est en section 5.

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| Les mots éparpillés et leurs cases | un mot à la fois sur le papier quadrillé ; avec chaque mot, une case de la grille qui surgit : une forme simple à ses couleurs (la case pleine, un disque, un cadre) ou sa vraie matière (ses photos, les logos de ses outils) | accroche, problème (l'avant) | `mots-objets` |
| La transition en pixels | des carrés qui basculent un à un et découvrent le plan suivant, sans fondu | raccord entre deux plans | `mots-objets` |
| L'écran de nuit et sa pastille | sa nuit tramée de tirets, la pastille claire de ce qu'il rate qui tombe, s'empile et vibre ; avec sa vraie capture, le téléphone incliné qui monte et vibre | le problème vécu, une notification | `mots-objets` |
| Le pivot en disque | la phrase pivot sur sa couleur pleine, qui se resserre en un disque plein entre trois anneaux fins, bat, puis s'ouvre sur l'après | la bascule avant / après, le nom de l'offre | `orbe-pivot` |
| Les messages | une conversation en bulles pleines sur sa couleur (l'offre dans sa nuit, son logo pour avatar), les points qui annoncent chaque réponse, le résultat qui arrive et se coche, puis sa couleur qui se referme en disque | solution, démonstration, preuve (un vrai échange) | `messages-verre` |
| Le cadre qui devient l'offre | le cadre qui se trace et s'allume à chaque mot de l'appel, les trois cartes de l'offre, le trait de sa couleur, le nom, le bouton cliqué | offre, appel | `fin-cadre` |

Sans avant / après dans son plan, le pivot en disque sert à révéler le nom de l'offre (`NOM`,
écrit dans le disque). Le motif papier / écran se répète une fois par besoin.

### L'original, pour mémoire

Scène par scène, un exemple et pas un plan à suivre (ses images ne se refont pas : section « Ce
qui ne se fera pas à l'identique ») :

| Bloc | Rôle | Durée | Ce qui s'y passe |
|---|---|---|---|
| Papier 1 | accroche, le problème | 1,9 s | Un mot à la fois sur la grille, un objet du quotidien en 3D qui surgit avec chaque mot ; dans le kit, une case à ses couleurs ou sa vraie matière (`mots-objets.html`) |
| Écran 1 | le problème vécu | 1,3 s | Transition en pixels ; l'écran tramé de couleurs, un téléphone de bureau qui vibre, la pastille de verre de ce qui arrive (« NOUVELLE DEMANDE ») ; dans le kit, sa nuit tramée et la pastille claire |
| Papier 2 | le problème, encore | 1,3 s | Une deuxième phrase courte, d'autres objets (d'autres cases) |
| Écran 2 | le problème qui coûte | 1,1 s | Le téléphone sous un autre angle, une autre pastille (« APPEL MANQUÉ ») |
| Papier 3 | la chute du problème | 1,4 s | La phrase qui fait mal, entourée de tous les objets ; puis les carrés d'un dégradé chaud envahissent l'écran (dans le kit, sa couleur pleine) |
| Le pivot | bascule | 4 s | La phrase pivot sur le dégradé (« Ça, c'était avant. »), le dégradé devient un orbe lumineux dans ses anneaux, l'orbe change de couleur et s'ouvre ; dans le kit, sa couleur qui se resserre en disque plein (`orbe-pivot.html`) |
| La conversation | solution, démonstration | 6 s | Les bulles de verre sur le dégradé de l'après ; l'offre répond, le résultat arrive et se coche ; dans le kit, des bulles pleines sur sa couleur (`messages-verre.html`) |
| La fin | offre et appel | 6,5 s | Le cadre au trait, la phrase d'appel ; le cadre devient les trois cartes de l'offre, qui deviennent un trait, puis le nom et le bouton (`fin-cadre.html`) |

### Des enchaînements qui marchent

Des points de départ quand le plan s'y prête, jamais une obligation.

L'original répète le motif papier / écran trois fois sur 13 s (trois besoins, trois écrans) ; une vidéo de page de 45 à 60 s peut faire de même (une ligne de `PAPIERS` et d'`ECRANS` par besoin), puis allonger la conversation (deux échanges) avant la fin.

## 3. Les fonds et les couleurs

| Dans l'original | Son rôle | Chez le client |
|---|---|---|
| Papier blanc cassé, grille grise de 100 px, cases gris clair | le monde d'avant, calme | sa couleur claire (`var(--brand-clair)`), une grille en noir à 6 %, les cases en noir à 5,5 % |
| Objets du quotidien en 3D, en couleurs, sur les cases | le quotidien du problème | ses vraies photos détourées ou les logos de ses outils ; sinon des formes simples qui prennent la case : pleine de sa couleur (`var(--brand-accent)`) ou de sa nuit (`var(--brand-sombre)`), un disque, un cadre au trait, un point |
| Trame bleu-vert en tirets, téléphones de bureau | l'écran où le problème arrive | sa nuit sous une trame de tirets blancs à 5 % où passent deux lumières blanches en transparence ; la pastille pleine en `var(--brand-clair)`, texte `var(--brand-sombre)`, son point de sa couleur ; un téléphone seulement autour de sa vraie capture |
| Dégradé rouge-orange vif | l'alerte, la bascule | sa couleur pleine, sans dégradé ; la phrase pivot en `var(--brand-contrast)` |
| Noir, anneaux fins, orbe lumineux | le vide autour de l'orbe | sa nuit, trois anneaux en blanc à 22 %, un disque plein de sa couleur, sans lueur ni cœur blanc |
| Dégradé vert, bleu, jaune, flou | l'après | sa couleur pleine, en aplat |
| Bulles de verre clair, texte blanc | la conversation | des bulles pleines : celles de l'offre et la carte du résultat dans sa nuit (texte `var(--brand-clair)`), celles du client en `var(--brand-clair)` (texte `var(--brand-sombre)`) ; son logo pour avatar, sur un disque de sa nuit |
| Fondu au noir | isoler l'appel | sa couleur se referme en disque sur sa nuit (un fondu de sa couleur vers sa nuit passerait par l'olive ou le brun) |
| Cartes en dégradé vert-jaune, trait lumineux, logo blanc | l'offre, la signature | le cadre en blanc à 30 %, puis un trait plein et fin de sa couleur, son fond qui s'éclaircit d'un gris ; les cartes, le trait et le bouton en sa couleur pleine (texte `var(--brand-contrast)`) ; le nom en `var(--brand-clair)` |

**Sur n'importe quelle marque, claire ou sombre.** Toutes les couleurs viennent de
`brand/tokens.css` : sa nuit (`--brand-sombre`, sa couleur la plus sombre : son fond s'il est
sombre, son texte s'il est clair), son clair (`--brand-clair`), sa couleur (`--brand-accent`) et des
neutres (`--brand-gris-1` à `--brand-gris-4`, du noir et du blanc en transparence). Rien ne se tire
de l'accent : ni teinte voisine, ni dégradé vers lui, ni accent en transparence ou en halo (avec un
jaune, cela donne du brun, de l'olive ou de l'orangé : story refusée du 06/11/2026). Sur une marque
claire, la nuit est son texte : les écrans, le disque et la fin gardent une nuit. Tout texte garde
un contraste d'au moins 4,5:1 : sur sa couleur, `var(--brand-contrast)` ; sur sa nuit,
`var(--brand-clair)` (`var(--brand-accent-lisible)` pour un mot à sa couleur) ; sur son clair,
`var(--brand-sombre)`.

## 4. La typographie

- **Police** : celle de la marque, en graisse **400** pour les mots de l'avant, la phrase pivot et la phrase d'appel ; **600** pour le bouton. L'original utilise une linéale grotesque fine et ronde ; si la marque n'impose rien : **Inter** (400, déjà livrée pour les interfaces), ou **Inter Tight** pour les grands mots.
- **Les bulles, les pastilles et les cartes** : Inter (`assets/fonts/interfaces.css`), comme une vraie interface.
- **Casse** : celle de la phrase, en minuscules ; les pastilles en capitales, approche +5 %.
- **Placement** : les mots de l'avant ne sont jamais alignés : chacun à sa place sur la grille de 100 px, en zigzag, lus de gauche à droite ; la phrase pivot et la phrase d'appel au centre ; les bulles à gauche (l'offre) et à droite (le client).

| Élément | 1920 × 1080 | 1080 × 1920 |
|---|---|---|
| Mots de l'avant | 104 px | 96 px, deux ou trois rangées dans la bande du milieu |
| Pastille d'un écran | 48 px, capitales | 48 px |
| Phrase pivot | 76 px, en `var(--brand-contrast)` | 64 px |
| Texte des bulles | 38 px (Inter 500) | 44 px (testé) |
| Étiquette d'une bulle | 22 px | 26 px |
| Phrase d'appel dans le cadre | 70 px | 64 px, sur deux lignes |
| Nom final | 104 px | 88 px |
| Bouton | 40 px dans une pilule de 96 px | 44 px dans une pilule de 104 px |

L'original écrit beaucoup plus petit (des bulles de 22 px, une phrase d'appel de 24 px) : le kit agrandit pour la lecture sur un téléphone et pour le contrôle du rythme.

En pub (vue sur un téléphone, souvent sans le son) : rien à lire sous 28 px. La carte du résultat passe à 38 et 28 px (essai du 03/11/2026) ; la pastille et les bulles y sont déjà.

## 5. Les mouvements signature

1. **Les mots éparpillés et leurs cases** (`mots-objets.html`) : chaque mot se tape en 0,1 à 0,2 s à sa place sur la grille, 0,35 à 0,4 s après le précédent ; avec lui, une case surgit (×0,55 à ×1 en 0,3 s, `back.out(1.8)`) : une forme qui prend toute la case, ou sa vraie matière posée sur la case grise ; ce qui est posé flotte (8 px, `sine.inOut` ; une photo ou un logo tourne aussi de 3 degrés, une forme reste d'équerre avec la grille) ; le papier pousse doucement (×1,00 à ×1,03 en 2,2 s).
2. **La transition en pixels** (`mots-objets.html`, cinq fois) : 144 carrés de 120 px ; chaque carré bascule à son seuil (55 % de hasard à graine, 45 % de balayage de gauche à droite), en 0,4 s, à vitesse constante. Le plan suivant apparaît à travers les carrés (`clip-path`), sans fondu.
3. **L'écran de nuit et sa pastille** (`mots-objets.html`) : une trame de tirets blancs à 5 % (4 × 9 px tous les 7 × 12 px), deux lumières blanches en transparence qui passent dessous (160 et 90 px en 2 s) ; la pastille glisse (34 px, 0,4 s, `expo.out`), deux pastilles vides s'empilent derrière elle (0,35 s, 0,09 s d'écart), tout vibre six fois (0,06 s, 2,2 degrés) et son point bat deux fois. Avec sa vraie capture, le téléphone (CSS 3D, incliné de 24 degrés) monte de 80 px en 1,4 s (`power2.out`) et vibre six fois (3 degrés) à côté de la pastille.
4. **Le pivot en disque** (`orbe-pivot.html`) : à chaque mot de la phrase pivot, sa couleur bat (un voile blanc de 14 % qui s'éteint en 0,35 s) ; elle se resserre en disque (rayon 1 250 → 300 px en 0,6 s, `power3.inOut`, puis → 175 px en 0,8 s, `expo.out`), trois anneaux apparaissent (0,6 s, 0,08 s d'écart) ; le disque bat deux fois (×1,04 puis ×1,06, `back.out`), les anneaux répondent au second battement, puis il s'ouvre sur tout l'écran (0,85 s, `power3.in`) pendant que les anneaux s'éloignent.
5. **Les messages** (`messages-verre.html`) : trois points qui sautent annoncent chaque réponse (0,38 s avant), la bulle se pose (26 px, flou de 8 px, 0,45 s, `expo.out`), ses mots s'allument un à un (0,07 s d'écart, depuis 22 % d'opacité), l'avatar bat, le fil remonte (0,5 s) et la caméra recadre (×1,08 → ×1, puis ×1,05 et ×0,97) ; la carte de résultat arrive, sa barre se remplit (0,7 s) et se coche (`back.out(2.5)`) ; à la fin, sa couleur se referme en disque sur sa nuit (0,6 s, `power3.in`).
6. **Le cadre qui devient l'offre** (`fin-cadre.html`) : le cadre se trace (blanc à 30 %, 0,7 s, `power2.inOut`), chaque mot de l'appel monte du flou (0,3 s) et allume un peu plus le cadre (son trait plein de sa couleur en fait le tour par paliers, son fond prend 4,5 % de blanc de plus), les mots s'effacent dans le désordre (0,07 s d'écart), le cadre se resserre en carte (0,55 s, `expo.inOut`), qui se remplit de sa couleur depuis son centre (0,4 s), deux cartes en sortent (±420 px, 0,55 s), les trois se rejoignent (0,4 s), s'aplatissent en un trait de sa couleur (0,45 s, `expo.in`), le nom sort du flou (0,6 s), le bouton saute (`back.out(2)`), le curseur le clique.

## 6. Les transitions

- **Les carrés de pixels** entre le papier et les écrans, et pour entrer dans sa couleur pleine : la transition signature, toujours sur un temps de la musique.
- **Le disque** : sa couleur plein écran se resserre en disque, le disque s'ouvre en couleur plein écran (l'avant devient l'après par le même objet) ; après la conversation, sa couleur se referme en disque sur sa nuit, pour isoler l'appel.
- **Le morphing de la fin** : le cadre devient une carte, la carte trois cartes, les cartes un trait, le trait le soulignement du nom.
- Jamais de fondu enchaîné entre deux plans chargés, ni de fondu de sa couleur vers sa nuit : les carrés de pixels et le disque font ce travail.

## 7. Le produit à l'écran

- **Le problème** se montre par sa vraie matière, fournie pour la vidéo : ses photos d'objets détourées et les logos des outils de sa corvée sur les cases, la capture de son téléphone ou de sa boîte de réception dans le téléphone de l'écran. Sans elle, par les mots, les cases à ses couleurs et la pastille de ce qu'il rate. Jamais un objet ni un écran redessinés.
- **L'offre** se montre par sa présence (sa couleur, le disque, son logo en avatar) et par **une vraie conversation** : son assistant qui répond, ses vrais échanges avec des clients, une vraie question de sa FAQ et sa vraie réponse ; puis **la carte du résultat** (ce que le produit rend vraiment : une page, un plan, un rendez-vous, une vidéo).
- **Le contenu de l'offre** se montre en trois cartes (ses trois parties réelles), comme les trois offres de l'original.
- Jamais une conversation inventée présentée comme vraie : sans échange réel, la scène montre une question de sa FAQ et la réponse de sa page.

## 8. Le son

- **Original** : une voix off chaleureuse dit la phrase du problème, et chaque mot apparaît au moment où il est dit ; pendant les messages, la conversation est jouée à deux voix (la voix de synthèse de l'offre et celle du client) ; une musique douce derrière, tempo estimé autour de 104 battements par minute, sans montée forte.
- **Chez le client** : texte et musique par défaut (une musique de lancement calme puis lumineuse, 95 à 110 battements par minute) ; les mots et les transitions en pixels se calent sur ses temps. Une voix off seulement à sa demande ([voix.md](../../references/voix.md)) : chaque mot de l'avant apparaît alors quand il est dit, et la conversation peut se jouer à deux voix.
- **Bruitages** : un petit tic par case qui surgit, un grésillement bref sur chaque transition en pixels, une vibration sourde sous la pastille des écrans, une nappe qui monte pendant le pivot et un impact doux quand le disque s'ouvre, une bulle douce par message, un clic sur le bouton.
- **Ambiance proposée** à la page des styles et des musiques (`musiques choisir --style 4`) : « Premium et calme » puis « Montée cinématique », jamais imposée (une ambiance qu'il demande passe devant).

## 9. L'ouverture et la fin

- **Original** : il s'ouvre sur le papier vide, le premier mot tapé lettre à lettre au centre ; il finit sur le logo au-dessus d'un trait lumineux, puis le noir (5 s en tout).
- **Chez le client** : pour une vidéo de page, la première image doit déjà dire le sujet : avance les instants du premier mot et de la première case à 0 (ils sont là dès la première image). La fin garde le nom et le trait, et ajoute le bouton que le curseur clique ; le nom et le bouton tiennent 2 s au moins, sans le long noir de l'original.

## Ce qui ne se fera pas à l'identique

- **Les images de l'original ne se refont pas.** Ses objets photoréalistes (des rendus 3D : bouteille, casque, cône, clavier, tasse), ses téléphones de bureau, les couleurs tramées de ses écrans et son orbe fluide ne se redessinent jamais, ni en 3D, ni en dessin simplifié. À leur place, sa vraie matière fournie pour la vidéo (ses photos d'objets détourées, les logos de ses outils, la capture de son téléphone), sinon des formes simples à ses couleurs (la case pleine, un disque, un cadre au trait, un point) et une pastille de texte.
- **La vraie trame** (des points de tailles variables selon la lumière) → des tirets blancs très pâles sur sa nuit : la texture de l'écran, sans image dessous.
- **L'orbe fluide** (une matière lumineuse qui coule) → un disque plein de sa couleur dans ses anneaux, sans lueur ni cœur blanc.
- **Les dégradés vifs** (l'alerte, l'après, les cartes) et le trait lumineux → sa couleur pleine, en aplat, et un trait plein et fin.
- **Les bulles de verre** → des bulles pleines : sur un aplat, le verre ne se voit pas, et un verre clair sur sa couleur la pâlirait.
- **La voix off et la conversation jouée** → texte et musique par défaut.
- **Les petits textes et les 5 s de noir** de l'original → agrandis et raccourcis pour la lecture et le contrôle du rythme.
- **Les trois familles de couleurs** (bleu, rouge, vert) → ses couleurs seules : sa couleur pleine, sa nuit, son clair et des gris.

## Sur une autre offre

Le style est une façon de présenter : il se monte sur n'importe quelle offre. Ce qui suivait l'original (un standard téléphonique tenu par une IA) s'adapte :

- **Toujours** : le papier quadrillé, les mots éparpillés et leurs cases, les écrans de nuit et leurs pastilles, les carrés de pixels, la phrase pivot, le disque, l'après sur sa couleur, une conversation en bulles, le cadre qui devient l'offre.
- **Une formation** : sur les cases, sa vraie matière (les miniatures de ses vidéos, les logos des outils qu'il enseigne), sinon les formes à ses couleurs ; la pastille dit ce qu'il rate (« ENCORE REPORTÉ », « PAS COMMENCÉ ») ; la conversation est une vraie question d'élève et la vraie réponse du formateur ou de l'assistant de la formation ; la carte du résultat est le module terminé ou le vrai livrable ; les trois cartes, ses trois parties.
- **Un coaching** : la capture de son agenda ou de ses messages en retard dans le téléphone de l'écran, s'il la fournit ; la pastille « NOUVEAU MESSAGE » ; la conversation, un vrai échange avec un client (avec son accord) ou un vrai témoignage en messages ; la carte, la séance réservée ; les trois cartes, ses formats d'accompagnement.
- **Un logiciel** : les logos des outils qu'il remplace sur les cases ; la pastille, l'alerte qu'il évite ; la conversation, son vrai assistant ou ses vraies notifications ; la carte, son vrai résultat ; les trois cartes, trois fonctions ou trois formules.

## En vertical et en carré

- **9:16 : chaque scène a sa version verticale** (`mots-objets-vertical.html`, `orbe-pivot-vertical.html`, `messages-verre-vertical.html`, `fin-cadre-vertical.html`), remise en page et jamais recadrée. Les quatre bout à bout en 1080 × 1920 font 23,9 s (essai du 06/11/2026 sur LMDM : `rythme` « ok », 1,58 événement par seconde, écart médian 0,40 s, aucune image figée, `palette` « ok », raccords image pour image).
- **Le papier en 9:16** (`mots-objets-vertical.html`) : les mots à 96 px, en deux ou trois rangées dans la bande du milieu (de 780 à 1 100 px dans le kit, 600 à 1 300 au plus), 8 lettres au plus par mot ; les cases dans les bandes du haut et du bas (200 à 300 px sur la grille de 100 px : x = 40, 140…, y = 60, 160…), quelques petites cases sur les bords : l'écran est rempli de haut en bas. Les carrés de pixels restent à 120 px (9 colonnes, 16 rangées). Sur les écrans, la pastille au centre ; avec sa vraie capture, le grand téléphone (500 × 1 000 px, centré, même inclinaison) et la pastille au-dessus de lui.
- **Le disque en 9:16** (`orbe-pivot-vertical.html`) : centré, un peu plus grand (rayon de 320 px, puis 200 px), anneaux plus larges (460, 740 et 1 080 px) qui occupent la hauteur ; la phrase pivot passe à 64 px.
- **La conversation en 9:16** (`messages-verre-vertical.html`) : elle remplit l'écran comme sur un téléphone : colonne de 968 px, bulles de 44 px, le fil part du milieu et remonte de 560 px en tout, le recadrage est plus doux (×1,03).
- **En pub 9:16** (zone sûre : y de 269 à 1 248, `zones pub`) : les versions verticales sont calées pour un Reel. Remonte la conversation (`BAS` à 880 au lieu de 1 020) et toute la fin de 100 px (une enveloppe `top: -100px` marquée `data-layout-allow-overflow`), les cartes à ±280 px ; la fin ne dessine pas de bouton : « Découvre-le » et une flèche vers le bas à sa place, sans curseur (structures.md, publicité). Essai du 03/11/2026.
- **La fin en 9:16** (`fin-cadre-vertical.html`) : le cadre fait 960 × 700 px, la phrase d'appel à 64 px passe sur deux lignes centrées (« | » dans `APPEL` marque le retour à la ligne) ; les trois cartes (720 × 240 px) sortent au-dessus et au-dessous de la première, s'empilent en colonne, puis la colonne s'aplatit en un trait de 860 px ; le nom à 88 px au-dessus, le bouton (pilule de 104 px, texte de 44 px) dessous, vers le milieu de l'écran.
- **4:5 et 1:1** : comme le 16:9 resserré ; 9 colonnes de carrés, les cases seulement sur les côtés, deux cartes au lieu de trois en 1:1 si le texte ne tient pas.
- Les mots clés restent hors des 10 % du haut et des 20 % du bas en vertical (les commandes de l'application).

## Les compositions du kit

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace |
|---|---|---|---|
| `compositions/mots-objets.html` | 7,4 s | L'avant : trois papiers (mots éparpillés et leurs cases), deux écrans de nuit avec leur pastille, reliés par cinq transitions en pixels, puis l'entrée de sa couleur pleine | L'id `t04-mots`, `PAPIERS` (les mots, leur place, leurs cases : une forme ou sa vraie matière, et leurs instants), `ECRANS` (la pastille, sa place, et sa vraie capture s'il en a une) |
| `compositions/orbe-pivot.html` | 4,0 s | La bascule : la phrase pivot sur sa couleur qui bat, le disque plein, les anneaux, les deux battements, l'ouverture sur l'après | L'id `t04-orbe`, `PIVOT` (une phrase courte et ses instants), `NOM` (s'il doit apparaître dans le disque), `MOMENTS` si la musique l'exige |
| `compositions/messages-verre.html` | 6,0 s | L'après : la conversation en bulles pleines sur sa couleur, les points qui annoncent les réponses, la carte du résultat qui se coche, puis sa couleur qui se referme en disque sur sa nuit | L'id `t04-msg`, `MESSAGES` (un vrai échange), `ETIQUETTE`, `LOGO`, `CADENCE`, `RESULTAT` (ou `null`) |
| `compositions/messages-verre-vertical.html` | 6,0 s | La même conversation en 9:16 | Comme la version 16:9 |
| `compositions/fin-cadre.html` | 6,5 s | L'offre et l'appel : le cadre qui s'allume, sa phrase, les trois cartes, le trait, le nom, le bouton cliqué | L'id `t04-fin`, `APPEL`, `CARTES` (les trois parties réelles de l'offre), le nom (ou son logo en `<img>`), le libellé du bouton |
| `compositions/mots-objets-vertical.html` | 7,4 s | L'avant en 9:16 : les mots dans la bande du milieu, les cases en haut et en bas, la pastille au centre des écrans, les carrés de pixels en 9 × 16 | Comme la version 16:9 ; les places des mots et des cases suivent la grille verticale (en-tête du fichier) |
| `compositions/orbe-pivot-vertical.html` | 4,0 s | La bascule en 9:16 : le disque centré, plus grand, ses anneaux sur toute la hauteur | Comme la version 16:9 |
| `compositions/fin-cadre-vertical.html` | 6,5 s | L'offre et l'appel en 9:16 : le cadre de 960 × 700 px, la phrase sur deux lignes, les trois cartes empilées, le trait, le nom, le bouton cliqué | Comme la version 16:9 ; trois cartes |

Bout à bout dans cet ordre, elles font une vidéo de 23,9 s qui se tient seule, en 16:9 comme en 9:16 avec les versions `-vertical` (essais : `rythme` « ok », `palette` « ok », `check` sans erreur). Les raccords sont faits dans les deux formats : la fin de `mots-objets` est la première image de `orbe-pivot` (sa couleur pleine plein cadre), la fin de `orbe-pivot` celle de `messages-verre` (sa couleur pleine), et `messages-verre` finit sur sa nuit, où commence `fin-cadre`. Un format = une seule famille de fichiers : en 9:16, monte les quatre `-vertical`, jamais une scène 16:9.
