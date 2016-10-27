##自己按理解随便写了一个

#include<iostream>

void main(){
	int i,j,a[5],temp;
	for(i=0;i<5;i++){
		scanf("%d",&a[i]);
	}                         //input

	for(j=4;j!=0;j--){
		for(i=0;i<j;i++){
				if(a[i]<a[i+1]){
					temp=a[i];
					a[i]=a[i+1];
					a[i+1]=temp;
			}
		}
		for(i=0;i<5;i++){                 //每一趟之后输出一次
		printf("%d ",a[i]);
		if(i==4)
			printf("\n");
		}
	}
	                            //output
	for(i=0;i<5;i++){
		printf("%d ",a[i]);
	}
}
