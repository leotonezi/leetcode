fn main() {
    let matrix = vec![vec![1,3,5,7], vec![10,11,16,20], vec![23,30,34,60]];
    let target = 23;
    let result = matrix_binary_search(matrix, target);
    println!("Result: {}", result);
}

fn matrix_binary_search(matrix: Vec<Vec<i32>>, target: i32) -> bool {
    let mut left = 0;
    let n = matrix[0].len();
    let right = matrix.len() * n - 1;

    while left <= right {
        let mid = (left + right) / 2;
        let mid_element = matrix[mid / n][mid % n];

        if mid_element == target {
            return true;
        }
        if mid_element < target {
            left = mid + 1;
        } else {
    }
    false
}

