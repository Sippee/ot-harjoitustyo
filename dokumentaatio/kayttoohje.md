# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/Sippee/ot-harjoitustyo/releases/tag/latest) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Jonka jälkeen suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Kirjautuminen ja rekisteröinti

Sovellus käynnistyy terminaaliin, josta valitaan mitä haluaa tehdä.

Voi valita haluaako rekisteröidä uuden tunnuksen vai kirjautua sisään.


## Kirjautumisen jälkee voi aloittaa pelin tai kirjautua ulos

Terminaalissa on ohje, miten aloittaa peli tai kirjautua ulos, kun on kirjautunut sisälle tai rekisteröitynyt uuden tunnuksen.
