fn main() {
    let nums: Vec<i32> = vec![-1,0,3,5,9,12];
    let target: i32 = 2;
    let result: i32 = binary_search(nums, target);
    println!("Result: {}", result);
}

fn binary_search(nums: Vec<i32>, target: i32) -> i32 {
    let mut left = 0;
    let mut right = nums.len() - 1;

    while left <= right {
        let mid = (left + right) / 2;
        if nums[mid] == target {
            return mid as i32;
        }
        if nums[mid] < target {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    -1
}
