import java.util.*;
public static class BinaryTreeNode {
    public int value;
    public BinaryTreeNode left;
    public BinaryTreeNode right;

    public BinaryTreeNode(int value) {
        this.value = value;
    }

    public BinaryTreeNode insertLeft(int leftValue) {
        this.left = new BinaryTreeNode(leftValue);
        return this.left;
    }

    public BinaryTreeNode insertRight(int rightValue) {
        this.right = new BinaryTreeNode(rightValue);
        return this.right;
    }

}

class myCode {

    public ArrayList<Integer> getAllDepths(BinaryTreeNode root) {
        Stack holder = new Stack();
        BinaryTreeNode currentNode = root;
        ArrayList<Integer> depthHolder = new ArrayList<Integer>();
        while (true) {
            holder.push(currentNode);
            if (currentNode.left == null) {
                if (currentNode.right == null) {

                }
                holder.pop();

                currentNode = holder.top();
            }
            currentNode = currentNode.left;


        }
    }

	public static void main (String[] args) throws java.lang.Exception
    {
        //Current thought: Check super balanced by doing DFS

    }
}