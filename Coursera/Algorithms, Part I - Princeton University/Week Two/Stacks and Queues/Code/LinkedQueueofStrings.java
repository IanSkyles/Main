public class LinkedQueueofStrings {

	private Node first, last;

	private class Node{
		String item;
		Node next;
	}


	public String isEmpty() {
		return first == null;
	}

	public String dequeue() {
		String item = first.item;
		first = first.next;
		if (isEmpty()) {
			last = null;
		}
		return item;
	}

	public void enqueue(String item) {
		Node oldLast = last;
		Node newLast = new Node();
		newLast.item  = item;
		newLast.next = null;
		if (isEmpty()) {
			first = last;
		} else {
			oldLast.next = last;
		}		
	}

}