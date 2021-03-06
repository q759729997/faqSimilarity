import jieba
from faqSimilarity.models.segment import Segment


class JiebaSegment(Segment):

    def __init__(self, cut_all=False):
        # cut_all - 是否使用精确模式.
        self.cut_all = cut_all
        pass

    def cut(self, sentence):
        """ 分词.

            @params:
                sentence - 待分词文本.

            @return:
                On success - 单词列表.
                On failure - 错误信息.
        """
        return list(jieba.cut(sentence, cut_all=self.cut_all))
