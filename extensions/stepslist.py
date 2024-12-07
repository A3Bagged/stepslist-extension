from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re

class StepsPreprocessor(Preprocessor):
    STEPS_RE = re.compile(r'(?s)<steps>(.*?)</steps>')

    def run(self, lines):
        text = "\n".join(lines)
        while True:
            match = self.STEPS_RE.search(text)
            if not match:
                break

            steps_content = match.group(1).strip()
            steps_lines = steps_content.split('\n')
            steps_list_items = ''.join(f'<li>{line.strip()}</li>' for line in steps_lines if line.strip())
            steps_html = f'<ol class="steps">{steps_list_items}</ol>'

            text = f'{text[:match.start()]}{steps_html}{text[match.end():]}'

        return text.split('\n')

class StepsList(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(StepsPreprocessor(md), 'steps_preprocessor', 25)

def makeExtension(**kwargs):
    return StepsList(**kwargs)