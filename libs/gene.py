import copy
import random
import sys
from libs.chromosome import Chromosome
from libs.display import Display
from libs.mutate import Mutater
from libs.shuffle import Shuffler


class GeneticSolver:
    gene_set = '0123456789'
    chromosome_count = 10

    def __init__(self, answer):
        self.answer = answer
        self.display = Display(answer)

    @property
    def random_gene(self):
        return [random.choice(self.gene_set) for _ in range(len(self.answer))]

    @property
    def first_generation(self):
        return [Chromosome(self.random_gene, self.answer) for _ in range(self.chromosome_count)]

    def generate_child(self, parent_list):
        # 자식 유전자를 선택
        child_list = select_child(parent_list)

        # 유전자를 섞음
        child_list = Shuffler().shuffle(child_list)

        # 돌연변이
        child_list = Mutater(self.answer).mutate(child_list)
        return child_list


def select_child(parent_list):
    range_list = __get_child_range_list(parent_list)
    child_list = []
    for i in range(10):
        rand = random.random()
        before = 0
        for j in range(len(range_list)):
            if before < rand <= range_list[j]:
                child_list.append(copy.deepcopy(parent_list[j]))
                break
            before = range_list[j]
    return child_list


def __get_child_range_list(parent_list):
    fitness_sum = sum(parent.fitness for parent in parent_list)
    fitness_percent_list = [parent.fitness / fitness_sum for parent in parent_list]
    fitness_accum_list = []

    fitness_sum = 0
    for fitness_percent in fitness_percent_list:
        fitness_sum += fitness_percent
        fitness_accum_list.append(fitness_sum)

    # 합 배열을 반환해준다.
    return fitness_accum_list
