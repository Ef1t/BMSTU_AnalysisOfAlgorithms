#include <iostream>
#include "ordinary.h"
#include "parallelQueue.h"
#include "parallelDistribution.h"

class Timer {
private:
    using clock_t = std::chrono::high_resolution_clock;
    using second_t = std::chrono::duration<double, std::ratio<1>>;

    std::chrono::time_point<clock_t> m_beg;

public:
    Timer() : m_beg(clock_t::now()) {
    }

    void reset() {
        m_beg = clock_t::now();
    }

    double elapsed() const {
        return std::chrono::duration_cast<second_t>(clock_t::now() - m_beg).count();
    }
};

void print_arr(std::vector<int> arr) {
    for (int i = 0; i < arr.size(); i++) {
        std::cout << arr[i] << " ";
    }
}
int iterations = 1;
int time_analysis() {

    Timer timer;

    int arr_amount = 100000;
    int arr_size = 10000;

    std::vector<std::vector<int>> arr;

    for (int i = 0; i < arr_amount; i++) {
        std::vector<int> sub_arr;
        for (int j = 0; j < arr_size; j++) {
            sub_arr.push_back(rand() % 9 + 1);
        }
        arr.push_back(sub_arr);
    }


//    std::vector<int> arr;
//
//    for (int i = 0; i < arr_amount; i++) {
//        arr.push_back(random() % 1000 + 1);
//    }

    for (int threads = 1; threads < 32; threads *= 2) {
        timer.reset();
        for (int i = 0; i < iterations; i++) {
            count_sum_parallel_distribution(arr, threads);
        }
        std::cout << threads << " " << timer.elapsed() / iterations << std::endl;
    }

    return 0;
}

std::vector<std::vector<int>> create_arr(int len_arr, int len_subarr){
    std::vector<std::vector<int>> arr;

    for (int i = 0; i < len_arr; i++) {
        std::vector<int> subarr;
        for (int j = 0; j < len_subarr; j++){
            subarr.push_back(rand() % 9 + 1);
        }
        arr.push_back(subarr);
    }

    return arr;
}

int time_analysis_common(){
    Timer timer;
    for (int i = 10000; i < 100001; i = i + 10000) {
        std::vector<std::vector<int>> arr = create_arr(i, 10000);
        timer.reset();
        for (int i = 0; i < iterations; i++) {
            count_sum_ordinary(arr);
            //count_sum_parallel_distribution(arr, 16);
            //count_sum_parallel_queue(arr, 16);
        }
        std::cout << i << " " << timer.elapsed() / iterations << std::endl;
    }


    return 0;
}


int main() {

    //std::cout << time_analysis();
    std::cout << time_analysis_common();
//    int arr_amount = 100;
//    int arr_size = 100;
//
//    std::vector<std::vector<int>> arr;
//
//    for (int i = 0; i < arr_amount; i++) {
//        std::vector<int> sub_arr;
//        for (int j = 0; j < arr_size; j++) {
//            sub_arr.push_back(rand() % 9 + 1);
//        }
//        arr.push_back(sub_arr);
//    }

    //count_sum_parallel_queue(arr, 2);
//    std::vector<int> kek;
//    std::vector<int> lol = {123, 23, 23};
//    kek = count_sum_parallel_queue(lol, 2);
//    print_arr(kek);

    return 0;
}
