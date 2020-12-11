//
// Created by ef1t on 25.11.2020.
//

#include "parallelDistribution.h"
#include <iostream>
std::mutex mtl;

static void parallel_subfunction(std::vector<std::vector<int>> &numbers, int start, int end, std::vector<int> &res) {

    for (int i = start; i < end; i++) {
        int result = 0;
        for (int j = 0; j < numbers[i].size(); j++) {
            result = result + numbers[i][j];
        }
        //mtl.lock();
        res[i] = result;
        //mtl.unlock();
    }
}

std::vector<int> count_sum_parallel_distribution(std::vector<std::vector<int>> numbers, int threads_amount) {
    std::vector<int> res(numbers.size());

    std::vector<std::thread> thread_vector;

    for (int i = 0; i < threads_amount; i++) {
        int start = ((double)numbers.size() / threads_amount * i);
        int end = ((double)numbers.size() / threads_amount * (i + 1));
        thread_vector.emplace_back(std::thread(parallel_subfunction,
                                               ref(numbers),
                                               start,
                                               end,
                                               std::ref(res)));
    }

    for (int i = 0; i < threads_amount; i++) {
        thread_vector[i].join();
    }


    return res;
}
