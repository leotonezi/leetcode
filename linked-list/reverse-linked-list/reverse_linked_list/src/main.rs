#[derive(Debug)]
struct ListNode {
    val: i32,
    next: Option<Box<ListNode>>,
}

fn main() {
    let head = Some(Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 2,
            next: Some(Box::new(ListNode { val: 3, next: None })),
        })),
    }));
    let reversed_head = reverse_list(head);
    println!("{:?}", reversed_head);
}

fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut prev = None;
    let mut curr = head;
    
    while let Some(mut curr_node) = curr {
        let next = curr_node.next.take();
        curr_node.next = prev;
        prev = Some(curr_node);
        curr = next;
    }
    
    prev
}