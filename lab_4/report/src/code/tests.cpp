int tests() {
   
    std::vector<int> res1;
    std::vector<int> res2;
    std::vector<int> res3;


    int arr_amount = 400;
    int arr_size = 100;

    std::vector<std::vector<int>> arr;

    for (int i = 0; i < arr_amount; i++) {
        std::vector<int> sub_arr;
        for (int j = 0; j < arr_size; j++) {
            sub_arr.push_back(rand() % 9 + 1);
        }
        arr.push_back(sub_arr);
    }

    res1 = count_sum_ordinary(arr);
    res2 = count_sum_parallel_queue(arr, 16);
    res3 = count_sum_parallel_distribution(arr, 16);

    if (arr1 == arr2 == arr3) return 0;
    else return -1;


    return 0;
}