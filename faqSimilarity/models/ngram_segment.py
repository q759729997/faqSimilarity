from ngram import NGram
from faqSimilarity.models.segment import Segment


class NGramSegment(Segment):

    def __init__(self, N=2, pad_len=0):
        self.model = NGram(N=N, pad_len=pad_len)

    def cut(self, sentence):
        """ 分词.

            @params:
                sentence - 待分词文本.

            @return:
                On success - 单词列表.
                On failure - 错误信息.
        """
        return list(list(self.model.split(sentence)))
