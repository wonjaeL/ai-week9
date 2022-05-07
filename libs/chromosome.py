# 단순한 염색체 클래스이다.
# 유전자 정보와 적합도 정보를 담고 있다.
class Chromosome:

    def __init__(self, genes, answer, parent=None):
        self.genes = genes
        self.answer = answer
        self.parent = parent

    def __str__(self):
        return ''.join(self.genes)

    @property
    def generation(self):
        count = 1
        parent = self.parent
        while parent:
            count += 1
            parent = parent.parent
        return count

    # 스트라이크는 5점, 볼은 1점으로 하여 계산한다.
    @property
    def fitness(self):
        fitness = 0
        for i, num in enumerate(self.genes):
            if self.answer[i] == num:  # 스트라이크
                fitness += 5
            elif num in self.answer:  # 볼
                fitness += 1
        return fitness
