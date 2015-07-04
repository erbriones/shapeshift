import logging
import sys
import traceback
from datetime import datetime
try:
    import json
except ImportError:
    import simplejson as json

if sys.version_info < (3, 0):
    SIMPLE_TYPES = (basestring, bool, dict, float, int, long, list, type(None))
else:
    SIMPLE_TYPES = (str, bool, dict, float, int, list, type(None))

DEFAULT_ENCODING = "utf-8"

FORMAT_STRING = "%Y-%m-%d@%H:%M:%S"

SKIP_LIST = ("args", "asctime", "created", "exc_info", "exc_text", "filename",
             "funcName", "levelname", "levelno", "lineno", "module")


def format_timestamp(time, format_string):
    stamp = datetime.utcfromtimestamp(time)
    microseconds = (stamp.microsecond / 1000)
    return stamp.strftime(format_string) + ".%03d" % microseconds + "Z"


def format_traceback(exc_info):
    if not exc_info:
        return ""
    return "".join(traceback.format_exception(*exc_info))


class JSONFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        self.format_string = kwargs.pop("format_string", FORMAT_STRING)
        self.encoding = kwargs.pop("encoding", DEFAULT_ENCODING)
        self.tags = kwargs.pop("tags", None)
        super(JSONFormatter, self).__init__(self, *args, **kwargs)

    def get_default_fields(self, record):
        fields = {
            "@logger": record.name,
            "@levelname": record.levelname,
            "@timestamp": format_timestamp(record.created, self.format_string),
            "message": record.getMessage(),
        }

        #: add optional tags
        if self.tags is not None:
            fields["tags"] = self.tags

        return fields

    def get_debug_fields(self, record):
        fields = {
            "@exc_info": format_traceback(record.exc_info),
            "@lineno": record.lineno,
            "@process": record.process,
            "@threadName": record.threadName
        }

        #: added in python 2.5
        if hasattr(record, "processName"):
            fields["@processName"] = record.processName

        #: added in python 2.6
        if hasattr(record, "funcName"):
            fields["@funcName"] = record.funcName

        return fields

    def get_extra_fields(self, record):
        fields = {}
        for key, value in record.__dict__.items():
            if key not in SKIP_LIST:
                if isinstance(value, SIMPLE_TYPES):
                    fields[key] = value
                else:
                    fields[key] = repr(value)
        return fields

    def serialize(self, message):
        payload = json.dumps(message)
        if sys.version_info < (3, 0):
            return payload
        else:
            return bytes(payload, encoding=self.encoding)

    def format(self, record):
        #: add default record fields
        message = self.get_default_fields(record)

        #: add debugging and traceback information if an exception occurred
        if record.exc_info:
            message.update(self.get_debug_fields(record))

        #: add extra fields
        message.update(self.get_extra_fields(record))

        return self.serialize(message)
