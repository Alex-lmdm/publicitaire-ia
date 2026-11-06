# Style n°4 · Mots éparpillés · d'après ElevenLabs (https://x.com/ElevenLabs/status/2100262886916358361)

**Ce qu'on voit :** un avant / après en deux mondes. L'avant est un papier clair quadrillé où une phrase complète du problème arrive un mot à la fois, éparpillée sur la grille, puis reste le temps de la lire ; avec ses mots, puis sur les temps de sa tenue, des cases de la grille surgissent, et chacune porte sa vraie matière (une capture de sa page en vignette, une image de sa vraie vidéo, un vrai chiffre qui compte, le vrai logo d'un outil de sa corvée) ; il est coupé d'écrans de nuit tramés où tombe la pastille de ce qu'il vit, près de sa vraie capture inclinée, chaque bascule se faisant en carrés de pixels. Puis la phrase pivot sur sa couleur pleine, qui se resserre en un disque autour d'elle pendant qu'on la lit, puis porte son logo et le nom de l'offre, bat et s'ouvre sur l'après : sa couleur, où une vraie conversation arrive en bulles (le lien de sa page, ses choix, le résultat qui se coche), avant une fin de nuit où un cadre au trait s'allume, devient les cartes de l'offre, puis le nom.
**Souvent utile pour :** un avant / après (la corvée d'avant, la vie avec l'offre), une offre qui répond, accompagne ou automatise (un assistant, un coaching, un logiciel), une vidéo de page ou une pub.

**D'après :** « Reception » d'ElevenLabs · 16:9 · 33 s · voix off, conversation jouée et musique douce.
**Mesures de l'original** (`studio_motion.py reference`) : 1,19 événement par seconde, écart médian 0,60 s, 23 coupes franches (presque toutes dans les transitions en pixels), image figée la plus longue 5,1 s (la fin noire).
**Mesures de l'essai du kit** (les 4 scènes bout à bout, 59,5 s, marque LMDM, la vraie matière de la story d'ouverture de Publicitaire IA, 06/11/2026) : `rythme` 1,06 événement par seconde en 16:9 (écart médian 0,70 s), 1,09 en 9:16 (0,80 s), aucune image figée ; `palette` « ok » dans les deux formats ; marque claire (Dupliq.me, accent orange) vérifiée par captures.

