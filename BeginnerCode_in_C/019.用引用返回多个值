比如此例，return返回一个函数值，
通过引用后在自定义函数中修改了y的值，使主函数的值也变了。

--------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h> 

int test(int,int&);
int main(){
	int a,b,error;
	scanf("%d %d",&a,&b);
	error=test(a,b);
	if(error)
		printf("%d %d\n",a,b);
	return 0;
}
int test(int x,int &y){
	y=y+1;
	return true;
}
