static void parallel_subfunction(
        std::vector<std::vector<int>> &numbers, 
                                    int start, 
                                    int end, 
                        std::vector<int> &res) {

    for (int i = start; i < end; i++) {
        int result = 0;
        for (int j = 0; j < numbers[i].size(); j++) {
            result = result + numbers[i][j];
        }

        res[i] = result;
    }
}