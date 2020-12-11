int tests(size_t words_amount, size_t letters_in_word) {
    std::vector<std::string> strings;
    for (size_t i = 0; i < words_amount; i++) {
        std::string string;
        for (size_t j = 0; j < letters_in_word; j++) {
            string.push_back(rand() % LETTERS_IN_ENG_ALPHABET + 'a');
        }
        strings.emplace_back(string);
    }

    std::vector<WorkObject> result_consistent =
                            initLinearWork(strings, 3);
                            
    std::vector<WorkObject> result_conveyor =
                            initConveyorWork(strings, 3);
    if (result_consistent != result_conveyor) {
        return EXIT_FAILURE;
    }   
    
    return EXIT_SUCCESS;
}