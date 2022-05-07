import random


class Shuffler:

    def __init__(self):
        pass

    def shuffle(self, child_list):
        # 무작위의 두 자식 유전자를 선택해 서로를 섞는다.
        # crossover_rate는 어떤 유전자가 섞일 확률이다.
        # 현실에서의 교배와 같은 개념이다.
        crossover_rate = 0.2  # 곱하기 100을 하면 백분율을 알 수 있다.

        # 예를 들어 crossover_rate가 0.2라면, 20%의 자식이 서로 유전자가 섞인다는 의미이다.
        selected = None

        for i in range(len(child_list)):
            if random.random() < crossover_rate:  # random은 0부터 1 사이의 값이므로, 이 값이 0.2보다 작을 확률은 0.2, 즉 20%이다.
                continue

            selected = i

            child_list[selected].genes[2:], child_list[i].genes[2:] = child_list[i].genes[2:], child_list[
                                                                                                   selected].genes[
                                                                                               2:]

        # 교체된 유전자들을 반환한다.
        return child_list
