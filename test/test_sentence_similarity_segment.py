"""
    main_module - 文本相似度匹配，测试是将对应方法的@unittest.skip注释掉.

    Main members:

        # __main__ - 程序入口.
"""
import unittest
import sys

sys.path.insert(0, './')  # 定义搜索路径的优先顺序，序号从0开始，表示最大优先级

import faqSimilarity  # noqa
print('faqSimilarity module path :{}'.format(faqSimilarity.__file__))  # 输出测试模块文件位置
from faqSimilarity.models.segment import Segment  # noqa
from faqSimilarity.models.sentence_similarity import SentenceSimilarity  # noqa


class TestSentenceSimilarity(unittest.TestCase):
    """ 文本相似度匹配.

    Main methods:
        test_similarity - 文本相似度匹配.
    """

    # @unittest.skip('debug')
    def test_similarity(self):
        """ 文本相似度匹配.
        """
        print('{} test_similarity {}'.format('-'*15, '-'*15))
        texts = [
            '温都尔站',
            '东乌广厦',
            '国电四郎',
            '阿尔善站',
            '朱日和基'
        ]
        segment_model = Segment()
        similarity_model = SentenceSimilarity(segment_model)
        similarity_model.set_sentences(texts)
        similarity_model.TfidfModel()  # tfidf模型
        # similarity_model.LsiModel()         # lsi模型
        # similarity_model.LdaModel()         # lda模型
        search_texts = [
            '朱日和站',
            '温都尔站',
            '国电站'
        ]
        for text in search_texts:
            top_k = similarity_model.similarity_k(text, 2)
            search_result = [(texts[idx], score) for idx, score in zip(*top_k)]
            print('text:{}'.format(text))
            print('words:{}'.format(segment_model.cut(text)))
            print('search_result:{}'.format(search_result))
        """
        text:朱日和站
        words:['朱', '日', '和', '站']
        search_result:[('朱日和基', 0.8227205), ('温都尔站', 0.109244354)]
        text:温都尔站
        words:['温', '都', '尔', '站']
        search_result:[('温都尔站', 0.99999994), ('阿尔善站', 0.24478666)]
        text:国电站
        words:['国', '电', '站']
        search_result:[('国电四郎', 0.6559487), ('温都尔站', 0.13064952)]
        """


if __name__ == "__main__":
    unittest.main()  # 运行当前源文件中的所有测试用例
