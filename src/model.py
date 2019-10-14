
# python-dateutil
import dateutil.parser

from pytils import base, check


class EventTimeline:
    def __init__(self, data):
        self.events = sorted(self.ingest(data))

    def ingest(self, data):
        events = []
        names = set()

        for data_event in data["events"]:
            event = Event(data_event)
            events += [event]

            if event.name in names:
                raise ValueError("EventTimeline duplicates event name: %s." % event.name)
            else:
                names.add(event.name)

        if len(events) == 0:
            raise ValueError("EventTimeline must have at least 1 event.")

        return events

    def as_json(self):
        return {
            "events": [event.as_json() for event in self.events]
        }


class Event(base.Comparable):
    def __init__(self, data):
        super(Event, self).__init__()
        self.name, self.blocks = self.ingest(data)
        self.blocks = sorted(self.blocks)
        self.start = self.blocks[0]

    def _comparator(self, fn, other):
        return fn(self.start, other.start)

    def ingest(self, data):
        name = data["name"]
        blocks = []

        for data_block in data["blocks"]:
            block = Block(data_block)
            blocks += [block]

        if len(blocks) == 0:
            raise ValueError("Event must have at least 1 block.")

        return name, blocks

    def as_json(self):
        return {
            "name": self.name,
            "blocks": [block.as_json() for block in self.blocks]
        }


class Block(base.Comparable):
    def __init__(self, data):
        super(Block, self).__init__()
        self.start, self.end, self.marks = self.ingest(data)
        self.marks = sorted(self.marks)

    def _comparator(self, fn, other):
        return fn(self.start, other.start)

    def ingest(self, data):
        start = dateutil.parser.parse(data["start"])
        end = dateutil.parser.parse(data["end"])

        if start > end:
            raise ValueError("Block start '%s' occurs after end '%s'." % (start.isoformat(), end.isoformat()))

        marks = []

        for data_mark in data["marks"]:
            mark = Mark(data_mark)
            marks += [mark]

        return start, end, marks

    def as_json(self):
        return {
            "start": self.start.isoformat(),
            "end": self.end.isoformat(),
            "marks": [mark.as_json() for mark in self.marks]
        }


class Mark(base.Comparable):
    POINT = "point"
    SPAN = "span"

    def __init__(self, data):
        self.kind, self.timestamp, self.start, self.end = self.ingest(data)

    def _comparator(self, fn, other):
        return fn(self.first(), other.first())

    def first(self):
        if self.kind == Mark.POINT:
            return self.timestamp
        else:
            return self.start

    def ingest(self, data):
        kind = data["kind"]

        if kind == Mark.POINT:
            timestamp = dateutil.parser.parse(data["timestamp"])
            start = None
            end = None
        elif kind == Mark.SPAN:
            timestamp = None
            start = dateutil.parser.parse(data["start"])
            end = dateutil.parser.parse(data["end"])

            if start > end:
                raise ValueError("Mark start '%s' occurs after end '%s'." % (start.isoformat(), end.isoformat()))
        else:
            raise ValueError("Mark unknown kind: %s" % kind)

        return kind, timestamp, start, end

    def as_json(self):
        return {
            "kind": self.kind,
            "timestamp": None if self.timestamp is None else self.timestamp.isoformat(),
            "start": None if self.start is None else self.start.isoformat(),
            "end": None if self.end is None else self.end.isoformat(),
        }

