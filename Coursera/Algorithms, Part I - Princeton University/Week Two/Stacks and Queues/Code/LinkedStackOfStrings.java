public class LinkedStackOfStrings {
	private Node first = null;

	private class Node {
		String item;
		Node next;
	}

	public boolean isEmpty() {
		return first == null;
	}

	public void push(String item) {
		Node bottom = first;
		first = new Node()
		first.item = item;
		first.next = bottom;
	}

	public String pop() {
		String item = first;
		first = first.next;
		return item;
	}
}