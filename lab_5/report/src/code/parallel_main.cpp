std::vector<WorkObject> init_conveyor_work(
                        std::vector<std::string>& strings,
                        const int workers_amount) {
    std::queue<WorkObject> complete_objects;
    std::vector<std::queue<WorkObject>> workers_queues(workers_amount);
    std::vector<std::thread> threads;
    for (auto& string : strings) {
        workers_queues[0].push(WorkObject(string));
    }

    std::vector<std::mutex> mutexes(workers_amount + 1);
    MyTimer timerAllWork;
    for (size_t i = 0; i < workers_amount; i++) {
        threads.emplace_back(std::thread(threadWork, i,
                             workers_amount,
                             std::ref(workers_queues[i]),
                             i == workers_amount - 1 ?
                             std::ref(complete_objects) :
                             std::ref(workers_queues[i + 1]),
                             strings.size(),
                             std::ref(mutexes[i]),
                             std::ref(mutexes[i + 1])));
    }

    for (size_t i = 0; i < workers_amount; i++) {
        threads[i].join();
    }

    std::cout << "All Conveyor worked for: " <<
                 timerAllWork.elapsed() <<
                 " seconds" << std::endl;
    std::vector<WorkObject> result;
    while (!complete_objects.empty()) {
        result.push_back(complete_objects.front());
        complete_objects.pop();
    }
    return result;
}