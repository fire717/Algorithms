##才发现之前的输出顺序是从大到小。刚好重新没看写了一个

#include<iostream>
using namespace std;

int main(){
	int i,j,n=100,a=0;
	for(i=2;i<=n;i++){
		for(j=2;j<i;j++){
			if(i%j==0)
				a+=1;
		}
		if(a==0)
			printf("%-3d",i);
		a=0;
	}

}




-----------------------old version---------------------------
#include <stdio.h>

int main(){
	int i,j,n;
	for(i=100;i>0;i--){
		n=0;
		for(j=i;j>0;j--){
			if(i%j==0)
				n++;
		}//for j
		if(n==2)
			printf("%-3d",i);
	}//for i
}//main
