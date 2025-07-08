fn main() {
    let s = "A man, a plan, a canal: Panama";
    println!("{}", is_palindrome(s));
}

fn is_palindrome(s: &str) -> bool {
    let bytes = s.as_bytes();
    let mut left = 0;
    let mut right = bytes.len() - 1;

    while left < right {
        while left < right && !bytes[left].is_ascii_alphanumeric() {
            left += 1;
        }

        while left < right && !bytes[right].is_ascii_alphanumeric() {
            right -= 1;
        }

        if bytes[left].to_ascii_lowercase() != bytes[right].to_ascii_lowercase() {
            return false;
        }

        left += 1;
        right -= 1;
    }
    true
}