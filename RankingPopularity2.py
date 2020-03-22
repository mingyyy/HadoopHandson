from mrjob.job import MRJob
from mrjob.step import MRStep


class RankingPopularity2(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_movie_count,
                   reducer=self.reducer_count),
            MRStep(reducer=self.reducer_sort)
        ]

    def mapper_movie_count(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1

    def reducer_count(self, key, values):
        yield str(sum(values)).zfill(5), key

    def reducer_sort(self, count, movies):
        for movie in movies:
            yield movie, count


if __name__ == '__main__':
    RankingPopularity2.run()