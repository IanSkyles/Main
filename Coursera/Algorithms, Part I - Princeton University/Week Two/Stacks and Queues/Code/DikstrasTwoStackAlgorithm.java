public class DikstrasTwoStackAlgorithm {
	public static void main(String[] args) {
		Stack<String> operators = new Stack<String>();
		Stack<Double> values = new Stack<Double>();

		while (!StdIn.isEmpty()) {
			String s = StdIn.readString();
			if (s.equals("(")) {

			} else if (s.equals("+")) {
				operators.push(s);
			} else if (s.equals("*")) {
				operators.push(s);
			} else if (s.equals(")")) {
				String operator = operators.pop();
				if (operator.equals("+")) {
					values.push(values.pop() + values.pop());
				} else if (operator.equals("*")) {
					values.push(values.pop() * values.pop());
				}
			} else {
				values.push(Double.parseDouble(s));
			}
		}
		StdOut.println(values.pop());
	}
}