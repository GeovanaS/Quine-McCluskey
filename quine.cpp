#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <string>

using namespace std;

int nMint = 0;


void removeSpaces(char *s)
{
    char* s2 = s;
    do {
        if (*s2 != ' ')
            *s++ = *s2;
    } while (*s2++);
}


void listarMintermos(char *equacao){
  int i = 0,j = 0, k = 0, pos = 0, cont = 0;
  nMint = 0;
  int mintPos[15];
  char eqBin[120];

  for(k-0;k<120;k++){
    eqBin[k] = '\0';
  }

  while ( equacao[i] !=  '\n') {
  if (equacao[i]=='!'){
     pos = i+1;
     k=i;
    //printf("\nvalor k:\n %d",k);
     eqBin[k] = ' ';
     mintPos[j] = pos;
     nMint++;
     k=pos;
     eqBin[k] = '0';
  	 i++;
  	 j++;
  	 k++;
 //printf("\nEntrou no PRIMEIRO IFn");

  	 cont++;
  }else if( (equacao[i]>='a') && (equacao[i]<='z') || 	((equacao[i]>='A')&&(equacao[i]<='Z') || (equacao[i]>='*') || (equacao[i]=='!') ) ) {
     if(equacao[i-1]=='!'){
     eqBin[k] = ' ';
     i++;
     cont++;
  //printf("\nEntrou no IF DO NEG\n");

     } 
     if( (equacao[i]>='a') && (equacao[i]<='z') ||    ((equacao[i]>='A')&&(equacao[i]<='Z')) ) {
            eqBin[k] = '1';
            k++;
            i++;
     //       printf("\nentrou no IF DA EQUACAO A a Z\n");
     }

     if((equacao[i]>='*') ){
     eqBin[k] = ' ';
     i++;
     k++;
  //  cont++;
   // printf("\nEntrou no else\n");
     }
 }else if((equacao[i]>='+')){
  	eqBin[k] = ' ';
  	i++;
    k++;
  //  cont++;
 //printf("\nEntrou no POSITIVO\n");

  }
  else{
  	eqBin[k] = ' ';
  	i++;
  	k++;
    //cont++;
  // printf("\nEntrou no ESPACO\n");

  }
//  cont++;
 }
     printf("\nCONT:%d\n",cont);
        //  printf("\nK:%d\n",k);

 /*char *eBin;
 eBin = (char *)malloc(strlen(eqBin) + 1);
 if(eBin==NULL){
    printf("alocacao invalida!\n");
    return;
 }

 int x=0; 
 for(k=0,x=0; eqBin[k]!='\n';k++){
    if(isspace(eqBin[k]) == 0){
        eBin[x++] = eqBin[k];
    }
 }
    eBin[x]='\0';
*/
 
 //eqBin[cont-1]='\0';


 printf("Mintermos:\n");

 for(j=0;j<nMint;j++){ 	 
	 printf("%d ",mintPos[j]);
 }

 printf("\n");
 removeSpaces(eqBin);
 printf("EqBin:\n");


 for(k=0;k<strlen(eqBin);k++){
     printf("%c ",eqBin[k]);
 }

/*printf("\nebin:\n");
 for(x=0;x<=nMint;x++){
  	 printf("%c ",eBin[x]);
 }
 */
 printf("\n");
}


int main() {
  char input[120];	
  char output[120];
  char termo[16];
  char vName[12];

  char *eq;
  int i = 0, j = 0, k = 0;
  int flagAnd=0,flagOr=0,nVars = 0 ,cont = 0, flag = 0;


  for(i=0;i<120;i++){
        input[i] = '\0';
  }

  eq = (char*) malloc(sizeof(char)*120);
  if(eq==NULL){
    printf("alocacao invalida\n");
    return 0;
  }

  printf("Digite a equaçao: \n");

  eq = fgets(input,120,stdin);
  
  if((eq==NULL) || (input[0]=='\n')){
    nVars=0;
    fprintf(stderr,"entrada invalida!");
    return 0;
  }
  
/*  while ( input[i] !=  '\n') {
  if (input[i]=='+'){
  	 flagAnd++;
  	 i++;
  }else if(input[i]=='*'){
  	flagOr++;
  	i++;
  }
  i++;
}
*/


 // printf("%s\n",eq);
  listarMintermos(eq);
  //  printf("teste");

  //free(eq);

  return 0;
}
