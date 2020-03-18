"""
    main_module - NGram分词，测试是将对应方法的@unittest.skip注释掉.

    Main members:

        # __main__ - 程序入口.
"""
import unittest
import sys

sys.path.insert(0, './')  # 定义搜索路径的优先顺序，序号从0开始，表示最大优先级

import faqSimilarity  # noqa
print('faqSimilarity module path :{}'.format(faqSimilarity.__file__))  # 输出测试模块文件位置
from faqSimilarity.models.ngram_segment import NGramSegment  # noqa


class TestNGramSegment(unittest.TestCase):
    """ NGram分词.

    Main methods:
        test_cut - 测试NGram分词.
    """

    # @unittest.skip('debug')
    def test_cut(self):
        """ 测试NGram分词.
        """
        print('{} test_cut {}'.format('-'*15, '-'*15))
        segment_model = NGramSegment()
        texts = [
            '温都尔站',
            '东乌广厦',
            '国电四郎',
            '阿尔善站',
            '朱日和基'
        ]
        for text in texts:
            print(segment_model.cut(text))
        """
        ['温都', '都尔', '尔站']
        ['东乌', '乌广', '广厦']
        ['国电', '电四', '四郎']
        ['阿尔', '尔善', '善站']
        ['朱日', '日和', '和基']
        """


if __name__ == "__main__":
    unittest.main()  # 运行当前源文件中的所有测试用例
