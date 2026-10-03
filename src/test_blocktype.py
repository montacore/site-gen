import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        test = """
####### Heading
            """
        testCase = block_to_block_type(test)
        self.assertNotEqual(testCase, BlockType.heading)

    def test_quotes(self):
        test = """
> This is a quote
> as well as this
but this is not
> uh oh
            """
        res = block_to_block_type(test)
        self.assertNotEqual(res, BlockType.quote)

    def test_ordered_list(self):
        test = """
1. Test
2. Testeroo
4. Oops
5. Spaghettios on ya tits
            """
        res = block_to_block_type(test)
        self.assertNotEqual(res, BlockType.unordered_list)

