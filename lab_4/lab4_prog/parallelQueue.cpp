//
// Created by ef1t on 24.11.2020.
//

#include "parallelQueue.h"
#include <iostream>
std::mutex mtx;

static void parallel_subfunction(const std::vector<std::vector<int>> numbers, int &ind, std::vector<int> &res) {

    while (true) {

        mtx.lock();
        if (ind >= numbers.size()) {
            mtx.unlock();
            break;
        }
        int cur_ind = ind++;
        mtx.unlock();
        int result = 0;
        for (int i = 0; i < numbers[cur_ind].size(); i++) {
            result = result + numbers[cur_ind][i];
        }
        mtx.lock();
        res.push_back(result);
        mtx.unlock();
    }
}

//static void parallel_subfunction(const std::vector<int> numbers, int &ind, std::vector<int> &res) {
//
//    while (true) {
//
//        mtx.lock();
//        if (ind >= numbers.size()) {
//            mtx.unlock();
//            break;
//        }
//        int cur_ind = ind++;
//        mtx.unlock();
//        int result = 0;
//
//        int help = numbers[cur_ind];
//
//        while ( help != 0)
//        {
//            result += help % 10;
//            help /= 10;
//        }
//        //std::cout<<result<<" ";
//        mtx.lock();
//        res.push_back(result);
//        mtx.unlock();
//    }
//}


std::vector<int> count_sum_parallel_queue(const std::vector<std::vector<int>> numbers, int threads_amount) {
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

//std::vector<int> count_sum_parallel_queue(const std::vector<int> numbers, int threads_amount) {
//    std::vector<int> res;
//    std::vector<std::thread> thread_vector;
//
//    int ind = 0;
//    for (int i = 0; i < threads_amount; i++) {
//        thread_vector.emplace_back(std::thread(parallel_subfunction,
//                                               numbers,
//                                               std::ref(ind),
//                                               std::ref(res)));
//    }
//
//    for (int i = 0; i < threads_amount; i++) {
//        thread_vector[i].join();
//    }
//
//
//    return res;
//}