#include <stdio.h>

void main(){
	int i,j,k,m,temp;
	int n[10];
	for(i=0;i<10;i++){
		printf("put in a number:");
		scanf("%d",&n[i]);
	}//输入
	
	for(j=1;j<10;j++){
		for(k=0;k<i;k++){
			if(n[j]<n[k]){
				temp=n[j];
				n[j]=n[k];
				n[k]=temp;
			}//if 
		}//for k
	}//for j


	for(m=0;m<10;m++){
	printf("%-3d",n[m]);
	}
}
