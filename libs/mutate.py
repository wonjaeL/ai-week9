import random

from libs.chromosome import Chromosome


class Mutater:
    gene_set = '0123456789'

    def __init__(self, answer):
        self.answer = answer

    def mutate(self, child_list):
        return self.__mutate_list(child_list)

    def __mutate_list(self, child_list):
        # 돌연변이 확률
        mutate_rate = 0.2

        for i in range(len(child_list)):
            if random.random() < mutate_rate:
                child_list[i] = self.__mutate_single(child_list[i])

        return child_list

    def __mutate_single(self, parent):
        childGenes = parent.genes[:]

        index = random.randrange(0, len(parent.genes))

        newGene, alternate = random.sample(self.gene_set, 2)

        childGenes[index] = alternate if childGenes[index] == newGene else newGene

        return Chromosome(childGenes, self.answer, parent=parent)
