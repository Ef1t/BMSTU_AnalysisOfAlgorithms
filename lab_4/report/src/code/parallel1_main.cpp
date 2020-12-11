std::vector<int> count_sum_parallel_queue
        (const std::vector<std::vector<int>> numbers, 
                                    int threads_amount) {
    std::vector<int> res;
    std::vector<std::thread> thread_vector;

    int ind = 0;
    for (int i = 0; i < threads_amount; i++) {
        thread_vector.emplace_back(std::thread(parallel_subfunction,
                                               numbers,
                                               std::ref(ind),
                                               std::ref(res)));
    }

    for (int i = 0; i < threads_amount; i++) {
        thread_vector[i].join();
    }

    return res;
}