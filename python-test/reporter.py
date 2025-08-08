from dataclasses import dataclass


@dataclass
class Reporter:
    def generate_report(self, *args, **kwargs):
        if not args and "title" in kwargs and "content" in kwargs and len(kwargs) == 2:
            title, content = kwargs["title"], kwargs["content"]
            return f"{title}\n{content}"
        elif not kwargs and args and len(args) == 1:
            return f"{args[0]}"
        return "Unknown report format"


reporter = Reporter()
print(reporter)
print(reporter.generate_report())
print(reporter.generate_report("hello"))
print(reporter.generate_report(title="hello", content="cat"))
print(reporter.generate_report("hello", title="cat", content="velociraptor"))
