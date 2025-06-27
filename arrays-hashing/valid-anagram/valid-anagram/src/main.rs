use std::collections::HashMap;

fn valid_anagram(s: &String, t: &String) -> bool {
    if s.len() != t.len() {
        return false;
    }

    let mut char_count: HashMap<char, i32> = HashMap::new();
    for ch in s.chars() {
        *char_count.entry(ch).or_insert(0) += 1;
    }

    for ch in t.chars() {
        match char_count.get_mut(&ch) {
            Some(count) => {
                *count -= 1;
                if *count < 0 {
                    return false;
                }
            }
            None => return false,
        }
    }

    true
}
