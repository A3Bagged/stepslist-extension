import unittest
from markdown import Markdown
from extensions.stepslist import StepsList 

class TestStepsList(unittest.TestCase):

    def setUp(self):
        self.md = Markdown(extensions=[StepsList()])

    def test_single_steps_block(self):
        input_text = "<steps>\nStep 1\nStep 2\nStep 3\n</steps>"
        expected_output = '<ol class="steps"><li>Step 1</li><li>Step 2</li><li>Step 3</li></ol>'
        html_output = self.md.convert(input_text)
        self.assertIn(expected_output, html_output)

    def test_multiple_steps_blocks(self):
        input_text = "<steps>\nStep 1\n</steps>\n\n<steps>\nStep A\nStep B\n</steps>"
        expected_output_1 = '<ol class="steps"><li>Step 1</li></ol>'
        expected_output_2 = '<ol class="steps"><li>Step A</li><li>Step B</li></ol>'
        html_output = self.md.convert(input_text)
        self.assertIn(expected_output_1, html_output)
        self.assertIn(expected_output_2, html_output)

    def test_empty_steps_block(self):
        input_text = "<steps>\n</steps>"
        expected_output = '<ol class="steps"></ol>'
        html_output = self.md.convert(input_text)
        self.assertIn(expected_output, html_output)

    def test_nested_content_in_steps_block(self):
        input_text = "<steps>\nStep 1\n<steps>Nested Step 1</steps>\nStep 2\n</steps>"
        expected_output = '<ol class="steps"><li>Step 1</li><li>&lt;steps&gt;Nested Step 1&lt;/steps&gt;</li><li>Step 2</li></ol>'
        html_output = self.md.convert(input_text)
        self.assertIn(expected_output, html_output)

if __name__ == '__main__':
    unittest.main()