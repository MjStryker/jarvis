from ctypes import *
from contextlib import contextmanager
import pyaudio
# import sounddevice as sd

ERROR_HANDLER_FUNC = CFUNCTYPE(
    None, c_char_p, c_int, c_char_p, c_int, c_char_p)


def py_error_handler(filename, line, function, err, fmt):
    pass


c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)


@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)


# print(sd.query_devices())

with noalsaerr():
    pa = pyaudio.PyAudio()
    print(pyaudio.pa.__file__)

    print('\navailable devices:')

    for i in range(pa.get_device_count()):
        dev = pa.get_device_info_by_index(i)
        name = dev['name'].encode('utf-8')
        print(i, name, dev['maxInputChannels'], dev['maxOutputChannels'])

    print('\ndefault input & output device:')
    print(pa.get_default_input_device_info())
    print(pa.get_default_output_device_info())
