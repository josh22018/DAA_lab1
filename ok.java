package java_pro;

public class ok {
public int [] search(int a[],int n) {
	int count=0;
	for(int i=0;i<n-1;i++) {
		for(int j=0;j<n-1;j++) {
			if(a[j]>a[j+1]) {
				int temp=a[j];
				a[j]=a[j+1];
				a[j+1]=temp;
				count++;
			}
		}
	}
	for (int k=0;k<n;k++) {
		System.out.print(a[k]+" ");
	}
	System.out.println("\nNO of swaps : "+count);
	return a;
}



public static void main(String[] args) {
	
	int a[]= {122,4672,8584,34,839,426,191,483,352,948};
	ok hi=new ok();
	double startTime = System.currentTimeMillis();
	hi.search(a, 10);
    double endTime = System.currentTimeMillis();
	System.out.print("\nTime for Execution :"+(endTime-startTime)+"ms");
}
}