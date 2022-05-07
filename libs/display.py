class Display:
    def __init__(self, answer):
        self.answer = answer

    def print(self, candidate_list):
        fitness_sum = 0

        for candidate in candidate_list:
            self.__print(candidate)
            fitness_sum += candidate.fitness

        # 평균 적합도를 구해 출력한다.
        print(f'평균 적합도: {fitness_sum / len(candidate_list)}')

    def __print(self, chromosome):
        strike = 0
        ball = 0

        for expected, actual in zip(self.answer, chromosome.genes):
            if expected == actual:  # 스트라이크인 경우
                strike += 1
            elif actual in self.answer:  # 볼인 경우
                ball += 1

        result = '아웃' if not strike and not ball else f'스트라이크: {strike}, 볼: {ball}'

        # format을 이용해 자식의 유전자, 스트라이크 수 / 볼 수, 적합도를 출력한다.
        print(f'{chromosome.generation}세대 - {chromosome}\t{result}\t{chromosome.fitness}')
