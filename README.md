# Tietoliikenteen sovellusprojekti 2025

Projektin tavoitteena oli luoda IoT-järjestelmä, jossa nordicin alustassa kiinnitettynä oleva kiihtyvyysanturi mittaa dataa, välittää sen bluetooth low energyn yli raspberry pi 3 palvelimelle ja sieltä toiselle tietokantapalvelimelle.​

Tietokannasta haetut tiedot näkyvät  palvelimen http sivulla. Sekä http sivulta, että tietokannasta pystytään hakemaan data csv tiedostoon. ​

Tämän csv data tiedoston avulla luodaan K-means algoritmi, joka käy arvot läpi ja määrittää mittauksien keskipisteet. Keskipisteiden avulla luodaan koneoppimismalli, joka kertoo mihin suuntaan kiihtyvyysanturi osoittaa.

# Järjestelmäarkkitehtuuri
<img width="764" height="627" alt="Näyttökuva 2025-10-31 125127" src="https://github.com/user-attachments/assets/ff08cb7e-857f-43f3-94b9-1b12a699e1e8" />
