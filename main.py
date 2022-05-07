from libs.gene import *


class BaseballGames:
    answer = ''

    def __init__(self):
        while len(set(self.answer)) != 4:
            self.answer = input("정답을 입력해주세요(4개의 서로다른 숫자): ")
        print(f'정답 : {self.answer}')

        # 목표 적합도.
        # 전부 스트라이크를 하는 것이 목표이므로, 목표의 길이에 5를 곱한 것이 목표 적합도가 된다.
        self.goal_fitness = len(self.answer) * 5
        self.solve()

    def solve(self):
        solver = GeneticSolver(self.answer)

        random.seed()

        # 1세대 부모 리스트를 생성한다.
        chromosome_list = solver.first_generation
        solver.display.print(chromosome_list)

        maximum_average = 0
        average = -sys.maxsize
        while average < self.goal_fitness:

            # 이전 세대의 부모 리스트로부터 자식 리스트를 선택한다.
            child_list = solver.generate_child(chromosome_list)

            # 평균 적합도를 구한다.
            average = sum(child.fitness for child in child_list) / 10

            # 이전 세대들의 최대 적합도보다 현재 세대의 적합도가 더 높다면
            # 현재 세대를 부모 리스트로 삼고 최대 적합도도 갱신한다.
            if average > maximum_average:
                print(f'이전 세대 최대 적합도: {maximum_average}, 새로운 최대 적합도: {average}')
                chromosome_list = child_list
                maximum_average = average

                solver.display.print(child_list)
                print('-' * 15)


if __name__ == '__main__':
    BaseballGames()
