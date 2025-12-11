# Tietoliikenteen sovellusprojekti 2025

Tämän projektin tavoitteena oli toteuttaa IoT-järjestelmä, jossa kiihtyvyysanturi mittaa kolmiakselista dataa ja välittää sen Bluetooth Low Energy (BLE) -yhteyden kautta Raspberry Pi 3 :lla olevalle linux palvelimelle. Raspberry Pi tallentaa datan tietokantapalvelimelle, josta se on hyödynnettävissä sekä ohjelmallisesti että HTTP-käyttöliittymän kautta.

Tallennetun datan pohjalta ohjelmoidaan ML malli, joka tunnistaa kiihtyvyysanturin suunnan.

Nordic-alusta (nRF5340 DK)
-	Anturi mittaa kiihtyvyyttä X, Y ja Z -akseleissa.
-	Data lähetetään eteenpäin BLE:n avulla.
-	Muodostetaan yhteys Raspberry Pi 3:n joka lukee arvot

Raspberry Pi 3
-	Toimii BLE-clientinä.
-	Vastaanottaa Nordicilta tulevan datan.
-	Tallentaa datan MySQL tietokantaan.
-	Siirtää datan HTTP-sivulle, josta näkee uusimman datan.

Tietokantapalvelin
-	Tallentaa kaikki mittaukset (X, Y, Z, timestamp).
-	Data on katsottavissa HTML-sivulla.
-	Data on ladattavissa CSV-tiedostona.

CSV-datan käsittely ja koneoppiminen Pythonilla
-	Pythonilla toteutettiin K-means-klusterointi.
-	Käytettiin kiihtyvyysanturin dataa:	(X, Y, Z + manuaalisesti annettu suuntatieto).
-	Algoritmin lopputuloksena muodostui 6 klusteria = 6 mahdollista suuntaa.
-	Klusterien keskipisteet tallennettiin tiedostoon keskipisteet.h.

K-means-luokittelijan toteutus Nordicissa (C-koodilla)
-	nRF5340DK-laitteelle toteutettiin luokittelija, joka:
	  -	lukee uuden mittauksen,
	  -	laskee etäisyyden jokaisen keskipisteen välillä,
	  -	valitsee lähimmän,
	  -	tulostaa / lähettää suunnan BLE:n kautta.

# Järjestelmäarkkitehtuuri
<img width="764" height="627" alt="Näyttökuva 2025-10-31 125127" src="https://github.com/user-attachments/assets/ff08cb7e-857f-43f3-94b9-1b12a699e1e8" />
