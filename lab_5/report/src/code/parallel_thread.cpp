static void count_letters_in_object (WorkObject& object,
                                  size_t start_letter,
                                  size_t end_letter) {
    for (size_t i = start_letter; i < end_letter; i++) {
        object.result[object.string[i] - 'a']++;
    }
}

std::mutex allThreadsLock;


void threadWork(const int thread_number,
                const int threads_amount, 
                std::queue<WorkObject>& threads_queue,
                std::queue<WorkObject>& next_thread_queue,
                size_t objects_to_process,
                std::mutex& threads_mutex,
                std::mutex& next_threads_mutex) {
    MyTimer timerThreadWork;
    size_t sleepTime;
    size_t processed = 0;
    while(processed != objects_to_process) {
        if (threads_queue.size()) {
            WorkObject object = threads_queue.front();

            threads_mutex.lock();
            threads_queue.pop();
            threads_mutex.unlock();

            count_letters_in_object(object,
                                object.string.length() *
                                (double)thread_number /
                                threads_amount,
                                object.string.length() *
                                (double)(thread_number + 1) /
                                threads_amount);

            next_threads_mutex.lock();
            next_thread_queue.push(object);
            next_threads_mutex.unlock();

            processed++;
        } else {
            usleep(1000);
            sleepTime += 1;
        }
    }

    allThreadsLock.lock();
    std::cout << "Thread # " << thread_number <<
                 " worked for " << timerThreadWork.elapsed() <<
                 " seconds" << std::endl;

    std::cout << "Thread # " << thread_number <<
                 " sleeped for " << sleepTime <<
                 " milliseconds" << std::endl;
    allThreadsLock.unlock();
}