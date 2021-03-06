"""
    main_module - 结巴分词，测试是将对应方法的@unittest.skip注释掉.

    Main members:

        # __main__ - 程序入口.
"""
import unittest
import sys

sys.path.insert(0, './')  # 定义搜索路径的优先顺序，序号从0开始，表示最大优先级

import faqSimilarity  # noqa
print('faqSimilarity module path :{}'.format(faqSimilarity.__file__))  # 输出测试模块文件位置
from faqSimilarity.models.jieba_segment import JiebaSegment  # noqa


class TestJiebaSegment(unittest.TestCase):
    """ 结巴分词.

    Main methods:
        test_cut - 测试结巴分词.
    """

    # @unittest.skip('debug')
    def test_cut(self):
        """ 测试结巴分词.
        """
        print('{} test_cut {}'.format('-'*15, '-'*15))
        segment_model = JiebaSegment()
        texts = [
            '温都尔站',
            '东乌广厦',
            '国电四郎',
            '阿尔善站',
            '朱日和基'
        ]
        print('{} 默认模式 {}'.format('-'*15, '-'*15))
        for text in texts:
            print(segment_model.cut(text))
        """
        ['温都尔', '站']
        ['东乌', '广厦']
        ['国电', '四郎']
        ['阿尔善', '站']
        ['朱日', '和', '基']
        """
        segment_model = JiebaSegment(cut_all=True)
        print('{} 精确匹配模式 {}'.format('-'*15, '-'*15))
        for text in texts:
            print(segment_model.cut(text))
        """
        ['温都尔', '站']
        ['东', '乌', '广厦']
        ['国电', '四', '郎']
        ['阿', '尔', '善', '站']
        ['朱', '日', '和', '基']
        """


if __name__ == "__main__":
    unittest.main()  # 运行当前源文件中的所有测试用例
