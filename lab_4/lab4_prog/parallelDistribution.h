//
// Created by ef1t on 25.11.2020.
//

#ifndef PROG_EF1T_PARALLELDISTRIBUTION_H
#define PROG_EF1T_PARALLELDISTRIBUTION_H

#include <vector>
#include <thread>
#include <mutex>

std::vector<int> count_sum_parallel_distribution(std::vector<std::vector<int>> numbers, int threads_amount);

#endif //PROG_EF1T_PARALLELDISTRIBUTION_H
