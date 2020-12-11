static void parallel_subfunction(
    const std::vector<std::vector<int>> numbers, 
                                        int &ind, 
                            std::vector<int> &res) {

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