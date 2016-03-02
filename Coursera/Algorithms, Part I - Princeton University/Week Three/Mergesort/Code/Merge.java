public class Merge {
	private Merge() {}

	private static void merge(Comparable[] a, Comparable[] aux, int lo, int mid, int hi) {

		//assert that both arrays (a[lo...mid]) and (a[mid+1...hi]) are sorted
		assert isSorted(a, lo, mid);
		assert isSorted(a, mid+1,hi);

		for(int k = lo; k <= hi; k++) {
			aux[k] = a[k];
		}

		int i = lo, j= mid + 1;

		for(int k = lo; k <= hi; k++) {
			if (i>mid) {
				a[k] = aux[j++];
			} else if (i > hi) {
				a[k] = aux[i++];
			} else if (less(aux[j], aux[i])) {
				a[k] = aux[j++];
			} else {
				a[k] = aux[i++];
			}
		}

	}
}