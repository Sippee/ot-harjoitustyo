# Kolikoiden keräys peli
Peli, jossa kerätään kolikoita snake-pelin tyylisesti. Peliin voi kirjautua, ja pelin pisteet tallentuvat siten käyttäjälle.

## Dokumentaatio  
[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)  
[Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)  
[Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)  
[Käyttöohje](dokumentaatio/kayttoohje.md)

## Releases
[Releases](https://github.com/Sippee/ot-harjoitustyo/releases/tag/latest)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coveragereport
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Pylintin alkuperäiset tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

## Tällä hetkellä ei toiminnassa oleva ominaisuus
Sovellus ei oikein halua sammua ainakaan omalla koneellani, en ehtinyt korjaa vielä
