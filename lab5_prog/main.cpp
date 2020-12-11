#include <iostream>
#include <vector>
#include <queue>
#include <cstdlib>
#include "LinearWork.h"
#include "ConveyorWork.h"
#include "WorkObject.h"

int tests(size_t wordsAmount, size_t lettersInWord) {
    std::vector<std::string> strings;
    for (size_t i = 0; i < wordsAmount; i++) {
        std::string string;
        for (size_t j = 0; j < lettersInWord; j++) {
            string.push_back(rand() % LETTERS_IN_ENG_ALPHABET + 'a');
        }
        strings.emplace_back(string);
    }

    std::cout << "LINEAR" << std::endl;
    for (int i = 0; i < 5; i++) {
        std::vector<WorkObject> resultConsistent = initLinearWork(strings, 3);
    }

    std::cout << "PARALLEL" << std::endl;
    for (int i = 0; i < 5; i++) {
        std::vector<WorkObject> resultConveyor = initConveyorWork(strings, 3);
    }
    return EXIT_SUCCESS;
}

int main() {
    const int WORKERS_AMOUNT = 3;
    tests(50000, 10000);
    return 0;
}