> On reprend la grammaire (mises en page, typographie, mouvements, transitions, façon de montrer
> le produit), jamais le contenu : ni ses textes, ni ses objets, ni ses téléphones, ni ses
> couleurs, ni son logo, ni sa voix, ni sa musique, ni son tempo haché. Ses images (les objets en
> 3D, les écrans tramés de couleurs, l'orbe) ne se redessinent pas et ne deviennent pas des formes
> seules : sa vraie matière les remplace, prise en descendant l'échelle de
> [style.md](../../references/style.md) (« Aucune image inventée »). Tout passe aux couleurs et aux
> polices de la marque du client.

## 1. Le rythme

- **La lecture d'abord.** Chaque papier pose sa phrase un mot à la fois (un mot toutes les 0,25 s), puis la tient le temps de la lire (`studio_motion.py lecture` : 0,3 s par mot + 0,8 s, jamais moins de 1,5 s) ; chaque écran de nuit pose sa pastille (1 s) puis la tient le temps de la lire ; chaque bulle reste le temps de la lire avant que la suivante n'arrive. Jamais le tempo de l'original (un papier toutes les 1,2 à 1,9 s, des bulles toutes les 1,2 s) : la story refusée du 06/11/2026 tombait dans ce piège (« beaucoup trop rapide »). Les scènes du kit calculent leurs instants depuis leurs textes et affichent leur durée (console, et `check`).
- **Le rythme vient de ce qu'on montre, jamais de la caméra.** Pendant qu'on lit, la caméra ne fait qu'une dérive lente (le papier pousse de ×1,03 sur toute sa tenue, la conversation de ×1,03 sur toute la scène) ; aucun recadrage, ni dans les cinq premières secondes ni sous un texte qu'on lit. La vie vient d'événements de contenu : les cases de vraie matière qui arrivent sur les temps de la tenue (« tenue 1, 2… »), le mot clé surligné, la capture de l'écran de nuit qui vibre à chaque appel et ses lumières qui passent, sa couleur qui se resserre en disque autour de la phrase pivot, le disque qui porte son logo et bat, l'aperçu de sa page qui défile section par section, ses mots de bulle qui s'allument au rythme de la lecture, ses cartes de choix, la carte choisie qui s'allume, les vignettes du résultat qui se cochent, ses vrais logos d'outils qui arrivent un à un dans les marges, le cadre qui s'allume à chaque mot de l'appel, les cartes de l'offre qui sortent l'une après l'autre et battent à leur tour.
- **Les bascules se font entre deux phrases** : les carrés de pixels, le disque qui s'ouvre, le fil qui remonte quand une nouvelle bulle arrive. Un `rythme` trop bas se corrige en ajoutant une case de vraie matière sur un temps de la tenue, une capture de plus, un logo de plus, jamais un recadrage.
- **Le contrôle** : `rythme` ne voit que ce qui change franchement à l'image. Une case grise, un logo au trait fin (ChatGPT), un mot qui s'allume, un surlignage jaune sur le papier blanc comptent peu ; une capture sombre ou claire qui se pose sur un fond contraire, un logo plein (CapCut), un chiffre sur sa couleur, une bulle, une carte, l'aperçu qui défile comptent. Mets les matières contrastées sur les temps de la tenue.
- **Le piège de la palette** (essai du 06/11/2026) : sur sa couleur, rien ne se fond, ne se floute ni ne porte d'ombre sombre. Une bulle de sa nuit qui entre en fondu, un logo flou, une ombre noire sur son jaune passent par l'olive et le brun (`palette` relevait 13 % d'une image) : tout y paraît à pleine opacité et grandit (pop), les logos y sont nets, les bulles sans ombre.

## 2. Les gestes signature et leur place

La structure vient de la vidéo du client, jamais de l'original ([../README.md](../README.md),
« Appliquer un style ») : chaque scène de son plan prend le geste qui sert son rôle, les autres se
construisent dans la grammaire des sections 3 à 7. Au moins trois gestes par vidéo (deux sous
15 s) ; le détail de chaque mouvement est en section 5.

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| Les mots éparpillés et leurs cases | une phrase complète, un mot à la fois sur le papier quadrillé, tenue le temps de la lire ; ses cases surgissent avec ses mots puis pendant sa tenue, et chacune porte sa vraie matière (une capture en vignette, une image de sa vraie vidéo, un vrai chiffre qui compte, un vrai logo nu) ; son mot clé se surligne de sa couleur | accroche, problème (l'avant) | `mots-objets` |
| La transition en pixels | des carrés qui basculent un à un et découvrent le plan suivant, sans fondu, entre deux phrases | raccord entre deux plans | `mots-objets` |
| L'écran de nuit et sa pastille | sa nuit tramée de tirets, la pastille de ce qu'il vit qui tombe, s'empile et vibre, près de sa vraie capture inclinée dans une carte claire (ou un téléphone) qui monte et vibre à chaque appel | le problème vécu, ce qu'il coûte | `mots-objets` |
| Le pivot en disque | la phrase pivot sur sa couleur pleine, qui se resserre en un disque autour d'elle pendant qu'on la lit, son mot clé surligné de sa nuit ; puis le disque porte son logo et le nom de l'offre, bat deux fois et s'ouvre sur l'après (sans logo ni nom, une transition de moins d'une seconde) | la bascule avant / après, le nom de l'offre | `orbe-pivot` |
| Les messages | une vraie conversation en bulles pleines sur sa couleur (l'offre dans sa nuit, son logo pour avatar), le lien collé avec l'aperçu de sa vraie page qui défile, ses choix en cartes numérotées, la réponse qui en sélectionne une, le résultat et ses vraies vignettes qui se cochent ; ses vrais logos d'outils dans les marges ; puis sa couleur qui se referme en disque | solution, démonstration, preuve (un vrai échange) | `messages-verre` |
| Le cadre qui devient l'offre | le cadre qui se trace et s'allume à chaque mot de l'appel, tenu le temps de le lire, ses logos d'outils autour ; les trois cartes de l'offre qui sortent l'une après l'autre, le trait de sa couleur, le nom, le bouton cliqué | offre, appel | `fin-cadre` |

Sans avant / après dans son plan, le pivot en disque sert à révéler le nom de l'offre (`NOM`,
`LOGO`). Le motif papier / écran se répète une fois par besoin (`PLANS`, dans n'importe quel
ordre : trois écrans de suite pour trois options, par exemple).

### L'original, pour mémoire

Scène par scène, un exemple et pas un plan à suivre (ses images ne se refont pas : section « Ce
qui ne se fera pas à l'identique » ; ses durées non plus : section 1) :

| Bloc | Rôle | Durée | Ce qui s'y passe |
|---|---|---|---|
| Papier 1 | accroche, le problème | 1,9 s | Un mot à la fois sur la grille, un objet du quotidien en 3D qui surgit avec chaque mot ; dans le kit, une phrase complète tenue le temps de la lire, ses cases portant sa vraie matière (`mots-objets.html`) |
| Écran 1 | le problème vécu | 1,3 s | Transition en pixels ; l'écran tramé de couleurs, un téléphone de bureau qui vibre, la pastille de verre de ce qui arrive (« NOUVELLE DEMANDE ») ; dans le kit, sa nuit tramée, la pastille claire et sa vraie capture qui vibre |
| Papier 2 | le problème, encore | 1,3 s | Une deuxième phrase courte, d'autres objets (dans le kit, d'autres matières) |
| Écran 2 | le problème qui coûte | 1,1 s | Le téléphone sous un autre angle, une autre pastille (« APPEL MANQUÉ ») |
| Papier 3 | la chute du problème | 1,4 s | La phrase qui fait mal, entourée de tous les objets (dans le kit, de toutes les matières vues) ; puis les carrés d'un dégradé chaud envahissent l'écran (dans le kit, sa couleur pleine) |
| Le pivot | bascule | 4 s | La phrase pivot sur le dégradé (« Ça, c'était avant. »), le dégradé devient un orbe lumineux dans ses anneaux, l'orbe change de couleur et s'ouvre ; dans le kit, sa couleur qui se resserre en disque autour de la phrase, puis porte son logo et son nom (`orbe-pivot.html`) |
| La conversation | solution, démonstration | 6 s | Les bulles de verre sur le dégradé de l'après ; l'offre répond, le résultat arrive et se coche ; dans le kit, des bulles pleines sur sa couleur, un vrai échange (`messages-verre.html`) |
| La fin | offre et appel | 6,5 s | Le cadre au trait, la phrase d'appel ; le cadre devient les trois cartes de l'offre, qui deviennent un trait, puis le nom et le bouton (`fin-cadre.html`) |

### Des enchaînements qui marchent

Des points de départ quand le plan s'y prête, jamais une obligation.

- **Les options écartées** (l'essai du kit, la story d'ouverture de Publicitaire IA) : un papier pose le choix (« Pour avoir une vidéo, tu as trois options. ») pendant que les vignettes des trois options arrivent sur sa tenue ; trois écrans de nuit les montrent une à une (sa capture et sa pastille : « TE FILMER », « UN DEVIS DÈS 1 500 € », « UN WEEK-END DE MONTAGE ») ; un dernier papier dit ce qu'elles donnent, entouré de toutes les matières ; le pivot dit qu'il en existe une autre.
- **Trois besoins, trois écrans** (l'original) : le motif papier / écran trois fois ; une vidéo de page de 45 à 60 s peut faire de même, puis allonger la conversation (deux échanges) avant la fin.

## 3. Les fonds et les couleurs

| Dans l'original | Son rôle | Chez le client |
|---|---|---|
| Papier blanc cassé, grille grise de 100 px, cases gris clair | le monde d'avant, calme | sa couleur claire (`var(--brand-clair)`), une grille en noir à 6 %, les cases en noir à 5,5 % |
| Objets du quotidien en 3D, en couleurs, sur les cases | le quotidien du problème | sa vraie matière, du plus fort au plus faible : ses captures en vignettes (sa page, son produit, une image de sa vraie vidéo), ses vrais chiffres (le chiffre sur sa couleur pleine, texte `var(--brand-contrast)`), les vrais logos nus des outils de sa corvée, puis ses vrais mots ; la case grise, au trait, de sa nuit ou de sa couleur n'est qu'un cadre autour d'une matière, jamais seule |
| Trame bleu-vert en tirets, téléphones de bureau | l'écran où le problème arrive | sa nuit sous une trame de tirets blancs à 5 % où passent deux lumières blanches en transparence ; la pastille pleine en `var(--brand-clair)`, texte `var(--brand-sombre)`, son point de sa couleur ; sa vraie capture dans une carte claire inclinée (ou un téléphone, pour une capture de téléphone) |
| Dégradé rouge-orange vif | l'alerte, la bascule | sa couleur pleine, sans dégradé ; la phrase pivot en `var(--brand-contrast)`, son mot clé en `var(--brand-clair)` sur un bloc de sa nuit |
| Noir, anneaux fins, orbe lumineux | le vide autour de l'orbe | sa nuit, trois anneaux en blanc à 22 %, un disque plein de sa couleur qui porte son logo, sans lueur ni cœur blanc ; le nom dessous en `var(--brand-clair)` |
| Dégradé vert, bleu, jaune, flou | l'après | sa couleur pleine, en aplat, sans ombre ni flou (une ombre sombre sur son jaune fait de l'olive) |
| Bulles de verre clair, texte blanc | la conversation | des bulles pleines sans ombre : celles de l'offre, ses cartes de choix et la carte du résultat dans sa nuit (texte `var(--brand-clair)`), celles du client en `var(--brand-clair)` (texte `var(--brand-sombre)`, le lien en `var(--brand-gris-2)`) ; son logo pour avatar, sur un disque de sa nuit ; les logos de ses outils nets, dans leurs couleurs (un logo monochrome dans sa nuit) |
| Fondu au noir | isoler l'appel | sa couleur se referme en disque sur sa nuit (un fondu de sa couleur vers sa nuit passerait par l'olive ou le brun) |
| Cartes en dégradé vert-jaune, trait lumineux, logo blanc | l'offre, la signature | le cadre en blanc à 30 %, puis un trait plein et fin de sa couleur, son fond qui s'éclaircit jusqu'à 20 % de blanc ; les cartes, le trait et le bouton en sa couleur pleine (texte `var(--brand-contrast)`) ; le nom en `var(--brand-clair)` ; ses logos d'outils autour (un logo monochrome en clair) |

**Sur n'importe quelle marque, claire ou sombre.** Toutes les couleurs viennent de
`brand/tokens.css` : sa nuit (`--brand-sombre`, sa couleur la plus sombre : son fond s'il est
sombre, son texte s'il est clair), son clair (`--brand-clair`), sa couleur (`--brand-accent`) et des
neutres (`--brand-gris-1` à `--brand-gris-4`, du noir et du blanc en transparence). Rien ne se tire
de l'accent : ni teinte voisine, ni dégradé vers lui, ni accent en transparence ou en halo, ni
fondu, flou ou ombre sombre posés sur lui (avec un jaune, cela donne du brun, de l'olive ou de
l'orangé : story refusée du 06/11/2026, essai du 06/11/2026). Sur une marque claire, la nuit est
son texte : les écrans, le disque et la fin gardent une nuit. Tout texte garde un contraste d'au
moins 4,5:1 : sur sa couleur, `var(--brand-contrast)` ; sur sa nuit, `var(--brand-clair)`
(`var(--brand-accent-lisible)` pour un mot à sa couleur) ; sur son clair, `var(--brand-sombre)`.
Un logo d'outil qui se confond avec sa couleur (Claude sur un accent orange, essai Dupliq.me du
06/11/2026) se garde pour la nuit ou les marges claires, ou laisse la place à l'autre outil.

## 4. La typographie

- **Police** : celle de la marque, en graisse **400** pour les mots de l'avant, la phrase pivot et la phrase d'appel ; **600** pour les chiffres des cases, le nom sous le disque et le bouton. L'original utilise une linéale grotesque fine et ronde ; si la marque n'impose rien : **Inter** (400, déjà livrée pour les interfaces), ou **Inter Tight** pour les grands mots.
- **Les bulles, les cartes de choix, la pastille et les cartes de l'offre** : Inter (`assets/fonts/interfaces.css`), comme une vraie interface.
- **Casse** : celle de la phrase ; les pastilles en capitales, approche +5 %.
- **Placement** : les mots de l'avant ne sont jamais alignés : chacun à sa place sur la grille de 100 px, en zigzag sur deux ou trois rangées, lus de gauche à droite ; la phrase pivot et la phrase d'appel au centre, sur une ou deux lignes (« | ») ; les bulles à gauche (l'offre) et à droite (le client).

| Élément | 1920 × 1080 | 1080 × 1920 |
|---|---|---|
| Mots de l'avant | 104 px | 96 px, deux ou trois rangées dans la bande du milieu |
| Chiffre d'une case | 0,46 × sa hauteur au plus, selon sa longueur | idem |
| Pastille d'un écran | 48 px, capitales | 48 px |
| Phrase pivot | 76 px, deux lignes, en `var(--brand-contrast)` | 64 px |
| Nom sous le disque | 60 px | 64 px |
| Texte des bulles | 38 px (Inter 500) | 44 px |
| Lien collé, étiquette d'une bulle | 26 et 22 px | 30 et 26 px |
| Cartes de choix | 26 px | 28 px |
| Phrase d'appel dans le cadre | 70 px, deux lignes | 64 px, deux lignes |
| Cartes de l'offre | 32 px, ligne 24 px | 40 px, ligne 30 px |
| Nom final | 104 px | 88 px |
| Bouton | 40 px dans une pilule de 96 px | 44 px dans une pilule de 104 px |

L'original écrit beaucoup plus petit (des bulles de 22 px, une phrase d'appel de 24 px) : le kit agrandit pour la lecture sur un téléphone.

En pub (vue sur un téléphone, souvent sans le son) : rien à lire sous 28 px. La carte du résultat passe à 38 et 28 px (essai du 03/11/2026) ; la pastille et les bulles y sont déjà.

## 5. Les mouvements signature

1. **Les mots éparpillés et leurs cases** (`mots-objets.html`) : chaque mot se tape en 0,1 s au plus à sa place sur la grille, 0,25 s après le précédent ; la phrase complète tient le temps de sa lecture. Les cases arrivent avec un mot (« mot 3 ») ou sur les temps de la tenue (« tenue 1 » : 0,4 s après le dernier mot, puis toutes les 0,5 s) : la case surgit (×0,55 à ×1 en 0,3 s, `back.out(1.8)`), sa matière s'y pose 0,2 s après (un logo de ×0,5 à ×1, `back.out(2)` ; une capture qui se découvre de bas en haut, 0,45 s, `expo.out` ; un chiffre qui compte jusqu'à sa valeur en 0,9 s, `expo.out`), puis flotte (8 px, `sine.inOut` ; un logo tourne aussi de 3 degrés, une capture et un chiffre restent d'équerre). Les mots clés se surlignent d'un bloc de sa couleur (0,35 s, `expo.out`) 0,3 s après le dernier mot. Le papier pousse doucement pendant toute sa tenue (×1,00 à ×1,03, `sine.inOut`). Une case sans matière ne s'affiche pas.
2. **La transition en pixels** (`mots-objets.html`, à chaque plan) : 144 carrés de 120 px ; chaque carré bascule à son seuil (55 % de hasard à graine, 45 % de balayage de gauche à droite), en 0,4 s. Le plan suivant apparaît à travers les carrés (`clip-path`), sans fondu ; un plan recouvert en entier est masqué.
3. **L'écran de nuit et sa pastille** (`mots-objets.html`) : une trame de tirets blancs à 5 % (4 × 9 px tous les 7 × 12 px), deux lumières blanches en transparence qui la traversent pendant tout l'écran (520 et 260 px) ; la pastille glisse (34 px, 0,4 s, `expo.out`), deux pastilles vides s'empilent derrière elle (0,35 s, 0,09 s d'écart), la pile vibre une fois (six fois 0,06 s, 2,2 degrés) et son point bat deux fois, puis la pastille ne bouge plus pendant qu'on la lit. Sa vraie capture, dans une carte claire inclinée (14 px de marge, CSS 3D) ou un téléphone, monte de 80 px en 1,6 s (`power2.out`) et vibre à l'arrivée puis toutes les 0,9 s (six fois 0,06 s, 3 degrés). L'écran dure 1 s plus la lecture de sa pastille.
4. **Le pivot en disque** (`orbe-pivot.html`) : la phrase pivot s'écrit un mot toutes les 0,3 s (coupe sèche), sa couleur bat à chaque mot (un voile blanc de 14 % qui s'éteint en 0,35 s) ; 0,4 s après le dernier mot, sa couleur se resserre en un grand disque autour de la phrase (rayon 1 250 → 430 px en 0,7 s, `power3.inOut`), trois anneaux apparaissent (0,6 s, 0,08 s d'écart), le mot clé se couvre d'un bloc de sa nuit (0,35 s), le disque bat une fois (×1,03) ; la phrase lue sort d'un coup ; le disque se resserre (→ 175 px, 0,6 s, `expo.out`) et porte son logo (de ×0 à ×1 en 0,45 s, `back.out(1.8)`) et le nom dessous, tenus le temps de lire le nom (1,5 s au moins) ; il bat deux fois (×1,04 puis ×1,06), les anneaux répondent, le logo se replie, le disque s'ouvre sur tout l'écran (0,85 s, `power3.in`). Sans logo ni nom : resserré en 0,4 s, rouvert en 0,5 s.
5. **Les messages** (`messages-verre.html`) : trois points qui sautent annoncent chaque réponse (0,38 s avant) ; la bulle paraît à pleine opacité et se pose (26 px, ×0,94 à ×1, 0,45 s, `expo.out`, sans fondu ni flou sur sa couleur) ; ses mots s'allument au rythme de la lecture (0,3 s par mot, depuis 22 % d'opacité) ; la bulle suivante n'arrive qu'après sa lecture ; les cartes de choix arrivent en cascade (0,1 s d'écart) et leurs titres s'allument à leur tour ; la réponse du client allume la carte choisie (un contour clair, son numéro sur sa couleur) ; l'aperçu du lien (sa vraie page) défile d'une section toutes les 0,9 s (0,45 s, `expo.inOut`) tant qu'il est à l'écran ; le fil remonte à l'arrivée d'une bulle (0,5 s, `expo.out`) ; la carte du résultat arrive sous la dernière bulle, ses vignettes surgissent et se cochent une à une pendant sa lecture, sa barre se remplit, la carte se coche ; ses logos d'outils, nets, arrivent un à un dans les moments les plus calmes (0,4 s, `back.out(2)`) puis dérivent ; la caméra pousse de ×1,03 sur toute la scène ; à la fin, sa couleur se referme en disque sur sa nuit (0,6 s, `power3.in`).
6. **Le cadre qui devient l'offre** (`fin-cadre.html`) : le cadre se trace (blanc à 30 %, 0,7 s, `power2.inOut`), chaque mot de l'appel monte du flou (0,3 s, 0,22 s d'écart) et allume un peu plus le cadre (son trait plein de sa couleur en fait le tour par paliers, son fond prend du blanc jusqu'à 20 %) ; pendant qu'on lit l'appel, ses logos d'outils arrivent un à un autour du cadre ; puis les mots s'effacent dans le désordre (0,07 s d'écart), le cadre se resserre en carte (0,55 s, `expo.inOut`), qui se remplit de sa couleur depuis son centre (0,4 s) ; les deux autres cartes en sortent l'une après l'autre (±420 px, 0,9 s d'écart), chacune bat à son tour pendant qu'on les lit (×1,04, toutes les 0,8 s) ; elles se rejoignent (0,4 s), s'aplatissent en un trait de sa couleur (0,45 s, `expo.in`), le nom sort du flou (0,6 s), le bouton paraît et saute (`back.out(2)`), le curseur le clique ; le nom et le bouton se tiennent 3 s au moins, les logos dérivent autour.

## 6. Les transitions

- **Les carrés de pixels** entre les papiers et les écrans, et pour entrer dans sa couleur pleine : la transition signature, toujours entre deux phrases, sur un temps de la musique.
- **Le disque** : sa couleur plein écran se resserre en disque autour de la phrase pivot, le disque s'ouvre en couleur plein écran (l'avant devient l'après par le même objet) ; après la conversation, sa couleur se referme en disque sur sa nuit, pour isoler l'appel.
- **Le morphing de la fin** : le cadre devient une carte, la carte trois cartes, les cartes un trait, le trait le soulignement du nom.
- Jamais de fondu enchaîné entre deux plans chargés, ni de fondu, de flou ou d'ombre entre sa couleur et sa nuit : les carrés de pixels et le disque font ce travail, et ce qui paraît sur sa couleur paraît à pleine opacité.

## 7. Le produit à l'écran

- **Le problème** se montre par sa vraie matière, en descendant l'échelle : les captures de sa page (ses propres illustrations du problème, ses options), une image de sa vraie vidéo, ses vrais chiffres (un prix, une durée de sa fiche), les logos des outils de sa corvée (le logiciel de montage, le réseau où la vidéo doit passer) ; une vraie capture dans la carte inclinée de l'écran de nuit. Sans aucune matière, ses mots seulement (le papier et ses mots, des cases de ses vrais mots) : jamais une forme seule, jamais un objet ni un écran redessinés.
- **L'offre** se montre par sa présence (sa couleur, le disque qui porte son logo et son nom, son logo en avatar) et par **une vraie conversation** : son assistant qui répond (tel que sa vidéo ou ses captures le montrent), ses vrais échanges avec des clients, une vraie question de sa FAQ et sa vraie réponse ; un lien collé montre l'aperçu de sa vraie page ; puis **la carte du résultat** (ce que le produit rend vraiment, avec ses vraies vignettes : les scènes d'une vidéo, les pages d'un plan, un rendez-vous).
- **Le contenu de l'offre** se montre en trois cartes (ses trois parties réelles), comme les trois offres de l'original.
- Jamais une conversation inventée présentée comme vraie : sans échange réel, la scène montre une question de sa FAQ et la réponse de sa page.

## 8. Le son

- **Original** : une voix off chaleureuse dit la phrase du problème, et chaque mot apparaît au moment où il est dit ; pendant les messages, la conversation est jouée à deux voix (la voix de synthèse de l'offre et celle du client) ; une musique douce derrière, tempo estimé autour de 104 battements par minute, sans montée forte.
- **Chez le client** : texte et musique par défaut (une musique de lancement calme puis lumineuse, 95 à 110 battements par minute) ; les cases de la tenue et les transitions en pixels se calent sur ses temps. Une voix off seulement à sa demande ([voix.md](../../references/voix.md)) : chaque mot de l'avant apparaît alors quand il est dit, et la conversation peut se jouer à deux voix.
- **Bruitages** : un petit tic par case qui surgit, un grésillement bref sur chaque transition en pixels, une vibration sourde sous la pastille et la capture des écrans, une nappe qui monte pendant le pivot et un impact doux quand le disque s'ouvre, une bulle douce par message, un clic sur la carte choisie et sur le bouton.
- **Ambiance proposée** à la page des styles et des musiques (`musiques choisir --style 4`) : « Premium et calme » puis « Montée cinématique », jamais imposée (une ambiance qu'il demande passe devant).

## 9. L'ouverture et la fin

- **Original** : il s'ouvre sur le papier vide, le premier mot tapé lettre à lettre au centre ; il finit sur le logo au-dessus d'un trait lumineux, puis le noir (5 s en tout).
- **Chez le client** : l'accroche entre par ses mots, un à un, sur une image stable (aucun recadrage dans les cinq premières secondes), et la première case arrive avec le premier mot ; pour une vidéo de page, la première phrase dit déjà le sujet. La fin garde le nom et le trait, et ajoute le bouton que le curseur clique ; le nom et le bouton tiennent 3 s au moins, sans le long noir de l'original.

## Ce qui ne se fera pas à l'identique

- **Les images de l'original ne se refont pas.** Ses objets photoréalistes (des rendus 3D : bouteille, casque, cône, clavier, tasse), ses téléphones de bureau, les couleurs tramées de ses écrans et son orbe fluide ne se redessinent jamais, ni en 3D, ni en dessin simplifié, ni en formes simples à sa place (essai du 06/11/2026 : des carrés et des ronds noirs et jaunes sans sujet autour de « Et ton offre attend. »). À leur place, sa vraie matière (ses captures, sa vraie vidéo, ses vrais chiffres, les logos de ses outils), sinon ses mots.
- **Le tempo haché** (un papier toutes les 1,2 à 1,9 s) → des phrases complètes, tenues le temps de les lire ; la vie vient des cases qui arrivent pendant la tenue.
- **La vraie trame** (des points de tailles variables selon la lumière) → des tirets blancs très pâles sur sa nuit : la texture de l'écran, sans image dessous.
- **L'orbe fluide** (une matière lumineuse qui coule) → un disque plein de sa couleur dans ses anneaux, sans lueur ni cœur blanc, qui porte sa phrase puis son logo.
- **Les dégradés vifs** (l'alerte, l'après, les cartes) et le trait lumineux → sa couleur pleine, en aplat, et un trait plein et fin.
- **Les bulles de verre** → des bulles pleines sans ombre : sur un aplat, le verre ne se voit pas, et un verre clair sur sa couleur la pâlirait.
- **La voix off et la conversation jouée** → texte et musique par défaut.
- **Les petits textes et les 5 s de noir** de l'original → agrandis et raccourcis pour la lecture.
- **Les trois familles de couleurs** (bleu, rouge, vert) → ses couleurs seules : sa couleur pleine, sa nuit, son clair et des gris.

## Sur une autre offre

Le style est une façon de présenter : il se monte sur n'importe quelle offre. Ce qui suivait l'original (un standard téléphonique tenu par une IA) s'adapte :

- **Toujours** : le papier quadrillé, les mots éparpillés et leurs cases de vraie matière, les écrans de nuit et leurs pastilles, les carrés de pixels, la phrase pivot dans le disque, l'après sur sa couleur, une vraie conversation en bulles, le cadre qui devient l'offre.
- **Une formation** : sur les cases, les miniatures de ses vidéos, les captures de son espace de formation, les logos des outils qu'il enseigne, le nombre réel de ses modules ; la pastille dit ce que l'élève vit (« ENCORE REPORTÉ », « PAS COMMENCÉ »), près d'une capture de son agenda ou de sa page ; la conversation est une vraie question d'élève et la vraie réponse du formateur ou de l'assistant de la formation ; la carte du résultat est le module terminé ou le vrai livrable ; les trois cartes, ses trois parties.
- **Un coaching** : la capture de son agenda ou de ses messages en retard dans la carte (ou le téléphone) de l'écran, s'il la fournit ; la pastille « NOUVEAU MESSAGE » ; la conversation, un vrai échange avec un client (avec son accord) ou un vrai témoignage en messages ; la carte, la séance réservée ; les trois cartes, ses formats d'accompagnement.
- **Un logiciel** : les logos des outils qu'il remplace et les captures de l'ancienne façon de faire sur les cases ; la pastille, l'alerte qu'il évite ; la conversation, son vrai assistant ou ses vraies notifications ; la carte, son vrai résultat avec ses vraies vignettes ; les trois cartes, trois fonctions ou trois formules.

## En vertical et en carré

- **9:16 : chaque scène a sa version verticale** (`mots-objets-vertical.html`, `orbe-pivot-vertical.html`, `messages-verre-vertical.html`, `fin-cadre-vertical.html`), remise en page et jamais recadrée. Les quatre bout à bout en 1080 × 1920 font 59,5 s avec l'exemple (essai du 06/11/2026 sur LMDM : `rythme` « ok », 1,09 événement par seconde, écart médian 0,80 s, aucune image figée, `palette` « ok », raccords image pour image).
- **Le papier en 9:16** (`mots-objets-vertical.html`) : les mots à 96 px, en deux ou trois rangées dans la bande du milieu (de 650 à 1 100 px dans le kit, 600 à 1 300 au plus), 9 lettres au plus par mot ; les cases dans les bandes du haut et du bas (100 à 300 px sur la grille de 100 px : x = 40, 140…, y = 60, 160…), quelques petites sur les bords de la bande du milieu : l'écran est rempli de haut en bas. Les carrés de pixels restent à 120 px (9 colonnes, 16 rangées). Sur les écrans, la pastille au-dessus de la capture (y = 560), la carte inclinée centrée (640 px de large ; un téléphone de 500 × 1 000 px pour une capture de téléphone).
- **Le disque en 9:16** (`orbe-pivot-vertical.html`) : centré, un peu plus grand (rayon de 420 px autour de la phrase, puis 200 px avec le logo), anneaux plus larges (470, 740 et 1 080 px) qui occupent la hauteur ; la phrase pivot passe à 64 px, le nom à 64 px sous le disque.
- **La conversation en 9:16** (`messages-verre-vertical.html`) : elle remplit l'écran comme sur un téléphone : colonne de 968 px, bulles de 44 px, aperçu du lien de 640 × 360 px, cartes de choix de 280 px, le fil part du milieu et remonte ; les logos d'outils dans les bandes du haut et du bas, hors du fil.
- **En pub 9:16** (zone sûre : y de 269 à 1 248, `zones pub`) : les versions verticales sont calées pour un Reel. Remonte la conversation (`Y0` vers 880, `BAS` vers 1 180 : vérifie sur la planche) et toute la fin de 100 px (une enveloppe `top: -100px` marquée `data-layout-allow-overflow`), les cartes à ±280 px ; la fin ne dessine pas de bouton : « Découvre-le » et une flèche vers le bas à sa place, sans curseur (structures.md, publicité ; essai du 03/11/2026).
- **La fin en 9:16** (`fin-cadre-vertical.html`) : le cadre fait 960 × 700 px, la phrase d'appel à 64 px passe sur deux lignes centrées (« | » dans `APPEL` marque le retour à la ligne) ; les trois cartes (720 × 240 px) sortent au-dessus et au-dessous de la première, s'empilent en colonne, puis la colonne s'aplatit en un trait de 860 px ; le nom à 88 px au-dessus, le bouton (pilule de 104 px, texte de 44 px) dessous, vers le milieu de l'écran ; les logos d'outils au-dessus et au-dessous du cadre.
- **4:5 et 1:1** : comme le 16:9 resserré ; 9 colonnes de carrés, les cases seulement sur les côtés, deux cartes au lieu de trois en 1:1 si le texte ne tient pas.
- Les mots clés restent hors des 10 % du haut et des 20 % du bas en vertical (les commandes de l'application).

## Les compositions du kit

Chaque scène calcule ses instants depuis ses textes (leur lecture) : sa durée change avec eux. La console (et `npm run check`) l'affiche : « t04-… dure … s » ; reporte-la dans `D` et `data-duration` de la scène, et sur son hôte dans `index.html`.

| Fichier | Durée (exemple) | Ce qu'elle montre | Ce qu'on remplace |
|---|---|---|---|
| `compositions/mots-objets.html` | 20,4 s | L'avant : un papier (la phrase et ses cases de vraie matière), trois écrans de nuit avec leur capture et leur pastille, un dernier papier entouré de toutes les matières, reliés par des transitions en pixels, puis l'entrée de sa couleur pleine | L'id `t04-mots`, `PLANS` (dans l'ordre : chaque papier, ses mots, leur place, ses mots clés et ses cases de vraie matière avec leur instant ; chaque écran, sa pastille, sa place et sa vraie capture) |
| `compositions/orbe-pivot.html` | 7,5 s | La bascule : la phrase pivot sur sa couleur qui bat, le disque qui se resserre autour d'elle, son mot clé, puis le disque qui porte son logo et son nom, les deux battements, l'ouverture sur l'après | L'id `t04-orbe`, `PIVOT` (« \| » coupe la ligne), `CLE`, `LOGO` et `NOM` (vides : le disque n'est qu'une transition) |
| `compositions/messages-verre.html` | 16,4 s | L'après : une vraie conversation en bulles pleines sur sa couleur, l'aperçu de sa page qui défile, ses choix, la carte choisie, la carte du résultat et ses vignettes qui se cochent, ses logos d'outils dans les marges, puis sa couleur qui se referme en disque sur sa nuit | L'id `t04-msg`, `MESSAGES` (un vrai échange, avec `lien`, `apercu`, `choix`, `prend`), `ETIQUETTE`, `LOGO`, `CADENCE`, `RESULTAT` (ou `null`), `OUTILS` et `PLACES` |
| `compositions/messages-verre-vertical.html` | 16,4 s | La même conversation en 9:16 | Comme la version 16:9 |
| `compositions/fin-cadre.html` | 15,2 s | L'offre et l'appel : le cadre qui s'allume, sa phrase, ses logos d'outils autour, les trois cartes, le trait, le nom, le bouton cliqué | L'id `t04-fin`, `APPEL`, `CARTES` (les trois parties réelles de l'offre), `NOM` (ou son logo en `<img>`), `BOUTON`, `OUTILS` et `PLACES` |
| `compositions/mots-objets-vertical.html` | 20,4 s | L'avant en 9:16 : les mots dans la bande du milieu, les cases en haut et en bas, la pastille au-dessus de la capture, les carrés de pixels en 9 × 16 | Comme la version 16:9 ; les places des mots et des cases suivent la grille verticale (en-tête du fichier) |
| `compositions/orbe-pivot-vertical.html` | 7,5 s | La bascule en 9:16 : le disque centré, plus grand, ses anneaux sur toute la hauteur | Comme la version 16:9 |
| `compositions/fin-cadre-vertical.html` | 15,2 s | L'offre et l'appel en 9:16 : le cadre de 960 × 700 px, la phrase sur deux lignes, les trois cartes empilées, le trait, le nom, le bouton cliqué | Comme la version 16:9 ; trois cartes |

L'exemple des scènes est l'essai du kit : la story d'ouverture de Publicitaire IA (ses phrases, les illustrations de sa page, sa vraie pub, l'échange réel de la vidéo de sa page, ses chiffres, ses logos d'outils). Ses captures (`assets/images/…`) n'existent que dans son projet : chez un autre client, tout se remplace (une case dont l'image ou le logo manque reste vide de matière, donc ne s'affiche pas). Bout à bout dans cet ordre, les scènes font une vidéo de 59,5 s qui se tient seule, en 16:9 comme en 9:16 avec les versions `-vertical` (essais : `rythme` « ok », `palette` « ok », `check` sans erreur). Les raccords sont faits dans les deux formats : la fin de `mots-objets` est la première image de `orbe-pivot` (sa couleur pleine plein cadre), la fin de `orbe-pivot` celle de `messages-verre` (sa couleur pleine), et `messages-verre` finit sur sa nuit, où commence `fin-cadre`. Un format = une seule famille de fichiers : en 9:16, monte les quatre `-vertical`, jamais une scène 16:9.
