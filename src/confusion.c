#include <zephyr/kernel.h>
#include <math.h>
#include "confusion.h"
#include "adc.h"
#include "keskipisteet(1).h"

/* 
  K-means algorithm should provide 6 center points with
  3 values x,y,z. Let's test measurement system with known
  center points. I.e. x,y,z are supposed to have only values
  1 = down and 2 = up
  
  CP matrix is thus the 6 center points got from K-means algoritm
  teaching process. This should actually come from include file like
  #include "KmeansCenterPoints.h"
  
  And measurements matrix is just fake matrix for testing purpose
  actual measurements are taken from ADC when accelerator is connected.
*/ 

/*int CP[6][3]={
	                {1,0,0},
						 {2,0,0},
						 {0,1,0},
						 {0,2,0},
						 {0,0,1},
						 {0,0,2}
};*/

/*int measurements[6][3]={
	                {1,0,0},
						 {2,0,0},
						 {0,1,0},
						 {0,2,0},
						 {0,0,1},
						 {0,0,2}
};*/

int CM[6][6]= {0};



void printConfusionMatrix(void)
{
	printk("Confusion matrix = \n");
	printk("   cp1 cp2 cp3 cp4 cp5 cp6\n");
	for(int i = 0;i<6;i++)
	{
		printk("cp%d %d   %d   %d   %d   %d   %d\n",i+1,CM[i][0],CM[i][1],CM[i][2],CM[i][3],CM[i][4],CM[i][5]);
	}
}
void makeHundredFakeClassifications(void)
{
   /*******************************************
   Jos ja toivottavasti kun teet toteutuksen paloissa eli varmistat ensin,
   että etäisyyden laskenta 6 keskipisteeseen toimii ja osaat valita 6 etäisyydestä
   voittajaksi sen lyhyimmän etäisyyden, niin silloin voit käyttää tätä aliohjelmaa
   varmistaaksesi, että etäisuuden laskenta ja luokittelu toimii varmasti tunnetulla
   itse keksimälläsi sensoridatalla ja itse keksimilläsi keskipisteillä.
   *******************************************/

   printk("Make your own implementation for this function if you need this\n");
}


void makeOneClassificationAndUpdateConfusionMatrix(int direction)
{
   /**************************************
   Tee toteutus tälle ja voit tietysti muuttaa tämän aliohjelman sellaiseksi,
   että se tekee esim 100 kpl mittauksia tai sitten niin, että tätä funktiota
   kutsutaan 100 kertaa yhden mittauksen ja sen luokittelun tekemiseksi.
   **************************************/

      /*int x = measurements[direction][0];
      int y = measurements[direction][1];
      int z = measurements[direction][2];*/
      struct Measurement m=readADCValue();
      int predictedClass = calculateDistanceToAllCentrePointsAndSelectWinner(m.x,m.y,m.z);
      int actualClass = direction;

      if(predictedClass >= 0 && predictedClass <6){
         CM[actualClass][predictedClass]++;
      }
   //printk("Make your own implementation for this function if you need this\n");
}

int calculateDistanceToAllCentrePointsAndSelectWinner(int x,int y,int z)
{
   /***************************************
   Tämän aliohjelma ottaa yhden kiihtyvyysanturin mittauksen x,y,z,
   laskee etäisyyden kaikkiin 6 K-means keskipisteisiin ja valitsee
   sen keskipisteen, jonka etäisyys mittaustulokseen on lyhyin.
   ***************************************/

  int distance[6];
  int min_index=0;
  for (int i = 0; i < 6; i++) {
   int dx=(CP[i][0] -x); //Muuta CP taulukko keskipisteet.h taulukon arvoiksi
   int dy= (CP[i][1] -y);
   int dz= (CP[i][2] -z);

   distance[i]=sqrt(dx*dx + dy*dy +dz*dz);
   if (distance[i] < distance[min_index]){
      min_index=i;
   }
}
      /*int closest_x = CP[min_index][0]; //Muuta CP, keskipisteet.h taulukon arvoiksi
      int closest_y = CP[min_index][1];
      int closest_z = CP[min_index][2];*/

      //printf("closest centroid: CP[%d] = (%d, %d, %d)\n", //Muuta CP
            //min_index, closest_x, closest_y, closest_z);
   //printk("Make your own implementation for this function if you need this\n");
   return min_index;
}

void resetConfusionMatrix(void)
{
	for(int i=0;i<6;i++)
	{ 
		for(int j = 0;j<6;j++)
		{
			CM[i][j]=0;
		}
	}
}

