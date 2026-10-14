# La voix

Trois modes, choisis au profil et changeables à chaque vidéo. Quel que soit le mode, **tout ce
qui compte se lit à l'écran** : beaucoup de supports se regardent muets.

## A. Texte à l'écran et musique (par défaut)

Le plus simple et le plus sûr. Le texte porte la vidéo, la musique et les bruitages la font
vivre. Les durées viennent des temps de lecture (`studio_motion.py lecture`).

## B. Sa voix, enregistrée sur son téléphone

La plus convaincante pour une vidéo de page de vente ou un Reel : c'est lui qui parle.

1. Écris le texte de la voix d'après le plan (phrases courtes, à dire, pas à lire ; 2,5 mots par
   seconde environ). Donne-le-lui avec la consigne : au dictaphone de son téléphone, dans un
   endroit calme, phrase par phrase ; il peut se reprendre, on garde la dernière version.
2. Il glisse le fichier audio dans la conversation. Range-le dans `assets/audio/voix-brute.*`.
3. Transcris-la (`npx hyperframes transcribe assets/audio/voix-brute.m4a`) : le texte daté
   montre les reprises. Garde la dernière prise de chaque phrase, coupe les blancs de plus de
   0,4 s avec ffmpeg (`atrim` + `concat`), normalise doucement (`loudnorm=I=-18`), puis exporte
   `assets/audio/voix.wav`. Fais écouter le résultat avant de caler la vidéo dessus.
4. Obtiens le temps de chaque mot : `npx hyperframes transcribe assets/audio/voix.wav`. Les
   animations se calent sur les mots : un élément arrive **avec** le mot qui le nomme, pas après.
5. Pose la voix avec les sons (`son.md`), au-dessus de la musique ; des sous-titres incrustés
   en plus si le support se regarde muet.

## C. Une voix de synthèse locale (gratuite)

HyperFrames génère une voix sur l'ordinateur, sans compte ni coût :

```bash
npx hyperframes tts "<texte>" --voice ff_siwis --lang fr-fr -o assets/audio/voix.wav
```

`ff_siwis` est la voix française ; `--speed 1.05` si elle traîne. Fais écouter 10 secondes au
client avant de produire toute la vidéo : la qualité ne plaît pas à tout le monde. Puis
`transcribe` et calage comme en B.

Une voix payante plus naturelle (ElevenLabs, HeyGen) ne s'utilise que si le client l'a déjà et
l'accepte, coût annoncé avant. Ne clone jamais une voix sans son accord explicite.

## Le texte d'une voix

Mêmes règles que `ecriture.md`, à l'oral : phrases de 12 mots au plus, une idée par phrase, des
mots qu'il dirait vraiment. Relis-le à voix haute. L'écran ne recopie pas la voix mot pour mot :
il affiche le mot clé, le chiffre, le nom de l'offre.
