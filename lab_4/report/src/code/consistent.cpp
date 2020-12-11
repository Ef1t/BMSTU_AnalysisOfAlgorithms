std::vector<int> count_sum_ordinary(
	std::vector<std::vector<int>> numbers) {
    std::vector<int> res;

    for (int i = 0; i < numbers.size(); i++) {
        int result = 0;
        for (int j = 0; j < numbers[i].size(); j++) {
            result = result + numbers[i][j];
        }
        res.push_back(result);
    }

    return res;
}