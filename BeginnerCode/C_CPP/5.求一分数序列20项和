/*1.a,b都必须声明为浮点型，否则后面的n+=a/b会隐士转换掉；
  2.控制小数位数的方法是在%f之间加上.再加上数字。         */

#include <stdio.h>

void main(){
	int	i,t;
	float a=2,b=1,n=0;
	for(i=0;i<2;i++){
		n+=a/b;
		t=b;
		b=a;
		a=a+t;
	}
	printf("qian20:%.3f\n",n);
}
