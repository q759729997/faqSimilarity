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
            '我来到北京清华大学',
            '他来到了网易杭研大厦',
            '小明硕士毕业于中国科学院计算所'
        ]
        for text in texts:
            print(segment_model.cut(text))
        """
        ['我', '来到', '北京', '清华大学']
        ['他', '来到', '了', '网易', '杭研', '大厦']
        ['小明', '硕士', '毕业', '于', '中国科学院', '计算所']
        """
        for text in texts:
            print(segment_model.cut(text, cut_all=True))
        """
        ['我', '来到', '北京', '清华', '清华大学', '华大', '大学']
        ['他', '来到', '了', '网易', '杭', '研', '大厦']
        ['小', '明', '硕士', '毕业', '于', '中国', '中国科学院', '科学', '科学院', '学院', '计算', '计算所']
        """


if __name__ == "__main__":
    unittest.main()  # 运行当前源文件中的所有测试用例
