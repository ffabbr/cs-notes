
/**
 * A singly-linked list of integer values with fast addFirst and addLast methods
 */


 /**
 * Separate file:
 *
 * public class IntNode {
 *
 *     private int value;
 *     private IntNode next;
 *
 *     public IntNode(int value) {
 *         this.value = value;
 *     }
 *
 *     public int getValue() {
 *         return value;
 *     }
 *
 *     public void setValue(int value) {
 *         this.value = value;
 *     }
 *
 *     public void setNext(IntNode next) {
 *         this.next = next;
 *     }
 *
 *     public IntNode getNext() {
 *         return next;
 *     }
 * }
 */
public class LinkedIntList {

    private IntNode first;
    private IntNode last;
    private int size;

    // Getter / Setter Methods for class

    public IntNode getFirst() {
        return first;
    }

    public void setFirst(IntNode first) {
        this.first = first;
    }

    public IntNode getLast() {
        return last;
    }

    public void setLast(IntNode last) {
        this.last = last;
    }

    public void setSize(int size) {
        this.size = size;
    }

    /**
     * Returns the size of the list
     */
    int getSize() {
        return this.size;
    }

    /**
     * Returns the integer value of the node at position 'index'.
     */
    int get(int index) {
        return getNode(index).getValue();
    }

    /**
     * Set the integer value at position 'index' to 'value'
     */
    void set(int index, int value) {
        getNode(index).setValue(value);
    }

    /**
     * Returns whether the list is empty (has no values)
     */
    boolean isEmpty() {
        return size == 0;
    }

    /**
     * Inserts a node with value 'value' at position 0 in the list.
     */
    void addFirst(int value) {
        IntNode newNode = new IntNode(value);
        newNode.setNext(first);
        first = newNode;
        if(last == null)
            last = newNode;
        size++;
    }

    /**
     * Appends a node with value 'value' at the end of the list.
     */
    void addLast(int value) {
        IntNode newNode = new IntNode(value);
        if(isEmpty())
            first = newNode;
        else
            last.setNext(newNode);

        last = newNode;
        size++;
    }

    /**
     * Removes the first node of the list and returns its value.
     */
    int removeFirst() {
        if(isEmpty()) {
            Errors.error("removeFirst() on empty list!");
        }

        int value = first.getValue();
        if(first == last) {
            // List has only one element, so just clear it
            clear();
        }
        else {
            first = first.getNext();
            size--;
        }

        return value;
    }

    /**
     * Removes the last node of the list and returns its value.
     */
    int removeLast() {
        if(isEmpty()) {
            Errors.error("removeLast() on empty list!");
        }

        int value = last.getValue();
        if(first == last) {
            // List has only one element, so just clear it
            clear();
        }
        else {
            // List has more than one element
            IntNode currentNode = first;
            while(currentNode.getNext() != last)
                currentNode = currentNode.getNext();

            currentNode.setNext(null);
            last = currentNode;
            size--;
        }
        return value;
    }

    /**
     * Removes all nodes from the list, making the list empty.
     */
    void clear() {
        first = last = null;
        size = 0;
    }

    /**
     * Returns a new int-array with the same contents as the list.
     */
    int[] toArray() {
        int[] array = new int[size];
        int i = 0;
        for(IntNode n = first; n != null; n = n.getNext(), i++)
            array[i] = n.getValue();
        return array;
    }

    /**
     * For internal use only.
     */
    IntNode getNode(int index) {
        if(index < 0 || index >= size) {
            Errors.error("getNode() with invalid index: " + index);
        }

        IntNode current = first;
        for(int i = 0; i < index; i++)
            current = current.getNext();
        return current;
    }
}
