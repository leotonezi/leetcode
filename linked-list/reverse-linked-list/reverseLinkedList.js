function ListNode(val, next) {
    this.val = val;
    this.next = next;
}

function reverseList(head) {
    let prev = null;
    let curr = head;
    while (curr) {
        let next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

let head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
let reversedHead = reverseList(head);
console.log(reversedHead);