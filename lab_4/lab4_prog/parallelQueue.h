//
// Created by ef1t on 24.11.2020.
//

#ifndef PROG_EF1T_PARALLELQUEUE_H
#define PROG_EF1T_PARALLELQUEUE_H

#include <vector>
#include <thread>
#include <mutex>

std::vector<int> count_sum_parallel_queue(std::vector<std::vector<int>> numbers, int threads_amount);
//std::vector<int> count_sum_parallel_queue(std::vector<int> numbers, int threads_amount);
#endif //PROG_EF1T_PARALLELQUEUE_H
