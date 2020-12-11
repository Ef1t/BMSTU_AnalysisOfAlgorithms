static void count_letters_in_object(work_object& object,
                                 size_t start_letter,
                                 size_t end_letter) {
    for (size_t i = start_letter; i < end_letter; i++) {
        object.result[object.string[i] - 'a']++;
    }
}

void linear_worker(std::queue<work_object>& objects,
                  const size_t worker_number,
                  const size_t worker_amount,
                  size_t elements_to_process) {
    for (size_t i = 0; i < elements_to_process; i++) {
        work_object object = objects.front();
        objects.pop();
        count_letters_in_object(object,
                             object.string.length() *
                             (double)worker_number /
                             worker_amount,
                             object.string.length() *
                             (double)(worker_number + 1) /
                             worker_amount);
        objects.push(object);
    }
}

std::vector<work_object> init_linear_work(
                        std::vector<std::string>& strings,
                        const int worker_amount) {
    std::queue<work_object> objects;
    for (auto& string : strings) {
        objects.emplace(work_object(string));
    }
    MyTimer Timer;
    for (int i = 0; i < worker_amount; i++) {
        linear_worker(objects, i, worker_amount, strings.size());
    }
    std::cout << "Linear algorithm works for: " <<
                 Timer.elapsed() <<
                 " seconds" << std::endl;
    std::vector<work_object> result;
    while (!objects.empty()) {
        result.push_back(objects.front());
        objects.pop();
    }
    return result;
}