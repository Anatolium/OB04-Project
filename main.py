from abc import ABC, abstractmethod

# Open/Closed Principle не используется
class Report1():
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def doc_printer(self):
        print(f"сформирован отчет - {self.title} - {self.content}")

# Open/Closed Principle используется
class Formatted(ABC):
    @abstractmethod
    def print_doc(self, report):
        pass

class TextFormatted(Formatted):
    def print_doc(self, report):
        print(report.title)
        print(report.content)

class HtmlFormatted(Formatted):
    def print_doc(self, report):
        print(f"<h1>{report.title}</h1>")
        print(f"<p>{report.content}</p>")

class Report:
    def __init__(self, title, content, format_style):
        self.title = title
        self.content = content
        self.format_style = format_style

    def doc_printer(self):
        self.format_style.print_doc(self)

report = Report("заголовок отчета", "это текст отчета, его тут много", TextFormatted())
report.doc_printer()
report_2 = Report("заголовок отчета", "это текст отчета, его тут много", HtmlFormatted())
report_2.doc_printer()
