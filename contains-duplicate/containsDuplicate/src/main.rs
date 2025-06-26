fn main() {
    let nums = vec![1, 2, 3, 4, 5];
    println!("Contains duplicate: {}", contains_duplicate(nums.clone()));
    println!(
        "Contains duplicate (sorted): {}",
        contains_duplicate_sorted(nums)
    );
}

fn contains_duplicate(nums: Vec<i32>) -> bool {
    let mut set = std::collections::HashSet::new();
    for num in nums {
        if !set.insert(num) {
            return true;
        }
    }
    false
}

fn contains_duplicate_sorted(mut nums: Vec<i32>) -> bool {
    nums.sort();
    nums.windows(2).any(|w| w[0] == w[1])
}
