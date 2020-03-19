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
from faqSimilarity.models.ngram_segment import NGramMixSegment  # noqa
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
            '朱日和基',
            '国调.东台变电站',
            '国调.500kv东台站',
            '四川.220kV东台变电站',
            '福建.东大I路',
            '四川.台大II路',
            '河北.东台I回',
            '河北.东台II回',
            '莆田.东台变/220kV.#1主变',
            '四川.东台变/220kV.#1主变'
        ]
        segment_model = NGramMixSegment()
        similarity_model = SentenceSimilarity(segment_model)
        similarity_model.set_sentences(texts)
        similarity_model.TfidfModel()  # tfidf模型
        # similarity_model.LsiModel()         # lsi模型
        # similarity_model.LdaModel()         # lda模型
        search_texts = [
            '朱日和站',
            '温都尔站',
            '国电站',
            '东台变#3号主变',
            '东台变',
            '东台变 东台站'
        ]
        for text in search_texts:
            top_k = similarity_model.similarity_k(text, 3)
            search_result = [(texts[idx], score) for idx, score in zip(*top_k)]
            print('text:{}'.format(text))
            print('words:{}'.format(segment_model.cut(text)))
            print('search_result:{}'.format(search_result))
        """
        text:朱日和站
        words:['朱', '日', '和', '站', '朱日', '日和', '和站']
        search_result:[('朱日和基', 0.81902415), ('温都尔站', 0.05910668)]
        text:温都尔站
        words:['温', '都', '尔', '站', '温都', '都尔', '尔站']
        search_result:[('温都尔站', 1.0), ('阿尔善站', 0.114771366)]
        text:国电站
        words:['国', '电', '站', '国电', '电站']
        search_result:[('国电四郎', 0.6219182), ('温都尔站', 0.0748035)]
        """

    @unittest.skip('debug')
    def test_similarity_LsiModel(self):
        """ 文本相似度匹配.
        """
        print('{} test_similarity {}'.format('-'*15, '-'*15))
        texts = [
            '温都尔站',
            '东乌广厦',
            '国电四郎',
            '阿尔善站',
            '朱日和基',
            '国调.东台变电站',
            '国调.500kv东台站',
            '四川.220kV东台变电站',
            '福建.东大I路',
            '四川.台大II路',
            '河北.东台I回',
            '河北.东台II回',
            '莆田.东台变/220kV.#1主变',
            '四川.东台变/220kV.#1主变'
        ]
        segment_model = NGramMixSegment()
        similarity_model = SentenceSimilarity(segment_model)
        similarity_model.set_sentences(texts)
        # similarity_model.TfidfModel()  # tfidf模型
        similarity_model.LsiModel()         # lsi模型
        # similarity_model.LdaModel()         # lda模型
        search_texts = [
            '朱日和站',
            '温都尔站',
            '国电站',
            '东台变#3号主变',
            '东台变',
            '东台变 东台站'
        ]
        for text in search_texts:
            top_k = similarity_model.similarity_k(text, 3)
            search_result = [(texts[idx], score) for idx, score in zip(*top_k)]
            print('text:{}'.format(text))
            print('words:{}'.format(segment_model.cut(text)))
            print('search_result:{}'.format(search_result))
        """
        text:朱日和站
        words:['朱日', '日和', '和站']
        search_result:[('朱日和基', 1.0), ('东乌广厦', 1.1175871e-08)]
        text:温都尔站
        words:['温都', '都尔', '尔站']
        search_result:[('温都尔站', 1.0), ('东乌广厦', 0.0)]
        text:国电站
        words:['国电', '电站']
        search_result:[('国电四郎', 0.99999994), ('朱日和基', 2.7008355e-08)]
        """


if __name__ == "__main__":
    unittest.main()  # 运行当前源文件中的所有测试用例
