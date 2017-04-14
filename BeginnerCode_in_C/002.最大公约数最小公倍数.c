ver2.

void main(){
	int a,b,temp,i,gy=1;
	scanf("%d %d",&a,&b);
	if(a>b){
		temp=a;
		a=b;
		b=temp;
	}
	for(i=a;i>1;i--){
		while(a%i==0&&b%i==0){
			gy*=i;
			a/=i;
			b/=i;
			printf("%d %d",i,i*a*b);
		}
	}
}


-----------------------------------------------------------------------------------
#include <stdio.h>

void  main(){
	int	i,m,n,t,low,high;
	printf("input two numbers:");
	scanf("%d %d",&m,&n);
	if(m<n){
		t=m;
		m=n;
		n=t;
	}
	for(i=2;i<=n;i++){
		if(m%i==0&&n%i==0){
			low=i;
		}
	}
	high=m*n/low;
	printf("low=%d high=%d\n",low,high);
}
