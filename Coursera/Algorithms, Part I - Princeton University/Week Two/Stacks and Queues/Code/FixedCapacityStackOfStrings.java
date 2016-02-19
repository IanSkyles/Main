public class FixedCapacityStackOfStrings {
	private String[] s;
	private int N = 0;

	public FixedCapacityStackOfStrings(int capacity) {
		s = new String[capacity];
	}

	public boolean isEmpty() {
		return N == 0;
	}

	public void push(String item) {
		s[N] = item;
		N = N + 1;
		/* or s[N++] = item;*/
	}

	public string pop() {
		//note that the s[n] starting position is empty.
		return s[--N];
	}


}