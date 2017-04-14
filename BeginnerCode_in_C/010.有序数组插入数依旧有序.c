#include <stdio.h>
#include <stdlib.h> 

void main(){
	int a[7]={1,3,5,7,9,11};
	int n,i=0,j;
	scanf("%d",&n);
	while(a[i]<n)
		i++;
	for(j=5;j>=i;j--){
		a[j+1]=a[j];
	}
	a[i]=n;
	for(i=0;i<=5+1;i++)
		printf("%d ",a[i]);
}
