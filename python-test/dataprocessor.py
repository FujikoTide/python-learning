from dataclasses import dataclass
from typing import Dict, List


@dataclass
class DataProcessor:
    def load_data(self, source) -> str:
        return f"loading data from {source}"

    def process_data(self, data) -> str:
        return f"processing data from {data}"


@dataclass
class CSVProcessor(DataProcessor):
    def load_data(self, source) -> str:
        return f"loading CSV data from {source}"

    def process_data(self, data) -> str:
        return f"processing CSV data from {data}"


@dataclass
class JSONProcessor(DataProcessor):
    def load_data(self, source) -> str:
        return f"loading JSON data from {source}"

    def process_data(self, data) -> str:
        return f"processing JSON data from {data}"


def run_processor(processor_instance, source, data):
    load_data = processor_instance.load_data(source)
    processed_data = processor_instance.process_data(data)
    return f"data loaded: {load_data}, data processed: {processed_data}"


data_processor = DataProcessor()
csv_processor = CSVProcessor()
json_processor = JSONProcessor()


# practice for data abstraction, although in this case I think it's a bit more useful too, also the name is somewhat tongue in cheek, types are also for purposes of practice and so on
@dataclass
class ProcessProcessors:
    processor: DataProcessor | CSVProcessor | JSONProcessor
    source: str
    data: List | Dict | str


processor_list = [
    ProcessProcessors(
        processor=data_processor, source="random path 1", data="dummy data"
    ),
    ProcessProcessors(
        processor=csv_processor, source="random path 2", data="dummy CSV data"
    ),
    ProcessProcessors(
        processor=json_processor, source="random path 3", data="dummy JSON data"
    ),
]


# trying to remember to run this Function
def display_processors(processor_list):
    for processor in processor_list:
        print(run_processor(processor.processor, processor.source, processor.data))


display_processors(processor_list)
