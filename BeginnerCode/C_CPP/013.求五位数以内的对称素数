做是做出来了，输出是对的，就是感觉貌似有点复杂，
CMD窗口都好多秒才慢慢显示完，有时间考虑下优化吧。
-----------------------------------------------------------------------
#include<iostream>

void dc(int x);
void main(){                  //主函数用于判断是否为素数
	int i,j,n=100000,a=0;
	for(i=2;i<n;i++){
		for(j=2;j<i/2;j++){
			if(i%j==0)
				a+=1;
		}
		if(a==0)
			dc(i);
		a=0;
	}

}
void dc(int x){                //定义了一个函数用来判断是否对称
	if(x>10000){
		if(x/10000==x%10&&x/1000%10==x/10%10)
			printf("%d ",x);
	}
	else if(x>1000){
		if(x/1000==x%10&&x/100%10==x/10%10)
			printf("%d ",x);
	}
	else if(x>100){
		if(x/100==x%10)
			printf("%d ",x);
	}
	else if(x>10){
		if(x/10==x%10)
			printf("%d ",x);
	}
	else
		printf("%d ",x);;
}
