# Counter-sort
This Algorithm uses iteration to sort elemnts in the array with a time complexity of $`O(n^2)`$.

## Setup
### Usage in Python
```python
import {counter-sort} from '@Preetham-ai/counter-sort'

test_list=[3,2,5,2,3,6,99,72]
print(counter-sort(test_list))
```
### Usage in Rust
```rust
fn main() {
    let test_list = vec![3,2,5,2,3,6,99,72];
    let result = counter_sort(test_list);
    println!("{:?}", result);
} ```