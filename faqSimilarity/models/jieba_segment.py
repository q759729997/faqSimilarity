import jieba
from faqSimilarity.models.segment import Segment


class JiebaSegment(Segment):

    def __init__(self):
        pass

    def cut(self, sentence, cut_all=False):
        """ 分词.

            @params:
                sentence - 待分词文本.
                cut_all - 是否使用精确模式.

            @return:
                On success - 单词列表.
                On failure - 错误信息.
        """
        return list(jieba.cut(sentence, cut_all=cut_all))
