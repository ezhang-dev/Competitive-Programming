#include <stdio.h>
#ifndef max
	#define max( a, b ) ( ((a) > (b)) ? (a) : (b) )
#endif
int main() {
    int i;
    scanf("%d",&i);
    for(int _=0;_<i;_++){
        int j;
        scanf("%d",&j);
        j--;
            int x,p,f,pr,m,d;
        scanf("%d %d",&x,&p);
        f=x;
        while(!p){
            scanf("%d %d",&x,&p);
            j--;
        }
        pr=x;
        m=-1;
        d=0;
        for(int __=0;__<j;__++){
            scanf("%d %d",&x,&p);
            m=max(m,x-pr);
            pr=x;
            if(p){
                d+=m;
                m=-1;
            }
        }
            printf("%d\n",pr-f-d);
    }

    return 0;
}