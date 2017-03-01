#include<iostream>

int a,b,c;							//试试全局变量
void daxiao(int *x,int *y,int *z);
inline int swap(int *m,int *n){      //试试内联函数 
		int t;
		t=*m;             //*x代表取x指针指向地址的内容
		*m=*n;
		*n=t;
		return 0;
}
void main(){
	int *x,*y,*z;
	scanf("%d %d %d",&a,&b,&c);
	x=&a;					//上面的&只是代表存储输入的数，这里要赋值指针
	y=&b;
	z=&c;
	daxiao(x,y,z);
	printf("%d>%d>%d",a,b,c);
}
void daxiao(int *q,int *w,int *e){
	if(a<b){            //全局变量可以直接使用
		swap(q,w);
	}
	if(a<c){
		swap(q,e);
	}
	if(b<c){
		swap(w,e);
	}

}
