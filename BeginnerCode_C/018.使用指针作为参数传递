C++实参单向传递为形参，通过指针可以将函数中的参数值回传至主函数

-----------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h> 

void change(int *x,int *y,int *z);
void main(){
	int a,b,c,*p1,*p2,*p3;
	scanf("%d %d %d",&a,&b,&c);
	p1=&a;
	p2=&b;
	p3=&c;
	change(p1,p2,p3);
	printf("%d<%d<%d",*p1,*p2,*p3);
}
void change(int *x,int *y,int *z){
	int t;
	if(*x>*y){
		t=*x;
		*x=*y;
		*y=t;
	}
	if(*x>*z){
		t=*x;
		*x=*z;
		*z=t;
	}
	if(*y>*z){
		t=*y;
		*y=*z;
		*z=t;
	}
	printf("%d<%d<%d\n",*x,*y,*z);
}
