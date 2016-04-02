//my first answer
void main(){
	int	i,j,n=0,k=1;
	for(i=1;i<=20;i++){
		for(j=1;j<=i;j++){
			k*=j;
		}
		n+=k;
	}
	printf("jieguo:%d\n",n);
}

//the given answer
void main(){
	int	i,n=0,k=1;
	for(i=1;i<=2;i++){
		k*=i;
		n+=k;
	}
	printf("jieguo:%d\n",n);
}

/*总结：我按照自然想法，用了两个循环，一个控制加，一个控制乘。
而实际中由于加法是递增的，乘法自然加到当前值就会停止，然后再累加时由于上一次的K未清零，相当于从1开始再乘了一遍。这个思想很实用，要熟练*/
