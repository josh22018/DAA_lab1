package java_pro;

public class Selection_sort {
	public void select(int arr[],int n) {
		System.out.print("Before sorting : \n");
		for(int k=0;k<n;k++) {
			System.out.print(arr[k]+" ");
		}
		System.out.print("\n");
		for (int i = 0; i < n-1; i++) {
            // Find the minimum element in unsorted array
            int minIndex = i;
            for (int j = i+1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }

            
            int temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
        }
		System.out.print("After sorting : \n");
		for(int k=0;k<n;k++) {
			System.out.print(arr[k]+" ");
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a[]= {67,95,93,75,80};
		Selection_sort one = new Selection_sort();
		long startTime = System.currentTimeMillis();
		one.select(a, 5);
        long endTime = System.currentTimeMillis();
		System.out.print("\nTime for Execution :"+(endTime-startTime)+"ms");
		

	}

}
