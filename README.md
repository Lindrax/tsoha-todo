# Tsoha todo
Tällä hetkellä sovellukseen voi rekisteröityä ja kirjautua. lisätä tehtäviä ja valita näille kategorian ja deadlinen. Uusia kategorioita voi tehdä ja näille voi valita värikoodin.

Käynnistysohjeet:

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

DATABASE_URL=tietokannan-paikallinen-osoite

SECRET_KEY=salainen-avain

Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r ./requirements.txt

Määritä vielä tietokannan skeema komennolla

$ psql < schema.sql

Nyt voit käynnistää sovelluksen komennolla

$ flask run





