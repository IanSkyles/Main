public class DynamicCapacityStackOfStrings {
	public String[] S;
	public int N;

	public DynamicCapacityStackOfStrings() {
		s = new String[1]
		N = 0;
	}

	public boolean isEmpty() {
		return N == 0;
	}

	public void push(String item) {
		//if the array is at max capacity, double it.
		if (N == s.length()) {
			resize(2*s.length);
		}
		s[N++] = item;
	}

	public String pop() {
		
		String item = s[--N];
		s[N] = null;
		//if the number of items is 1/4 the size of the array, half the array.
		if (N == (s.length() / 4) {
			resize(s.length / 2);
		}
		return item;
	}

	public void resize(int newSize) {
		String[] temp = new String[newSize];
		for(int i = 0; i < N; i++) {
			temp[i] = S[i];
		}
		S = temp;
	}

}