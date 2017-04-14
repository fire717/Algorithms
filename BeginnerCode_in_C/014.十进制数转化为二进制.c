#include<iostream>

void main(){
	int a,n=0,k=1;
	scanf("%d",&a);
	for(a;a>0;a/=2){
		if(a%2!=0){
		n+=k;
		}
		k*=10;
	}
	printf("%d\n",n);
}
