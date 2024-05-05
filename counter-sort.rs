fn counter_sort(lst: Vec<usize>) -> Vec<usize> {
    let mut counter = 0;
    let mut sorted_list = Vec::new();

    while sorted_list.len() < lst.len() {
        counter += 1;
        if lst.contains(&counter) {
            sorted_list.push(counter);
        }
    }

    sorted_list
}
